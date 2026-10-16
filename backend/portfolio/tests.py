from django.test import TestCase
from django.core.management import call_command
from .models import Project
from .models import Profile
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from PIL import Image
from io import BytesIO
from tempfile import TemporaryDirectory

class AdminImageUploadTests(TestCase):
    def test_admin_uploads_and_clear_falls_back_to_url(self):
        user = get_user_model().objects.create_superuser('image-admin', password='test-password')
        self.client.force_login(user)
        with TemporaryDirectory() as media, override_settings(MEDIA_ROOT=media):
            for model, fields, key in [
                (Profile, {'name':'Test', 'role':'Developer', 'bio':'Test bio'}, 'profile'),
                (Project, {'title':'Test project', 'description':'Test', 'category':'web', 'order':0}, 'projects'),
            ]:
                obj = model.objects.create(**fields, image_url='https://example.com/fallback.jpg')
                if model is Project:
                    fields = {**fields, 'images-TOTAL_FORMS':'0', 'images-INITIAL_FORMS':'0'}
                url = f'/admin/portfolio/{model._meta.model_name}/{obj.pk}/change/'
                buffer = BytesIO()
                Image.new('RGB', (8, 8), 'blue').save(buffer, format='PNG')
                data = {**fields, 'image_url':obj.image_url, 'image':SimpleUploadedFile('photo.png', buffer.getvalue(), content_type='image/png')}
                response = self.client.post(url, data)
                self.assertEqual(response.status_code, 302)
                obj.refresh_from_db()
                self.assertTrue(obj.image.storage.exists(obj.image.name))
                payload = self.client.get('/api/portfolio/').json()[key]
                self.assertEqual((payload[0] if isinstance(payload, list) else payload)['image_url'], obj.image.url)
                response = self.client.post(url, {**fields, 'image_url':obj.image_url, 'image-clear':'on'})
                self.assertEqual(response.status_code, 302)
                payload = self.client.get('/api/portfolio/').json()[key]
                self.assertEqual((payload[0] if isinstance(payload, list) else payload)['image_url'], obj.image_url)

    def test_admin_rejects_non_image_file(self):
        from django.forms import modelform_factory
        form_class = modelform_factory(Profile, fields=['name','role','bio','image'])
        form = form_class({'name':'Test','role':'Dev','bio':'Bio'}, {'image':SimpleUploadedFile('fake.png', b'not an image', content_type='image/png')})
        self.assertFalse(form.is_valid())
        self.assertIn('image', form.errors)
class PortfolioTests(TestCase):
    def test_project_details_and_ordered_gallery(self):
        from .models import ProjectImage
        Profile.objects.create(name='Test')
        project = Project.objects.create(title='Portfolio',description='Summary',category='web',content='Full details\nSecond line',technologies='React, Django',youtube_url='https://www.youtube.com/watch?v=abcdefghijk',source_url='https://github.com/example/project')
        ProjectImage.objects.create(project=project,image='projects/gallery/second.png',caption='Second',order=2)
        ProjectImage.objects.create(project=project,image='projects/gallery/first.png',caption='First',order=1)
        data = self.client.get('/api/portfolio/').json()['projects'][0]
        self.assertEqual(data['content'], project.content)
        self.assertEqual(data['technologies'], 'React, Django')
        self.assertEqual(data['youtube_url'], project.youtube_url)
        self.assertEqual(data['source_url'], project.source_url)
        self.assertEqual([item['caption'] for item in data['images']], ['First','Second'])
        self.assertEqual(data['images'][0]['image_url'], '/media/projects/gallery/first.png')

    def test_admin_saves_gallery_upload(self):
        user = get_user_model().objects.create_superuser('gallery-admin',password='test-password')
        self.client.force_login(user)
        project = Project.objects.create(title='Gallery',description='Test',category='web')
        buffer = BytesIO()
        Image.new('RGB',(8,8),'green').save(buffer,format='PNG')
        with TemporaryDirectory() as media, override_settings(MEDIA_ROOT=media):
            response = self.client.post(f'/admin/portfolio/project/{project.pk}/change/', {
                'title':'Gallery','description':'Test','category':'web','order':0,
                'content':'Product details','technologies':'React','youtube_url':'https://youtu.be/abcdefghijk',
                'images-TOTAL_FORMS':'1','images-INITIAL_FORMS':'0',
                'images-0-image':SimpleUploadedFile('screen.png',buffer.getvalue(),content_type='image/png'),
                'images-0-caption':'Product screen','images-0-order':'0',
            })
            self.assertEqual(response.status_code,302)
            project.refresh_from_db()
            self.assertEqual(project.content,'Product details')
            self.assertEqual(project.youtube_url,'https://youtu.be/abcdefghijk')
            photo = project.images.get()
            self.assertEqual(photo.caption,'Product screen')
            self.assertTrue(photo.image.storage.exists(photo.image.name))

    def test_missing_profile_returns_actionable_error(self):
        self.assertEqual(self.client.get('/api/portfolio/').status_code,503)
    def test_seed_is_idempotent_and_api_reads_database(self):
        call_command('seed_demo');call_command('seed_demo')
        self.assertEqual(Project.objects.count(),4)
        p=Project.objects.first();p.title='Updated';p.save()
        r=self.client.get('/api/portfolio/')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['projects'][0]['title'],'Updated')
    def test_api_disallows_writes(self):
        self.assertEqual(self.client.post('/api/portfolio/').status_code,405)

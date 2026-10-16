from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from portfolio.models import Project, ProjectImage


class Command(BaseCommand):
    help = 'Add generated illustrations to demo projects without replacing existing covers.'

    def handle(self, *args, **options):
        assets = settings.BASE_DIR / 'demo_assets'
        for title, slug in [
            ('Personal Portfolio', 'portfolio'),
            ('Ứng dụng đặt sân', 'booking'),
            ('Lớp học thông minh', 'portfolio'),
            ('Ứng dụng thời tiết', 'booking'),
        ]:
            project = Project.objects.filter(title=title).first()
            path = assets / f'{slug}.png'
            if not project or not path.exists():
                self.stdout.write(f'Skipped: {slug}')
                continue
            if not project.youtube_url:
                project.youtube_url = 'https://youtu.be/0IB-Pi9jQjo'
                project.save(update_fields=['youtube_url'])
            if not project.image and not project.image_url:
                with path.open('rb') as stream:
                    project.image.save(path.name, File(stream), save=True)
            caption = 'Ảnh minh họa giao diện (AI tạo, dùng chung cho các dự án)'
            if not project.images.filter(caption=caption).exists():
                photo = ProjectImage(project=project, caption=caption)
                with path.open('rb') as stream:
                    photo.image.save(path.name, File(stream), save=True)
            self.stdout.write(self.style.SUCCESS(f'Illustration ready: {slug}'))

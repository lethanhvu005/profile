from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(name='Profile',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(default='Lê Thanh Vũ',max_length=100)),('role',models.CharField(default='Web Developer',max_length=100)),('bio',models.TextField(default='Mình yêu thích công nghệ và việc biến những ý tưởng thành trải nghiệm số. Đây là không gian chia sẻ hành trình học tập và các dự án mình xây dựng.')),('email',models.EmailField(blank=True,max_length=254)),('image_url',models.URLField(blank=True,help_text='Link HTTPS đến ảnh chân dung của bạn'))]),
        migrations.CreateModel(name='Project',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('title',models.CharField(max_length=150)),('description',models.TextField()),('category',models.CharField(choices=[('web','Web'),('mobile','Mobile'),('ai','AI')],max_length=10)),('image_url',models.URLField(blank=True)),('demo_url',models.URLField(blank=True)),('source_url',models.URLField(blank=True)),('is_demo',models.BooleanField(default=True)),('order',models.PositiveIntegerField(default=0))],options={'ordering':['order','id']})
    ]

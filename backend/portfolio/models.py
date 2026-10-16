from django.db import models
class Profile(models.Model):
    image=models.ImageField('Ảnh upload',upload_to='profiles/',blank=True,help_text='Ảnh upload được ưu tiên hơn URL ảnh.')
    name=models.CharField(max_length=100,default='Lê Thanh Vũ')
    role=models.CharField(max_length=100,default='Web Developer')
    bio=models.TextField(default='Mình yêu thích công nghệ và việc biến những ý tưởng thành trải nghiệm số. Đây là không gian chia sẻ hành trình học tập và các dự án mình xây dựng.')
    email=models.EmailField(blank=True)
    image_url=models.URLField(blank=True,help_text='Link HTTPS đến ảnh chân dung của bạn')
    def __str__(self): return self.name
class Project(models.Model):
    image=models.ImageField('Ảnh upload',upload_to='projects/',blank=True,help_text='Ảnh upload được ưu tiên hơn URL ảnh.')
    title=models.CharField(max_length=150)
    description=models.TextField()
    category=models.CharField(max_length=10,choices=[('web','Web'),('mobile','Mobile'),('ai','AI')])
    image_url=models.URLField(blank=True)
    demo_url=models.URLField(blank=True)
    source_url=models.URLField(blank=True)
    content=models.TextField('Thông tin chi tiết',blank=True)
    technologies=models.CharField('Công nghệ sử dụng',max_length=300,blank=True,help_text='Ngăn cách bằng dấu phẩy, ví dụ: React, Django, SQLite')
    youtube_url=models.URLField('Link YouTube demo',blank=True)
    is_demo=models.BooleanField(default=True)
    order=models.PositiveIntegerField(default=0)
    class Meta: ordering=['order','id']
    def __str__(self): return self.title

class ProjectImage(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField('Ảnh',upload_to='projects/gallery/')
    caption=models.CharField('Chú thích',max_length=250,blank=True)
    order=models.PositiveIntegerField('Thứ tự',default=0)
    class Meta:
        ordering=['order','id']
        verbose_name='Ảnh dự án'
        verbose_name_plural='Bộ ảnh dự án'
    def __str__(self): return self.caption or f'Ảnh {self.pk}'

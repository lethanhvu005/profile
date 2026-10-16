from django.core.management.base import BaseCommand
from portfolio.models import Profile,Project
class Command(BaseCommand):
    help='Create demo data without overwriting existing data'
    def handle(self,*args,**options):
        if not Profile.objects.exists():Profile.objects.create()
        for i,(title,category,description) in enumerate([('Personal Portfolio','web','Không gian giới thiệu bản thân và các dự án.'),('Ứng dụng đặt sân','mobile','Ý tưởng tìm kiếm sân thể thao và lựa chọn khung giờ.'),('Lớp học thông minh','ai','Ý tưởng hỗ trợ quan sát sự tập trung trong lớp học.'),('Ứng dụng thời tiết','mobile','Thực hành hiển thị thời tiết với React Native.')]):
            Project.objects.get_or_create(title=title,defaults={'category':category,'description':description,'order':i})
        self.stdout.write(self.style.SUCCESS('Demo data ready'))

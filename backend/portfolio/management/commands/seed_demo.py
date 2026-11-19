from django.core.management.base import BaseCommand
from portfolio.models import Profile, Project

SAMPLE_PROJECT_TITLES = [
    'Personal Portfolio',
    'Ứng dụng đặt sân',
    'Lớp học thông minh',
    'Ứng dụng thời tiết',
]

REAL_PROJECTS = [
    {
        'title': 'NEXA GEAR / CommerceOS',
        'category': 'web',
        'description': 'Nền tảng thương mại điện tử gaming-gear theo kiến trúc modular với storefront ReactJS, Django REST API và trang quản trị phân quyền.',
        'technologies': 'Python, Django, Django REST Framework, ReactJS, PostgreSQL, JWT, Docker, Render',
        'demo_url': 'https://nexa-commerceos-lethanhvu005-c89e.onrender.com/',
        'source_url': 'https://github.com/lethanhvu005/E-Commerce-Project',
        'youtube_url': '',
        'is_demo': False,
        'order': 0,
        'content': (
            'Vai trò: Full-stack Developer (2026 – Hiện tại)\n\n'
            'Tổng quan:\n'
            'Phát triển hệ thống thương mại điện tử gaming-gear theo kiến trúc modular gồm giao diện khách hàng (ReactJS), '
            'backend RESTful API (Django REST Framework) và cổng quản trị phân quyền (RBAC).\n\n'
            'Tính năng nổi bật:\n'
            '• Thiết kế các module RESTful API: tài khoản, danh mục sản phẩm, giỏ hàng, tồn kho theo SKU, đơn hàng, thanh toán, khuyến mãi, đánh giá và danh sách yêu thích.\n'
            '• Xác thực JWT, phân quyền RBAC, tích hợp Google OAuth và hỗ trợ đăng nhập Facebook.\n'
            '• Tìm kiếm, lọc, sắp xếp, phân trang, biến thể sản phẩm và quản lý tồn kho theo từng SKU.\n'
            '• Luồng giỏ hàng và thanh toán cập nhật tồn kho theo transaction cùng cơ chế idempotency chống trùng đơn.\n'
            '• Tích hợp thanh toán COD / VNPay Sandbox, theo dõi trạng thái đơn hàng, voucher, đánh giá sản phẩm và dashboard quản trị.\n'
            '• Cấu hình PostgreSQL, Docker, Render Blueprint, GitHub Actions cùng công cụ kiểm thử và kiểm tra bảo mật.'
        ),
    },
    {
        'title': 'SafeVision — AI Driver Safety System',
        'category': 'ai',
        'description': 'Nền tảng web hỗ trợ an toàn lái xe tích hợp AI phát hiện buồn ngủ qua camera, nhận diện cử chỉ tay SOS và dashboard giám sát.',
        'technologies': 'Python, FastAPI, ReactJS, TypeScript, OpenCV, MediaPipe, YOLO, SQLAlchemy, Docker',
        'demo_url': 'https://safevision-web.onrender.com',
        'source_url': 'https://github.com/lethanhvu005/SafeVision',
        'youtube_url': '',
        'is_demo': False,
        'order': 1,
        'content': (
            'Vai trò: Full-stack / AI Application Developer (11/2026 – Hiện tại)\n\n'
            'Tổng quan:\n'
            'Xây dựng nền tảng web hỗ trợ an toàn lái xe kết hợp phân tích buồn ngủ qua camera, nhận diện cử chỉ tay SOS và quy trình giám sát sự cố.\n\n'
            'Tính năng nổi bật:\n'
            '• Phát triển pipeline xử lý ảnh tính chỉ số mở mắt (EAR), mở miệng (MAR), tư thế đầu (head pose) và tín hiệu cử chỉ SOS.\n'
            '• Tích hợp MediaPipe / OpenCV và mô hình SOS tương thích Ultralytics (YOLO) với luật kết hợp đa tín hiệu theo thời gian để phân cấp cảnh báo.\n'
            '• Xây dựng FastAPI endpoints cho đăng ký, đăng nhập JWT, cài đặt người dùng, sự kiện buồn ngủ, lịch sử SOS và bằng chứng sự cố.\n'
            '• Sử dụng SQLAlchemy hỗ trợ SQLite khi phát triển cục bộ và PostgreSQL khi triển khai.\n'
            '• Giao diện React/TypeScript cho người dùng và quản trị viên gồm dashboard giám sát, xác nhận SOS, nhật ký gửi thông báo khẩn cấp, email retry và audit log.\n'
            '• Chuẩn bị Docker Compose và cấu hình triển khai Render cho cả frontend và backend.'
        ),
    },
]


class Command(BaseCommand):
    help = 'Remove sample projects and seed real portfolio projects without overwriting edits'

    def handle(self, *args, **options):
        if not Profile.objects.exists():
            Profile.objects.create(
                name='Lê Thành Vũ',
                role='Full-stack Developer',
                email='lethanhvu005@gmail.com',
            )
        Project.objects.filter(is_demo=True).delete()
        Project.objects.filter(title__in=SAMPLE_PROJECT_TITLES).delete()
        for item in REAL_PROJECTS:
            Project.objects.get_or_create(
                title=item['title'],
                defaults={k: v for k, v in item.items() if k != 'title'},
            )
        self.stdout.write(self.style.SUCCESS('Real portfolio data ready'))


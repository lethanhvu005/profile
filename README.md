# Portfolio — ReactJS + Django

Hướng dẫn deploy hiện tại: [DEPLOY_RENDER.md](DEPLOY_RENDER.md). Backend tự đọc `backend/.env`; mẫu biến môi trường nằm ở `backend/.env.example`.

Giao diện nền đen/vàng, 4 trang, responsive, đổi sáng/tối và lọc dự án.
React quản lý giao diện bằng component và hooks; Django cung cấp API, SQLite và trang quản trị.
Ảnh chân dung mặc định là hình vẽ SVG minh họa, có thể thay bằng URL ảnh trong Admin. Dự án mẫu có nhãn minh họa.

## Yêu cầu
Node.js 22.12+ (hoặc 24 LTS), Python 3.10–3.14. Hai terminal chạy đồng thời.

## 1. Backend — PowerShell
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```
Không cần activate môi trường ảo. Tự đặt tài khoản/mật khẩu admin khi được hỏi.
Admin: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/api/portfolio/

## 2. Frontend — terminal mới
```powershell
cd frontend
npm install
npm run dev
```
Mở địa chỉ Vite hiển thị (mặc định http://localhost:5173).
Vite chuyển /api sang Django, vì vậy không cần cấu hình CORS trong môi trường phát triển.
Nếu báo không kết nối được Django, kiểm tra backend đã chạy cổng 8000 rồi tải lại trang.

## 3. Cá nhân hóa
- Django Admin → Profiles: đổi tên, chức danh, giới thiệu trang chủ, email hiển thị và URL ảnh chân dung.
- Django Admin → Projects: thêm/sửa/xóa dự án, loại, ảnh, liên kết demo/GitHub; bỏ is_demo khi đã thay bằng dự án thật.
- Nội dung trang Giới thiệu và các liên kết GitHub: frontend/src/pages/About.jsx, Contact.jsx, Home.jsx.
- Màu sắc và responsive: frontend/src/styles.css.
- API: backend/portfolio/views.py; dữ liệu: models.py.
- API chỉ đọc; thay đổi dữ liệu qua Admin yêu cầu đăng nhập.

## Kiểm tra và build
```powershell
# Trong backend
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
# Trong frontend
npm run build
```

## Triển khai thực tế
Đây là source chạy local. Website demo trước đó vẫn là bản HTML tĩnh.
Khi deploy React + Django, phục vụ frontend/dist bằng static host/reverse proxy và chuyển /api sang Django; cấu hình Django Admin/static riêng.
Đặt DJANGO_DEBUG=0, DJANGO_SECRET_KEY ngẫu nhiên và DJANGO_ALLOWED_HOSTS đúng tên miền; dùng HTTPS và máy chủ WSGI thay runserver.
Admin hỗ trợ upload ảnh bìa, bộ ảnh dự án và link YouTube demo. Chưa có form gửi mail.

## Trạng thái xác minh khi bàn giao
- npm install và npm run build: thành công.
- Django 5.2.18: manage.py check không có lỗi.
- manage.py test: 3 bài kiểm tra đều đạt (API đọc dữ liệu DB, seed không nhân bản, API từ chối ghi).
- makemigrations --check --dry-run: không có thay đổi chưa tạo migration.
- Chưa kiểm tra trực quan bằng trình duyệt.

## Cập nhật giao diện
Đã sửa khung ảnh dọc, tăng cỡ chữ/nút, cân đối khoảng cách trên màn hình rộng và dùng icon SVG. Nếu trình duyệt đang thu nhỏ, nhấn Ctrl+0 để về mức zoom 100%.

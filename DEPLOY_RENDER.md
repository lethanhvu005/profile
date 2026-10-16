# Deploy React + Django lên Render

## Cấu hình đã chuẩn bị

- Một Docker Web Service phục vụ React, `/api/`, `/admin/`, `/static/` và `/media/` trên cùng domain. Không cần frontend env hoặc CORS.
- `render.yaml`: plan Starter và persistent disk 1 GB. **Có phí cho service và disk**; xem giá hiện tại trên Render trước khi tạo.
- SQLite `/var/data/db.sqlite3` và ảnh `/var/data/media` nằm trên disk để tồn tại qua restart/deploy.
- Phù hợp portfolio cá nhân, một instance. Khi cần nhiều instance, chuyển sang PostgreSQL và object storage.
- Docker build React và collectstatic; migrate chạy lúc start vì disk chỉ có ở runtime.

## Deploy

1. Commit/push source lên GitHub, gồm Dockerfile, start.sh, render.yaml, migrations, frontend/package-lock.json và backend/demo_assets. Không commit `.env`, SQLite, media hoặc tài khoản admin.
2. Render → New → Blueprint → kết nối repository → chọn branch có `render.yaml`.
3. Kiểm tra plan/disk và chi phí, rồi tạo service. Render tự tạo secret key và cấp domain; cấu hình tự nhận `RENDER_EXTERNAL_HOSTNAME`.
4. Chờ deploy Live. Mở URL service, `/health/` và `/api/portfolio/`.
5. Trong Render Shell chạy:

   ```sh
   cd /app/backend
   python manage.py createsuperuser
   ```

6. Vào `/admin/` bằng tài khoản vừa tạo. Sửa Profile, Project, ảnh và video. Bấm dự án trên trang web để kiểm tra ảnh/video.
7. Restart service rồi kiểm tra nội dung và ảnh còn nguyên.

## Dữ liệu hiện tại trên máy

Lần đầu deploy tạo dữ liệu demo, hai ảnh minh họa dùng chung và link video mẫu. **Dữ liệu cá nhân trong SQLite local và ảnh upload local không tự chuyển lên Render.** Có thể nhập lại qua admin hoặc chuyển dữ liệu riêng qua SSH; không push database lên GitHub. Admin local cũng không tự chuyển lên hosting.

## Biến môi trường

Local: `backend/.env` được tự nạp, đã được gitignore. Máy khác sao chép `backend/.env.example` thành `.env`, thay secret placeholder bằng giá trị ngẫu nhiên riêng.

Render: dùng Environment trong dashboard, không upload `.env` local. Blueprint cấu hình:

| Biến | Giá trị |
|---|---|
| DJANGO_DEBUG | 0 |
| DJANGO_SECRET_KEY | Render tự sinh |
| DJANGO_DB_PATH | /var/data/db.sqlite3 |
| DJANGO_MEDIA_ROOT | /var/data/media |
| DJANGO_ALLOWED_HOSTS | localhost,127.0.0.1; domain Render được tự thêm |

Nếu dùng domain riêng, thêm domain vào `DJANGO_ALLOWED_HOSTS` và origin `https://your-domain` vào `DJANGO_CSRF_TRUSTED_ORIGINS` (nhiều giá trị ngăn cách bằng dấu phẩy).

## Lưu ý vận hành

- Media được phục vụ qua FileResponse với kiểm tra đường dẫn và loại ảnh; static qua WhiteNoise.
- Không dùng Render Free với SQLite/ảnh local: filesystem không bền vững, không gắn được persistent disk.
- Disk chỉ dùng một instance và deploy có khoảng gián đoạn. Sao lưu SQLite bằng SQLite backup API và sao lưu thư mục media định kỳ; không xem git là bản sao lưu dữ liệu.
- Chưa tạo dịch vụ hoặc kiểm chứng URL Render Live từ phiên làm việc này.

Tài liệu: https://render.com/docs/disks và https://render.com/docs/deploy-django

# Render Free + Neon PostgreSQL + Cloudinary

Ứng dụng chạy trên Render Free. Neon lưu database và tài khoản admin; Cloudinary lưu ảnh upload. Không cần ổ đĩa hoặc Shell trên Render. Các dịch vụ có giới hạn sử dụng; kiểm tra gói trước khi đăng ký.

## 1. Tạo database Neon

1. Đăng ký tại https://console.neon.tech/ và tạo project `portfolio`.
2. Chọn region gần service Render.
3. Chọn **Connect**, tắt **Connection pooling** để lấy direct PostgreSQL URL dùng cho migration và ứng dụng.
4. Giữ tham số TLS như `sslmode=require` trong URL.
5. Lưu URL vào biến `DATABASE_URL` trên Render. Không gửi URL vào chat hoặc đưa lên GitHub vì có chứa mật khẩu.

## 2. Tạo nơi lưu ảnh Cloudinary

1. Đăng ký tại https://cloudinary.com/ và mở Console.
2. Trong **API Keys**, lấy **Cloud name**, **API key** và **API secret**.
3. Nhập vào ba biến môi trường tương ứng trên Render ở bảng bên dưới.

Backend dùng thông tin xác thực để upload ảnh; không cần unsigned upload preset.

## 3. Deploy lên Render

Push code lên GitHub. Vào **Render → New → Blueprint**, chọn repository chứa `render.yaml`. Blueprint dùng `plan: free`, không có persistent disk.

Nếu đã có service, cập nhật **Environment** và deploy commit mới; kiểm tra **Instance Type** là **Free**. Không xóa disk cũ nếu chưa sao lưu dữ liệu cần giữ.

Điền các biến trong **Environment**:

| Biến | Giá trị |
|---|---|
| `DJANGO_DEBUG` | `0` |
| `DJANGO_SECRET_KEY` | Blueprint tự sinh; service tạo thủ công cần secret ngẫu nhiên dài |
| `DATABASE_URL` | PostgreSQL URL từ Neon |
| `CLOUDINARY_CLOUD_NAME` | Cloud name |
| `CLOUDINARY_API_KEY` | API key |
| `CLOUDINARY_API_SECRET` | API secret |
| `DJANGO_SUPERUSER_USERNAME` | Tên admin bạn tự chọn |
| `DJANGO_SUPERUSER_EMAIL` | Email của bạn |
| `DJANGO_SUPERUSER_PASSWORD` | Mật khẩu mạnh do bạn tự đặt |
| `SEED_DEMO` | `1` cho lần đầu, sau đó đổi thành `0` |

Domain Render được tự nhận. Nếu dùng domain riêng, thêm domain vào `DJANGO_ALLOWED_HOSTS` và thêm origin `https://domain` vào `DJANGO_CSRF_TRUSTED_ORIGINS`.

Khi khởi động, ứng dụng chạy migration, tạo admin đầu tiên và nạp dữ liệu mẫu nếu `SEED_DEMO=1`. Ứng dụng không đổi mật khẩu admin hiện có và không nâng quyền tài khoản thường. Nếu thiếu cấu hình, xem thông báo trong **Logs**. Không cần dùng Shell.

## 4. Sau khi service báo Live

1. Mở `/health/`, `/api/portfolio/` và `/admin/` trên domain của service.
2. Đăng nhập bằng username và password đã đặt trong Environment.
3. Xóa ba biến `DJANGO_SUPERUSER_*` sau khi tạo tài khoản thành công. Tài khoản đã được lưu trong Neon.
4. Đổi `SEED_DEMO=0` để ứng dụng không thêm lại nội dung mẫu đã xóa.
5. Upload ảnh và thêm link YouTube trong admin. URL ảnh phải là HTTPS của Cloudinary.
6. Restart hoặc deploy lại, rồi kiểm tra dữ liệu và ảnh vẫn còn nguyên.

Nếu quên mật khẩu, trên máy local cấu hình `DATABASE_URL` trỏ tới Neon trong `backend/.env`, rồi chạy từ thư mục `backend`:

```powershell
.\.venv\Scripts\python.exe manage.py changepassword <username>
```

Thay `<username>` bằng tên admin của bạn. Ứng dụng không tự reset mật khẩu mỗi lần khởi động.

## Local và dữ liệu cũ

- `backend/.env` được tự đọc và đã được gitignore. `.env.example` chỉ chứa mẫu cấu hình.
- Để `DATABASE_URL` và ba biến Cloudinary trống nếu muốn tiếp tục dùng SQLite và ảnh local.
- Frontend không cần file env vì chạy cùng domain với API.
- Dữ liệu SQLite, ảnh cá nhân và tài khoản admin local không tự chuyển lên Neon. Bản deploy đầu có dữ liệu mẫu; nhập lại nội dung và upload lại ảnh qua admin.
- Không push `db.sqlite3` hoặc `.env` lên GitHub.
- Database lưu public ID ảnh và link YouTube; Cloudinary lưu file ảnh.

Production sẽ dừng nếu thiếu PostgreSQL hoặc Cloudinary để tránh ghi dữ liệu vào filesystem tạm. Render Free có thể ngủ khi không hoạt động; theo dõi giới hạn sử dụng và sao lưu dữ liệu.

## Trạng thái xác minh

Chưa có thông tin kết nối Neon/Cloudinary nên chưa kiểm chứng kết nối cloud, upload thật hoặc Render Live. Kiểm tra local không thay thế bước kiểm tra trên hosting.

Tài liệu tham khảo:

- https://render.com/docs/free
- https://neon.com/docs
- https://github.com/klis87/django-cloudinary-storage

# Task 1 — Báo cáo kiểm thử GUI

## Phạm vi và nguồn dữ liệu

- **SUT:** EShop Web
- **Màn hình:** Đăng ký (Registration), Đăng nhập (Login), Quên mật khẩu (Forgot Password), Hồ sơ (Profile)
- **Nguồn kết quả:** [`02-checklist.csv`](./02-checklist.csv) hiện tại và các ảnh chụp gốc hiện có trong [`evidence/gui/`](../../evidence/gui/)
- **Môi trường thực thi ghi trong checklist:** Trình duyệt tích hợp VS Code (Electron 43.8.3; Chrome 150.0.7871.250), Windows NT 10.0, khung nhìn 1281 × 676
- **Khoảng thời gian thực thi ghi trong checklist:** 2026-11-09 10:21–10:35 +07; checklist không ghi thời điểm chính xác cho từng mục.
- Đây là báo cáo tổng hợp ở giai đoạn báo cáo. Không chạy lại kiểm thử, không chỉnh sửa kết quả mong đợi hay kết quả kiểm thử và không thay đổi source EShop.

## Kết quả tổng quan

| Trạng thái | Số lượng |
|---|---:|
| Đạt (Passed) | 29 |
| Không đạt (Failed) | 34 |
| Chưa chạy (Not Run) | 3 |
| Bị chặn (Blocked) | 0 |
| Không áp dụng (N/A) | 0 |
| **Tổng** | **66** |

### Kết quả theo nhóm tiêu chí

| Nhóm | Đạt | Không đạt | Chưa chạy | Tổng |
|---|---:|---:|---:|---:|
| IA-01 | 6 | 6 | 0 | 12 |
| IA-02 | 16 | 21 | 2 | 39 |
| IA-03 | 4 | 5 | 1 | 10 |
| IA-04 | 3 | 2 | 0 | 5 |
| **Tổng** | **29** | **34** | **3** | **66** |

## Các mục chưa chạy

- **GUI-014 — thông báo email Đăng ký không hợp lệ:** Chưa chạy vì trường email ở màn hình Đăng ký dùng `type=text`; gửi email sai định dạng có thể tạo tài khoản thử nghiệm ngoài ý muốn. Không gửi biểu mẫu đó.
- **GUI-016 — thông báo khi mật khẩu Đăng ký không khớp:** Chưa chạy vì biểu mẫu không có trường xác nhận mật khẩu nên không thể nhập trạng thái mật khẩu không khớp. Trường còn thiếu được ghi ở GUI-008.
- **GUI-043 — điều hướng quay lại Đăng nhập:** Chưa chạy vì GUI-042 xác nhận màn hình Quên mật khẩu ban đầu không có điều khiển quay lại để kích hoạt.

## Các bản nháp bug report đã gộp

34 ID checklist Không đạt được gộp thành các phát hiện dưới đây; ID cụ thể và đường dẫn ảnh nằm trong [`04-bug-reports.md`](./04-bug-reports.md). Mức độ nghiêm trọng chỉ là đề xuất để người dùng xem xét, chưa phải mức ưu tiên được phê duyệt.

| # | Phát hiện dự thảo | ID checklist | Mức độ đề xuất | Bằng chứng |
|---:|---|---|---|---|
| 1 | Các trang được chọn thiếu tiêu đề H1 theo yêu cầu | GUI-001, GUI-036, GUI-052 | Thấp | Có ảnh chụp |
| 2 | Tiêu đề trang đích Đăng nhập lại ghi là Đăng ký | GUI-020, GUI-023 | Trung bình | Có ảnh chụp |
| 3 | Trường email ở Đăng ký, Đăng nhập và Quên mật khẩu dùng kiểu `text` | GUI-006, GUI-026, GUI-039 | Trung bình | Có ảnh chụp |
| 4 | Biểu mẫu Đăng ký không có trường xác nhận mật khẩu | GUI-008 | Trung bình | Có ảnh chụp |
| 5 | Biểu mẫu đặt lại mật khẩu không có trường xác nhận mật khẩu | GUI-047 | Trung bình | Có ảnh chụp |
| 6 | Trường bắt buộc thiếu dấu hoa thị hiển thị | GUI-009, GUI-028, GUI-040, GUI-048, GUI-058 | Thấp | Có ảnh chụp |
| 7 | Hướng dẫn mật khẩu Đăng ký không liệt kê nhóm ký tự đặc biệt được phép | GUI-011 | Thấp | Có ảnh chụp |
| 8 | Trường mật khẩu Đăng nhập không che ký tự đã nhập | GUI-027 | Cao | Có ảnh chụp |
| 9 | Màn hình Đăng nhập có nhãn hiển thị cho người dùng bằng tiếng Anh | GUI-024 | Thấp | Có ảnh chụp |
| 10 | Thông báo xác thực Đăng nhập xuất hiện bên dưới nút gửi | GUI-029, GUI-030 | Trung bình | Có ảnh crop bảo vệ dữ liệu |
| 11 | Mục điều hướng Đăng ký và Đăng nhập không được đánh dấu là trang hiện tại | GUI-021, GUI-035 | Thấp | Có ảnh chụp |
| 12 | Thứ tự Tab ở Đăng nhập đưa liên kết Đăng ký lên trước nút gửi | GUI-032 | Trung bình | Có ảnh chụp |
| 13 | Bước đầu Quên mật khẩu không có điều khiển hiển thị để quay lại Đăng nhập | GUI-042 | Trung bình | Có ảnh chụp |
| 14 | Luồng Quên mật khẩu không có chỉ báo bước | GUI-038, GUI-044, GUI-050 | Trung bình | Có ảnh của cả hai bước; OTP trong ảnh GUI-044 đã được che trên bản crop |
| 15 | Hướng dẫn OTP yêu cầu bốn chữ số thay vì sáu | GUI-046 | Trung bình | Có ảnh nhãn đã crop |
| 16 | Email khôi phục sai định dạng tạo hộp thoại trình duyệt thay vì xác thực nội tuyến theo yêu cầu | GUI-041 | Trung bình | Có ảnh chụp |
| 17 | Biểu mẫu đặt lại hiển thị hộp thoại mật khẩu yếu; chưa xác minh phản hồi OTP | GUI-049 | Trung bình | Ảnh crop thể hiện cảnh báo mật khẩu yếu; không kết luận về phản hồi OTP sai |
| 18 | Xác thực số điện thoại hồ sơ hiển thị bằng hộp thoại thay vì nội tuyến | GUI-059 | Trung bình | Ảnh crop thể hiện cảnh báo số điện thoại sai; đã lược bỏ dữ liệu hồ sơ |
| 19 | Thao tác đăng xuất có nhãn “Thoát” thay vì “Đăng xuất” | GUI-063 | Thấp | Có ảnh chụp |
| 20 | Trạng thái lịch sử đơn hàng trống không có hình minh họa | GUI-064 | Thấp | Có ảnh chụp |
| 21 | Nút thao tác chính của Đăng ký có màu đỏ thay vì xanh dương | GUI-066 | Thấp | Có ảnh chụp |

### Quyết định review về Bug #4

Theo quyết định của bạn, không tạo bug report độc lập cho GUI-026. Phần `type="text"` của trường Đăng nhập đã được gộp vào Bug #3 (hiện đánh số #3); vấn đề nhãn “Username” không được theo dõi thành bug riêng. **GUI-026 vẫn giữ nguyên trong checklist** và kết quả kiểm thử không thay đổi.

## Giới hạn bằng chứng và tính nhất quán nguồn

- Checklist hiện tại ghi **GUI-065 Đạt (Passed)**, với thông tin một đơn hàng trong Actual Result và ghi chú rằng không bắt buộc có ảnh. Báo cáo giữ nguyên trạng thái này; không tự xác minh lại hoặc tạo lại trạng thái lịch sử đơn hàng.
- [`03-execution-summary.md`](./03-execution-summary.md) trước đó ghi 28 Passed / 35 Failed / 3 Not Run và cho biết GUI-065 là Not Run. Tóm tắt đó phản ánh một phiên bản checklist cũ, không khớp CSV hiện tại (29 Passed / 34 Failed / 3 Not Run). Báo cáo này dùng số liệu CSV hiện tại và không chỉnh sửa execution summary cũ.
- Ảnh GUI-044 do người dùng cung cấp ghi lại trạng thái bước hai; báo cáo liên kết bản crop đã che banner OTP và giá trị OTP đã nhập. Ảnh gốc được giữ nguyên.
- Với GUI-049, người dùng xác nhận rằng khi gửi OTP sai cùng mật khẩu yếu, hệ thống hiện cảnh báo “Mật khẩu quá yếu!”. Báo cáo ghi nhận hiện tượng đó và **không** khẳng định đã tiếp cận hoặc kiểm tra được phản hồi OTP sai.
- Ảnh GUI-059 do người dùng cung cấp hiển thị hộp thoại cảnh báo số điện thoại không hợp lệ; báo cáo liên kết bản crop đã lược bỏ dữ liệu hồ sơ thử nghiệm. Ảnh gốc được giữ nguyên.
- Ảnh lỗi Đăng nhập gốc hiển thị mật khẩu thử nghiệm đã nhập trong trường không được che. Bug report chỉ liên kết ảnh crop hiển thị nút và thông báo lỗi, không chứa các giá trị đã nhập; ảnh gốc không bị chỉnh sửa.
- Không tạo hoặc phát hành GitHub Issue. Không push Git. Các phát hiện dự thảo cần được người dùng xem xét trước khi báo cáo ra bên ngoài.

## Kết luận để xem xét

Báo cáo sẵn sàng để người dùng xem xét. Cần lưu ý các mức độ nghiêm trọng đề xuất, giới hạn của GUI-049 (chưa xác minh phản hồi OTP) và kết quả GUI-065 Đạt nhưng không có ảnh trước khi phê duyệt bước tiếp theo.

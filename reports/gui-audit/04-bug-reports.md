# Các bug report GUI đã gộp — Task 1

Các phát hiện dưới đây là bản nháp cần người dùng xem xét. Mức độ nghiêm trọng chỉ là đề xuất, chưa được xác nhận. Quan sát và kết quả mong đợi lấy từ `02-checklist.csv` hiện tại, trừ những chỗ ghi rõ là quan sát mới do người dùng xác nhận. Không chạy lại kiểm thử khi chuẩn bị báo cáo.

**Môi trường ghi nhận quan sát trong checklist:** trình duyệt tích hợp VS Code (Electron 43.8.3; Chrome 150.0.7871.250), Windows NT 10.0, khung nhìn 1281 × 676. Checklist ghi khoảng thời gian thực thi là 2026-11-09 10:21–10:35 +07, không ghi thời điểm riêng cho từng mục. GUI-044 và GUI-059 có thêm ảnh mới do người dùng cung cấp; không chạy lại kiểm thử khi cập nhật báo cáo.

## 1. Các trang được chọn thiếu tiêu đề H1 theo yêu cầu

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-001, GUI-036, GUI-052
- **URL SUT / màn hình:** `http://127.0.0.1:5173/register`, `/forgot-password`, `/profile`
- **Mức độ nghiêm trọng (đề xuất):** Thấp — cả ba màn hình đều thiếu cấu trúc tiêu đề cấp trang theo yêu cầu, làm giảm độ rõ ràng của cấu trúc trang và điều hướng bằng heading.
- **Bằng chứng:** [GUI-001](../../evidence/gui/GUI-001-registration-heading.png), [GUI-036](../../evidence/gui/GUI-036-forgot-heading.png), [GUI-052](../../evidence/gui/GUI-052-profile-heading.png)

### Điều kiện tiên quyết
Mở từng màn hình được liệt kê; cần người dùng đã đăng nhập để vào Hồ sơ.

### Các bước tái hiện
1. Mở `/register`, `/forgot-password` hoặc `/profile` sau khi đăng nhập.
2. Kiểm tra tiêu đề hiển thị và cấp heading của trang.

### Kết quả GUI mong đợi
Mỗi trang có đúng một tiêu đề H1 mô tả trang, theo yêu cầu GUI FR-21.

### Kết quả GUI thực tế
Checklist ghi nhận tiêu đề Đăng ký và Quên mật khẩu là H2; Hồ sơ có hai tiêu đề phần H2 và không có H1.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Báo cáo gộp tình trạng thiếu H1 giống nhau ở ba màn hình. Màn hình Đăng nhập được ghi riêng vì tiêu đề còn ghi sai tên trang.

---

## 2. Tiêu đề trang đích Đăng nhập lại ghi là Đăng ký

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-020, GUI-023
- **URL SUT / màn hình:** `http://127.0.0.1:5173/login` (cũng có thể truy cập từ màn hình Đăng ký)
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — tiêu đề trang đích xác định sai màn hình hiện tại.
- **Bằng chứng:** [GUI-020](../../evidence/gui/GUI-020-registration-link-destination-heading.png), [GUI-023](../../evidence/gui/GUI-023-login-heading.png)

### Điều kiện tiên quyết
Mở màn hình Đăng ký.

### Các bước tái hiện
1. Kích hoạt liên kết “Đăng nhập” trong biểu mẫu.
2. Kiểm tra tiêu đề trang đích tại `/login`.

### Kết quả GUI mong đợi
Màn hình Đăng nhập mở ra với tiêu đề xác định đúng trang Đăng nhập.

### Kết quả GUI thực tế
Đường dẫn mở `/login`, nhưng tiêu đề là “Đăng Ký” và được hiển thị ở cấp H2.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện 1 cũng đề cập việc thiếu H1; phát hiện này tập trung vào tiêu đề trang Đăng nhập bị sai.

---

## 3. Trường email ở Đăng ký, Đăng nhập và Quên mật khẩu dùng kiểu nhập văn bản

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-006, GUI-026, GUI-039
- **URL SUT / màn hình:** `http://127.0.0.1:5173/register`, `/login`, `/forgot-password`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — các trường không dùng kiểu nhập email/khả năng xác thực HTML như tài liệu yêu cầu.
- **Bằng chứng:** [GUI-006](../../evidence/gui/GUI-006-registration-email-type.png), [GUI-026](../../evidence/gui/GUI-026-login-email-type-label.png), [GUI-039](../../evidence/gui/GUI-039-forgot-email-type.png)

### Điều kiện tiên quyết
Mở các màn hình Đăng ký, Đăng nhập và Quên mật khẩu.

### Các bước tái hiện
1. Kiểm tra trường email tại `/register`.
2. Kiểm tra trường email tại `/login`.
3. Kiểm tra trường email khôi phục tại `/forgot-password`.

### Kết quả GUI mong đợi
Mỗi trường email được khai báo `type=email`, theo FR-22.

### Kết quả GUI thực tế
Cả ba trường đều được khai báo `type=text`.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Quyết định review: chỉ gộp vấn đề `type="text"` của GUI-026 vào phát hiện này. Không tạo bug độc lập cho nhãn “Username”; GUI-026 vẫn được giữ nguyên trong checklist.

---

## 4. Biểu mẫu Đăng ký không có trường xác nhận mật khẩu

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-008, GUI-016
- **URL SUT / màn hình:** `http://127.0.0.1:5173/register`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — không thể thực hiện bước xác nhận được quy định trong FR-01.
- **Bằng chứng:** [GUI-008](../../evidence/gui/GUI-008-registration-confirmation.png)

### Điều kiện tiên quyết
Mở `/register`.

### Các bước tái hiện
1. Kiểm tra tất cả trường trong biểu mẫu Đăng ký.
2. Tìm trường riêng để xác nhận mật khẩu.

### Kết quả GUI mong đợi
Có trường xác nhận mật khẩu riêng, hiển thị và che ký tự đã nhập.

### Kết quả GUI thực tế
Chỉ có trường tên, email và mật khẩu. Không thể chạy mục kiểm tra thông báo mật khẩu không khớp GUI-016 vì thiếu trường xác nhận.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
GUI-016 là Chưa chạy (Not Run), không phải Không đạt (Failed); mục này được dẫn ở đây để giải thích trạng thái phụ thuộc không thể tạo.

---

## 5. Biểu mẫu đặt lại mật khẩu không có trường xác nhận mật khẩu

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-047
- **URL SUT / màn hình:** `http://127.0.0.1:5173/forgot-password` (bước đặt lại mật khẩu)
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — biểu mẫu đặt lại thiếu điều khiển xác nhận theo yêu cầu FR-03.
- **Bằng chứng:** [GUI-047 crop đã che](../../evidence/gui/report-redacted/GUI-047-confirm-missing-redacted.png) — bản crop đã loại phần OTP hiển thị trong ảnh gốc.

### Điều kiện tiên quyết
Luồng khôi phục đã đến bước đặt lại mật khẩu.

### Các bước tái hiện
1. Kiểm tra các trường trong biểu mẫu ở bước đặt lại.
2. Tìm trường nhập xác nhận mật khẩu riêng.

### Kết quả GUI mong đợi
Có cả trường mật khẩu mới và xác nhận mật khẩu; cả hai đều che ký tự đã nhập.

### Kết quả GUI thực tế
Checklist ghi nhận trường OTP và mật khẩu mới nhưng không có trường xác nhận mật khẩu.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Vấn đề này khác với trường xác nhận mật khẩu bị thiếu ở màn hình Đăng ký.

---

## 6. Trường bắt buộc thiếu dấu hoa thị hiển thị

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-009, GUI-028, GUI-040, GUI-048, GUI-058
- **URL SUT / màn hình:** Đăng ký, Đăng nhập, Quên mật khẩu, Hồ sơ
- **Mức độ nghiêm trọng (đề xuất):** Thấp — các trường bắt buộc không được đánh dấu trực quan như yêu cầu FR-22.
- **Bằng chứng:** [GUI-009](../../evidence/gui/GUI-009-registration-required-markers.png), [GUI-028](../../evidence/gui/GUI-028-login-required-markers.png), [GUI-040](../../evidence/gui/GUI-040-forgot-required-marker.png), [GUI-048 crop đã che](../../evidence/gui/report-redacted/GUI-048-required-markers-redacted.png), [GUI-058](../../evidence/gui/GUI-058-profile-required-markers.png)

### Điều kiện tiên quyết
Mở từng màn hình; mục GUI-048 của Quên mật khẩu cần ở bước đặt lại.

### Các bước tái hiện
1. Kiểm tra nhãn các trường được quy định là bắt buộc trên từng biểu mẫu.
2. Kiểm tra dấu hoa thị bắt buộc bên cạnh từng nhãn tương ứng.

### Kết quả GUI mong đợi
Các trường bắt buộc có dấu hoa thị hiển thị bên cạnh nhãn, theo FR-22.

### Kết quả GUI thực tế
Checklist ghi nhận không có dấu hoa thị ở Đăng ký, Đăng nhập, cả hai bước khôi phục hoặc trường Họ tên bắt buộc trong Hồ sơ.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện này gộp cùng một vấn đề trình bày lặp lại. GUI-058 ghi nhận trực tiếp trạng thái bắt buộc của trường Họ tên trên trình duyệt.

---

## 7. Hướng dẫn mật khẩu Đăng ký không liệt kê ký tự đặc biệt được phép

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-011
- **URL SUT / màn hình:** `http://127.0.0.1:5173/register`
- **Mức độ nghiêm trọng (đề xuất):** Thấp — văn bản trợ giúp không truyền đạt đầy đủ quy tắc mật khẩu đã được mô tả.
- **Bằng chứng:** [GUI-011](../../evidence/gui/GUI-011-registration-special-chars-guidance.png)

### Điều kiện tiên quyết
Mở `/register`.

### Các bước tái hiện
1. Đọc văn bản trợ giúp bên dưới trường mật khẩu.
2. Đối chiếu hướng dẫn hiển thị với các ký tự được phép trong FR-01.

### Kết quả GUI mong đợi
Hướng dẫn hiển thị liệt kê nhóm ký tự đặc biệt được phép.

### Kết quả GUI thực tế
Văn bản trợ giúp có nhắc đến ký tự đặc biệt nhưng không liệt kê các ký tự được phép.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Báo cáo này chỉ đánh giá hướng dẫn hiển thị, không đánh giá việc thực thi quy tắc mật khẩu.

---

## 8. Trường mật khẩu Đăng nhập không che ký tự đã nhập

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-027
- **URL SUT / màn hình:** `http://127.0.0.1:5173/login`
- **Mức độ nghiêm trọng (đề xuất):** Cao — mật khẩu hiển thị rõ khi nhập thay vì được che.
- **Bằng chứng:** [GUI-027](../../evidence/gui/GUI-027-login-password-type.png)

### Điều kiện tiên quyết
Mở `/login`.

### Các bước tái hiện
1. Kiểm tra kiểu nhập của trường mật khẩu.
2. Nhập giá trị thử nghiệm và quan sát cách ký tự hiển thị.

### Kết quả GUI mong đợi
Trường mật khẩu dùng `type=password` theo FR-22 để che các ký tự đã nhập.

### Kết quả GUI thực tế
Trường dùng `type=text`; ảnh trong checklist cho thấy giá trị thử nghiệm đã nhập hiển thị rõ.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Ảnh lỗi Đăng nhập gốc có mật khẩu thử nghiệm không được liên kết ở đây. Ảnh được dẫn chỉ ghi nhận kiểu của trường.

---

## 9. Màn hình Đăng nhập có nhãn hiển thị cho người dùng bằng tiếng Anh

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-024
- **URL SUT / màn hình:** `http://127.0.0.1:5173/login`
- **Mức độ nghiêm trọng (đề xuất):** Thấp — màn hình không nhất quán với yêu cầu sử dụng tiếng Việt FR-21.
- **Bằng chứng:** [GUI-024](../../evidence/gui/GUI-024-login-language.png)

### Điều kiện tiên quyết
Mở `/login`.

### Các bước tái hiện
1. Kiểm tra tiêu đề, nhãn và thao tác chính trên màn hình Đăng nhập.

### Kết quả GUI mong đợi
Nhãn và thao tác hướng đến người dùng được viết bằng tiếng Việt, ngoại trừ thuật ngữ kỹ thuật thông dụng.

### Kết quả GUI thực tế
Màn hình hiển thị “Username” và “Sign In”.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện này liên quan đến ngôn ngữ hiển thị trên màn hình Đăng nhập.

---

## 10. Thông báo xác thực Đăng nhập xuất hiện bên dưới nút gửi

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-029, GUI-030
- **URL SUT / màn hình:** `http://127.0.0.1:5173/login`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — FR-22 yêu cầu thông báo lỗi xuất hiện phía trên nút gửi.
- **Bằng chứng:** [Ảnh crop bảo vệ dữ liệu của GUI-030](../../evidence/gui/report-redacted/GUI-030-login-error-feedback-redacted.png). Ảnh gốc được giữ nguyên; bản crop đã loại thông tin đăng nhập thử nghiệm đã nhập.

### Điều kiện tiên quyết
Mở `/login`.

### Các bước tái hiện
1. Gửi email sai định dạng cùng mật khẩu thử nghiệm không khớp.
2. Gửi thông tin đăng nhập thử nghiệm không hợp lệ.
3. Quan sát vị trí thông báo lỗi Đăng nhập so với nút gửi.

### Kết quả GUI mong đợi
Thông báo xác thực email và lỗi đăng nhập xuất hiện phía trên nút gửi, dễ đọc.

### Kết quả GUI thực tế
Email sai định dạng tạo phản hồi xác thực chung bên dưới nút “Sign In”; thông báo đăng nhập thất bại cũng xuất hiện bên dưới nút đó.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi gốc và bản crop bảo vệ dữ liệu.

### Ghi chú / điểm chưa chắc chắn
Kết quả thực tế của GUI-029 dựa trên việc gửi địa chỉ sai định dạng và nhận lỗi đăng nhập chung; báo cáo không khẳng định đã kiểm tra cơ chế xác thực email gốc của trình duyệt.

---

## 11. Mục điều hướng Đăng ký và Đăng nhập không được đánh dấu là trang hiện tại

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-021, GUI-035
- **URL SUT / màn hình:** `http://127.0.0.1:5173/register`, `/login`
- **Mức độ nghiêm trọng (đề xuất):** Thấp — không thể nhận biết trực quan trang hiện tại trên thanh điều hướng chung, trái với FR-23.
- **Bằng chứng:** [GUI-021](../../evidence/gui/GUI-021-registration-active-nav.png), [GUI-035](../../evidence/gui/GUI-035-login-active-nav.png)

### Điều kiện tiên quyết
Mở riêng từng màn hình Đăng ký và Đăng nhập.

### Các bước tái hiện
1. Kiểm tra thanh điều hướng chung trên từng màn hình.
2. Xác định xem trang hiện tại có được phân biệt trực quan hay không.

### Kết quả GUI mong đợi
Mục điều hướng tương ứng với trang hiện tại được làm nổi bật trực quan.

### Kết quả GUI thực tế
Các liên kết Đăng ký và Đăng nhập có cùng kiểu hiển thị; checklist không ghi nhận kiểu đang chọn hoặc trạng thái `aria-current`.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Hồ sơ được ghi nhận là có làm nổi bật nên không nằm trong phát hiện này.

---

## 12. Thứ tự Tab ở Đăng nhập đưa liên kết Đăng ký lên trước nút gửi

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-032
- **URL SUT / màn hình:** `http://127.0.0.1:5173/login`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — thứ tự focus bằng bàn phím quan sát được khác với thứ tự trực quan từ trên xuống dưới đã quy định.
- **Bằng chứng:** [Focus tại liên kết Đăng ký](../../evidence/gui/GUI-032-login-tab-order-register-link.png), [focus tại nút gửi](../../evidence/gui/GUI-032-login-tab-order-submit.png)

### Điều kiện tiên quyết
Mở `/login`; có thể tương tác bằng bàn phím.

### Các bước tái hiện
1. Đưa focus vào trường Email.
2. Nhấn Tab liên tục và ghi lại các điều khiển lần lượt nhận focus.

### Kết quả GUI mong đợi
Focus di chuyển theo thứ tự trực quan từ trên xuống dưới đã quy định.

### Kết quả GUI thực tế
Thứ tự quan sát được sau trường Email là Mật khẩu, Quên mật khẩu, liên kết Đăng ký, rồi nút “Sign In”. Liên kết Đăng ký nhận focus trước nút gửi nằm phía trên nó theo bố cục trực quan.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện này chỉ phản ánh thứ tự focus Đăng nhập đã ghi nhận.

---

## 13. Bước đầu Quên mật khẩu không có điều khiển quay lại Đăng nhập

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-042
- **URL SUT / màn hình:** `http://127.0.0.1:5173/forgot-password`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — FR-03 yêu cầu có cách quay lại Đăng nhập; thiếu điều khiển này khiến người dùng không thể quay lại từ màn hình khôi phục ban đầu.
- **Bằng chứng:** [GUI-042](../../evidence/gui/GUI-042-forgot-login-return.png)

### Điều kiện tiên quyết
Mở màn hình khôi phục ban đầu.

### Các bước tái hiện
1. Kiểm tra màn hình Quên mật khẩu ban đầu để tìm điều khiển quay lại Đăng nhập.
2. Thử kích hoạt điều khiển đó.

### Kết quả GUI mong đợi
Có điều khiển hiển thị để quay lại Đăng nhập.

### Kết quả GUI thực tế
Không có điều khiển quay lại Đăng nhập hiển thị hoặc có thể kích hoạt.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
GUI-043 ở trạng thái Chưa chạy (Not Run) vì không thể kích hoạt điều khiển bị thiếu mà GUI-042 đã ghi nhận; mục này không được tính là ID Không đạt.

---

## 14. Luồng Quên mật khẩu không có chỉ báo bước

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-038, GUI-044, GUI-050
- **URL SUT / màn hình:** `http://127.0.0.1:5173/forgot-password`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — FR-03 và FR-22 yêu cầu có chỉ báo hiển thị cho luồng khôi phục gồm hai bước.
- **Bằng chứng:** [Bước đầu](../../evidence/gui/GUI-038-forgot-step-indicator.png), [Bước hai, OTP đã che](../../evidence/gui/report-redacted/GUI-044-step2-redacted.png), [Bước một sau khi quay lại](../../evidence/gui/GUI-050-forgot-return-step.png). Bản crop bước hai lấy từ ảnh do người dùng cung cấp; banner OTP và giá trị OTP đã nhập đã được che.

### Điều kiện tiên quyết
Mở bước đầu của luồng khôi phục; với GUI-044 và GUI-050, quá trình kiểm thử đã đến bước hai rồi quay lại bước một.

### Các bước tái hiện
1. Kiểm tra màn hình khôi phục ban đầu để tìm chỉ báo bước.
2. Yêu cầu OTP và kiểm tra bước hai.
3. Quay lại bước một và kiểm tra lại.

### Kết quả GUI mong đợi
Bước hiện tại được nhận diện phù hợp là bước 1/2 hoặc bước 2/2.

### Kết quả GUI thực tế
Checklist ghi nhận không có chỉ báo trên màn hình ban đầu, không có chỉ báo sau khi quay lại bước một và không có chỉ báo bước 2 hiển thị sau khi yêu cầu OTP.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem ảnh bước một và ảnh bước một sau khi quay lại được liên kết.

### Ghi chú / điểm chưa chắc chắn
Ảnh GUI-044 do người dùng cung cấp hỗ trợ quan sát ở bước hai. OTP đã được che trong bản crop của báo cáo; tệp bằng chứng gốc không bị thay đổi.

---

## 15. Hướng dẫn OTP yêu cầu bốn chữ số thay vì sáu

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-046
- **URL SUT / màn hình:** `http://127.0.0.1:5173/forgot-password` (bước đặt lại mật khẩu)
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — số chữ số OTP được hiển thị không khớp với FR-03.
- **Bằng chứng:** [Nhãn OTP đã crop](../../evidence/gui/GUI-046-forgot-otp-length.png)

### Điều kiện tiên quyết
Luồng khôi phục đã đến bước hai.

### Các bước tái hiện
1. Kiểm tra nhãn trường OTP.

### Kết quả GUI mong đợi
Hướng dẫn nêu rõ yêu cầu OTP gồm sáu chữ số.

### Kết quả GUI thực tế
Nhãn ghi “Mã OTP (4 số)”.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem ảnh nhãn đã crop được liên kết.

### Ghi chú / điểm chưa chắc chắn
Ảnh bằng chứng đã crop không chứa giá trị OTP.

---

## 16. Email khôi phục sai định dạng tạo hộp thoại trình duyệt thay vì xác thực nội tuyến

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-041
- **URL SUT / màn hình:** `http://127.0.0.1:5173/forgot-password`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — phản hồi được ghi nhận không khớp với thông báo lỗi định dạng email mong đợi phía trên nút gửi.
- **Bằng chứng:** [GUI-041](../../evidence/gui/GUI-041.png)

### Điều kiện tiên quyết
Mở màn hình Quên mật khẩu ban đầu.

### Các bước tái hiện
1. Nhập địa chỉ email sai định dạng.
2. Gửi yêu cầu OTP.
3. Quan sát cách phản hồi được hiển thị.

### Kết quả GUI mong đợi
Thông báo xác thực định dạng email hiển thị phía trên nút gửi.

### Kết quả GUI thực tế
Hộp thoại trình duyệt hiển thị “Lỗi: User not found”; không có thông báo lỗi định dạng email nội tuyến phía trên nút.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem ảnh thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Báo cáo ghi nhận giao diện phản hồi đã quan sát, không đánh giá cơ chế tra cứu tài khoản phía sau.

---

## 17. Biểu mẫu đặt lại hiển thị hộp thoại mật khẩu yếu; chưa xác minh phản hồi OTP

- **Trạng thái:** Bản nháp — đã ghi nhận hộp thoại; chưa xác minh kết quả OTP
- **ID checklist liên quan:** GUI-049
- **URL SUT / màn hình:** `http://127.0.0.1:5173/forgot-password` (bước đặt lại mật khẩu)
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — phản hồi quan sát được là hộp thoại trình duyệt thay vì thông báo nội tuyến phía trên nút gửi.
- **Bằng chứng:** [Cảnh báo độ mạnh mật khẩu GUI-049, OTP đã che](../../evidence/gui/report-redacted/GUI-049-password-alert-redacted.png). Ảnh chụp gốc được giữ nguyên.

### Điều kiện tiên quyết
Luồng khôi phục đã đến bước hai.

### Các bước tái hiện
1. Nhập OTP sai và mật khẩu không đáp ứng yêu cầu độ mạnh đang hiển thị.
2. Gửi biểu mẫu đặt lại mật khẩu.
3. Quan sát phản hồi nào được hiển thị.

### Kết quả GUI mong đợi
Thông báo xác thực hoặc phản hồi yêu cầu đặt lại hiển thị dễ đọc phía trên nút gửi.

### Kết quả GUI thực tế
Người dùng xác nhận rằng sau khi gửi OTP sai cùng mật khẩu yếu, hệ thống hiển thị hộp thoại: “Mật khẩu quá yếu!”. Không nhận được hoặc xác minh phản hồi liên quan đến OTP.

### Khả năng tái hiện
Hộp thoại được hỗ trợ bởi ảnh GUI-049 do người dùng cung cấp và xác nhận của người dùng. Chưa kiểm tra xem hệ thống có báo OTP sai khi dùng mật khẩu đủ mạnh hay không.

### Ghi chú / điểm chưa chắc chắn
Không xem đây là bằng chứng đã kiểm tra xác thực OTP sai. Quan sát chỉ giới hạn ở việc hiển thị cảnh báo mật khẩu yếu và chưa thể xác nhận phản hồi OTP trong lần gửi này.

---

## 18. Xác thực số điện thoại hồ sơ hiển thị trong hộp thoại trình duyệt

- **Trạng thái:** Bản nháp — có ảnh chụp làm bằng chứng
- **ID checklist liên quan:** GUI-059
- **URL SUT / màn hình:** `http://127.0.0.1:5173/profile`
- **Mức độ nghiêm trọng (đề xuất):** Trung bình — FR-22 yêu cầu thông báo xác thực hiển thị phía trên thao tác lưu.
- **Bằng chứng:** [Ảnh crop cảnh báo xác thực số điện thoại GUI-059](../../evidence/gui/report-redacted/GUI-059-phone-alert-crop.png), được crop từ ảnh người dùng cung cấp để loại dữ liệu hồ sơ. Ảnh gốc được giữ nguyên.

### Điều kiện tiên quyết
Người dùng thử nghiệm đã đăng nhập và đang ở `/profile`.

### Các bước tái hiện
1. Nhập số điện thoại được checklist ghi nhận là không hợp lệ.
2. Gửi biểu mẫu Hồ sơ.
3. Quan sát cách phản hồi được hiển thị.

### Kết quả GUI mong đợi
Thông báo xác thực số điện thoại dễ đọc và hiển thị phía trên nút lưu.

### Kết quả GUI thực tế
Ảnh do người dùng cung cấp cho thấy hộp thoại trình duyệt ghi “Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.” thay vì thông báo nội tuyến phía trên nút lưu.

### Khả năng tái hiện
Ảnh ghi lại hộp thoại này. Bản thân quy tắc xác thực số điện thoại không được kiểm tra trong lần cập nhật báo cáo.

### Ghi chú / điểm chưa chắc chắn
Nội dung cảnh báo đề cập 9–10 chữ số, trong khi FR-04 quy định 10–11 chữ số bắt đầu bằng 0. Báo cáo không đánh giá quy tắc nghiệp vụ số điện thoại; phát hiện này chỉ liên quan đến cách hiển thị phản hồi.

---

## 19. Thao tác đăng xuất có nhãn “Thoát” thay vì “Đăng xuất”

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-063
- **URL SUT / màn hình:** `http://127.0.0.1:5173/profile` (đã đăng nhập)
- **Mức độ nghiêm trọng (đề xuất):** Thấp — nhãn thao tác không khớp với FR-23.
- **Bằng chứng:** [GUI-063](../../evidence/gui/GUI-063-profile-logout-label.png)

### Điều kiện tiên quyết
Người dùng đã đăng nhập đang ở `/profile`.

### Các bước tái hiện
1. Kiểm tra thanh điều hướng khi đã đăng nhập.
2. Đọc nhãn thao tác đăng xuất.

### Kết quả GUI mong đợi
Thao tác có nhãn “Đăng xuất”.

### Kết quả GUI thực tế
Thao tác có nhãn “Thoát”.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện này chỉ liên quan đến nhãn thao tác hiển thị.

---

## 20. Trạng thái lịch sử đơn hàng trống không có hình minh họa

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-064
- **URL SUT / màn hình:** `http://127.0.0.1:5173/profile` (tài khoản chưa có đơn hàng)
- **Mức độ nghiêm trọng (đề xuất):** Thấp — FR-24 yêu cầu trạng thái trống có biểu tượng hoặc hình minh họa.
- **Bằng chứng:** [GUI-064](../../evidence/gui/GUI-064-profile-empty-orders.png)

### Điều kiện tiên quyết
Người dùng thử nghiệm đã đăng nhập, không có đơn hàng và đang ở `/profile`.

### Các bước tái hiện
1. Kiểm tra trạng thái lịch sử đơn hàng trống.

### Kết quả GUI mong đợi
Trạng thái trống có thông báo cùng biểu tượng hoặc hình minh họa.

### Kết quả GUI thực tế
Thông báo chưa có đơn hàng hiển thị, nhưng checklist ghi nhận không có hình ảnh hoặc minh họa SVG.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện này chỉ liên quan đến hình thức trạng thái trống; không kiểm tra hành vi đơn hàng.

---

## 21. Nút thao tác chính của Đăng ký có màu đỏ thay vì xanh dương

- **Trạng thái:** Bản nháp — cần người dùng xem xét
- **ID checklist liên quan:** GUI-066
- **URL SUT / màn hình:** `http://127.0.0.1:5173/register`
- **Mức độ nghiêm trọng (đề xuất):** Thấp — FR-21 quy định màu xanh dương cho các nút gửi mang ý nghĩa tích cực.
- **Bằng chứng:** [GUI-066](../../evidence/gui/GUI-066-registration-primary-color.png)

### Điều kiện tiên quyết
Mở Đăng ký khi nút thao tác chính đang hiển thị.

### Các bước tái hiện
1. Kiểm tra màu nút gửi ở màn hình Đăng ký.
2. So sánh với màu được quy định cho thao tác tích cực.

### Kết quả GUI mong đợi
Các thao tác gửi/lưu tích cực dùng màu xanh dương.

### Kết quả GUI thực tế
Nút Đăng ký màu đỏ (RGB ghi nhận là `239, 68, 68`); các nút trên những màn hình khác đã kiểm tra có màu xanh dương.

### Khả năng tái hiện
Không kiểm tra lại trong giai đoạn báo cáo; xem bằng chứng thực thi được liên kết.

### Ghi chú / điểm chưa chắc chắn
Phát hiện này chỉ giới hạn ở quy ước màu đã nêu.

> Các bản nháp này chưa được tạo thành GitHub Issue. Cần người dùng phê duyệt trước khi báo cáo ra bên ngoài.

# ⚡ Đồ án: Dự đoán tiêu thụ điện năng & Chi phí hàng tháng

## 📖 Tổng quan
Đồ án sử dụng thuật toán **Linear Regression** để tìm ra mối liên hệ giữa nhiệt độ thời tiết và mức độ tiêu thụ điện của hộ gia đình, từ đó đưa ra dự báo tài chính cho 3 tháng tiếp theo.

## 🛠 Cách chạy dự án
1. Clone repository: `git clone <link_cua_ban>`
2. Cài đặt thư viện: `pip install -r requirements.txt`
3. Chạy file phân tích: `python model_dudoan.py`

## 📊 Phương pháp tiếp cận
- **Dữ liệu:** Thu thập từ hóa đơn điện thực tế và dữ liệu thời tiết lịch sử.
- **Tính toán:** Áp dụng công thức tính giá điện bậc thang của EVN.
- **Đánh giá:** Sử dụng chỉ số R-squared để đo lường độ khớp của mô hình.

## 🎯 Kết quả mong đợi
Giúp người dùng chủ động hơn trong việc sử dụng thiết bị làm mát khi nhiệt độ môi trường tăng cao, tránh rơi vào các bậc điện giá cao (Bậc 5, Bậc 6).

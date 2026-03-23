# Đồ án: Dự báo Tiền điện Hộ gia đình (3 tháng tới)

## 📌 Giới thiệu
Đồ án này sử dụng các kỹ thuật Khoa học Dữ liệu để phân tích lịch sử tiêu thụ điện và dự báo chi phí tiền điện cho 3 tháng tiếp theo. Dự án giúp người dùng hiểu rõ thói quen sử dụng và tối ưu hóa chi tiêu năng lượng.

## 📊 Dữ liệu sử dụng
- **Nguồn:** Dữ liệu tiêu thụ điện theo tháng (kWh) từ năm 2021 - 2025.
- **Các thuộc tính:** Tháng, Năm, Số chữ điện (kWh), Nhiệt độ trung bình, Số ngày trong tháng.

## 🛠 Công nghệ sử dụng
- **Ngôn ngữ:** Python 3.x
- **Thư viện chính:** - `pandas`, `numpy`: Xử lý dữ liệu.
  - `matplotlib`, `seaborn`: Trực quan hóa.
  - `scikit-learn`: Xây dựng mô hình Regression.
  - `prophet`: Dự báo chuỗi thời gian (Time Series).

## 🚀 Quy trình thực hiện
1. **Tiền xử lý:** Làm sạch dữ liệu, xử lý giá trị thiếu.
2. **Feature Engineering:** Tạo các biến trễ (lag), biến mùa vụ.
3. **Huấn luyện mô hình:** So sánh giữa Linear Regression và Facebook Prophet.
4. **Tính toán chi phí:** Áp dụng biểu giá điện bậc thang của EVN để quy đổi từ kWh sang VNĐ.

## 📈 Kết quả

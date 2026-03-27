import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# Tạo thư mục outputs nếu chưa có
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# 1. Biểu giá điện sinh hoạt 6 bậc cập nhật mới nhất 2026
def calculate_electricity_bill_2026(kwh):
    # Giá chưa thuế (VNĐ/kWh) - Cập nhật 2026
    prices = [1984, 2050, 2380, 2998, 3350, 3460]
    limits = [50, 50, 100, 100, 100, float('inf')]
    
    total_bill = 0
    remaining_kwh = kwh
    for i in range(len(prices)):
        if remaining_kwh <= 0: break
        usage = min(remaining_kwh, limits[i])
        total_bill += usage * prices[i]
        remaining_kwh -= usage
        
    return total_bill * 1.08 # Thuế VAT 8%

# 2. Xử lý dữ liệu
# Lưu ý: Đảm bảo file 'electricity_usage.csv' có các cột 'kWh' và 'Avg_Temp'
df = pd.read_csv('electricity_usage.csv')
df['Month_Index'] = range(len(df))

# 3. Huấn luyện mô hình
# X là các biến độc lập (Feature names: Month_Index, Avg_Temp)
X = df[['Month_Index', 'Avg_Temp']]
y = df['kWh']
model = LinearRegression()
model.fit(X, y)

# 4. Dự báo cho quý 2 năm 2026 (Tháng 4, 5, 6)
# FIX: Sử dụng DataFrame thay vì np.array để giữ tên cột, tránh lỗi UserWarning
future_data = pd.DataFrame({
    'Month_Index': [15, 16, 17],
    'Avg_Temp': [32, 35, 37]
})

predictions = model.predict(future_data)

# In kết quả ra màn hình
print("-" * 45)
print(f"{'THÁNG DỰ BÁO (2026)':<20} | {'SỐ ĐIỆN':<10} | {'TIỀN ĐIỆN'}")
print("-" * 45)

for i, kwh in enumerate(predictions):
    month_name = f"Tháng {i+4}/2026"
    cost = calculate_electricity_bill_2026(kwh)
    print(f"{month_name:<20} | {kwh:>7.1f} kWh | {cost:,.0f} VNĐ")

# 5. Vẽ biểu đồ lưu vào outputs/
plt.figure(figsize=(10, 5))
plt.plot(df['Month_Index'], df['kWh'], 'b-o', label='Dữ liệu 2025-2026')
plt.plot(future_data['Month_Index'], predictions, 'r--s', label='Dự báo Hè 2026')
plt.title('Dự báo tiêu thụ điện năng Hộ gia đình Q2/2026')
plt.xlabel('Chỉ số tháng (từ tháng 1/2025)')
plt.ylabel('kWh')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('outputs/forecast_2026.png')
print("\n[OK] Đã xuất biểu đồ dự báo năm 2026 tại outputs/forecast_2026.png!")

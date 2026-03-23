import pandas as pd
import numpy as np

# 1. Hàm tính tiền điện theo bậc thang EVN (Giá giả định 2024)
def tinh_tien_dien(kwh):
    bac = [
        (50, 1806),   # Bậc 1: 0-50 kWh
        (50, 1866),   # Bậc 2: 51-100 kWh
        (100, 2167),  # Bậc 3: 101-200 kWh
        (100, 2729),  # Bậc 4: 201-300 kWh
        (100, 3050),  # Bậc 5: 301-400 kWh
        (float('inf'), 3151) # Bậc 6: 401 kWh trở lên
    ]
    
    tong_tien = 0
    con_lai = kwh
    
    for gioi_han, gia in bac:
        if con_lai <= 0:
            break
        dung = min(con_lai, gioi_han)
        tong_tien += dung * gia
        con_lai -= dung
        
    # Cộng thêm 8% thuế VAT (giả định)
    return tong_tien * 1.08

# 2. Giả lập dữ liệu dự báo (Ví dụ kết quả từ mô hình của bạn)
# Giả sử mô hình dự báo 3 tháng tới tiêu thụ lần lượt: 250kWh, 310kWh, 400kWh
forecast_kwh = [250, 310, 400]
months = ['Tháng 4', 'Tháng 5', 'Tháng 6']

print("--- KẾT QUẢ DỰ BÁO CHI PHÍ TIỀN ĐIỆN ---")
for month, kwh in zip(months, forecast_kwh):
    chi_phi = tinh_tien_dien(kwh)
    print(f"{month}: Dự báo tiêu thụ {kwh} kWh -> Thành tiền: {chi_phi:,.0f} VNĐ")

# 3. Gợi ý hướng làm mô hình dự báo với thư viện Prophet
"""
from prophet import Prophet
df_train = data[['ds', 'y']] # ds: thời gian, y: số kWh
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=3, freq='M')
forecast = m.predict(future)
"""

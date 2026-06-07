import pandas as pd
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

CSV_URL = os.getenv("CSV_URL")

def chuan_hoa_gio(chuoi_gio):
    """Hàm phụ trợ: Thêm số 0 vào trước giờ (vd: 5:40 -> 05:40) để khớp với hệ thống"""
    chuoi = str(chuoi_gio).strip()
    if len(chuoi) == 4 and chuoi[1] == ':':
        return '0' + chuoi
    return chuoi

def lay_cong_viec_hien_tai():
    """Đọc CSV, đối chiếu giờ hệ thống và trả về danh sách việc cần làm"""
    try:
        df = pd.read_csv(CSV_URL)
        
        # 1. Chuẩn hóa dữ liệu Ngày và Khung giờ
        df['Ngày'] = df['Ngày'].astype(str).str.strip()
        df['Khung giờ'] = df['Khung giờ'].apply(chuan_hoa_gio)
        
        # LẤY MÚI GIỜ VIỆT NAM (UTC+7)
        mui_gio_vn = timezone(timedelta(hours=7))
        now = datetime.now(mui_gio_vn)
        
        # Dịch ngày hệ thống sang định dạng Excel của bạn
        day_map = {
            "Monday": "Thứ 2", "Tuesday": "Thứ 3", "Wednesday": "Thứ 4",
            "Thursday": "Thứ 5", "Friday": "Thứ 6", "Saturday": "Thứ 7", "Sunday": "Chủ Nhật"
        }
        ngay_hom_nay = day_map[now.strftime("%A")]
        gio_hien_tai = now.strftime("%H:%M") 
        
        print(f"🕒 Đang quét lịch: {ngay_hom_nay} - {gio_hien_tai}")
        
        # 2. Lọc các dòng khớp cả Ngày và Khung giờ
        cong_viec_den_han = df[(df['Ngày'] == ngay_hom_nay) & (df['Khung giờ'] == gio_hien_tai)]
        
        danh_sach_tin_nhan = []
        for index, row in cong_viec_den_han.iterrows():
            # Thay đổi dấu * thành thẻ <b> </b>
            tin_nhan = f"🔔 <b>BÁO THỨC LỊCH TRÌNH!</b>\n\n"
            
            hoat_dong = row.get('Hoạt động & Chi tiết trọng tâm', 'Không có nội dung')
            tin_nhan += f"🎯 <b>Hoạt động:</b> {hoat_dong}\n\n"
            
            if 'Link' in df.columns and pd.notna(row['Link']):
                tin_nhan += f"🔗 <b>Tài liệu/Link:</b> {row['Link']}"
                
            danh_sach_tin_nhan.append(tin_nhan)
            
        return danh_sach_tin_nhan
        
    except Exception as e:
        print(f"❌ Lỗi đọc dữ liệu CSV: {e}")
        return []
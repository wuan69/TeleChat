import time
from sheets_handler import lay_cong_viec_hien_tai
from telegram_bot import gui_tin_nhan

def kiem_tra_va_thong_bao():
    """Hàm trung tâm: Lấy việc và gửi đi"""
    print("🕒 Bắt đầu quét lịch từ Google Sheets...")
    cac_viec_can_lam = lay_cong_viec_hien_tai()
    
    if cac_viec_can_lam:
        for viec in cac_viec_can_lam:
            gui_tin_nhan(viec)
            # Dừng 1 giây giữa các tin nhắn để tránh bị Telegram chặn vì spam
            time.sleep(1)
        print("✅ Đã xử lý xong các tác vụ của phút này.")
    else:
        print("Trống lịch, không có việc nào.")

if __name__ == "__main__":
    # Bỏ hoàn toàn thư viện schedule, chỉ cần gọi thẳng hàm này 1 lần duy nhất
    kiem_tra_va_thong_bao()
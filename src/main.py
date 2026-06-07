import time
import schedule
from sheets_handler import lay_cong_viec_hien_tai
from telegram_bot import gui_tin_nhan

def kiem_tra_va_thong_bao():
    """Hàm trung tâm: Lấy việc và gửi đi"""
    cac_viec_can_lam = lay_cong_viec_hien_tai()
    
    if cac_viec_can_lam:
        for viec in cac_viec_can_lam:
            gui_tin_nhan(viec)
            # Dừng 1 giây giữa các tin nhắn để tránh bị Telegram chặn vì spam
            time.sleep(1)

# Lên lịch cho bot chạy hàm kiem_tra_va_thong_bao vào đầu mỗi phút (Giây thứ 00)
schedule.every().minute.at(":00").do(kiem_tra_va_thong_bao)

if __name__ == "__main__":
    print("🚀 Hệ thống Bot Nhắc Việc đang chạy. Nhấn Ctrl+C để dừng.")
    
    # Chạy vòng lặp vô tận để duy trì chương trình
    while True:
        schedule.run_pending()
        time.sleep(1)
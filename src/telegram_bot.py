import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def gui_tin_nhan(noi_dung):
    """Hàm gửi tin nhắn qua Telegram Bot"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Gửi dạng văn bản thuần túy, bỏ dòng parse_mode
    payload = {
        "chat_id": CHAT_ID,
        "text": noi_dung,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, json=payload)
        
        # Bắt lỗi chi tiết để dễ sửa nếu còn sai
        if response.status_code != 200:
            print(f"❌ Chi tiết lỗi từ Telegram: {response.text}")
            
        response.raise_for_status()
        print(f"✅ Đã gửi thông báo Telegram!")
    except Exception as e:
        print(f"❌ Lỗi khi gửi Telegram: {e}")
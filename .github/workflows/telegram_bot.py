import requests
import os
from datetime import datetime

def send_to_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": message, 
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
    try:
        response = requests.post(url, json=payload )
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

def post_best_keys():
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Token or Chat ID not found.")
        return

    try:
        with open("best_keys.txt", "r") as f:
            keys = f.readlines()
        
        if not keys:
            print("No keys to post.")
            return

        # ယနေ့ရက်စွဲ
        today = datetime.now().strftime("%d/%m/%Y")
        
        # Message Template (သင့်ပုံထဲကအတိုင်း ပြင်ဆင်ထားသည်)
        message = "🌟 *MM Free VPN Hub* 🌟\n"
        message += "🌍 *GLOBAL FAST NODES* 🌍\n"
        message += "⚡️ REALITY NODES ⚡️\n"
        message += "🔐 REALITY SECURITY\n"
        message += "🚀 XTLS VISION\n"
        message += "🌍 STABLE CONNECTION\n"
        message += "───────────────────\n\n"

        for i, key in enumerate(keys[:2]): # Node ၂ ခုပဲ တင်ပြရန်
            node_no = i + 1
            message += f"📦 *NODE 0{node_no}*\n"
            message += f"```\n{key.strip()}\n```\n"
            message += "───────────────────\n"

        message += "\n📥 *SUPPORTED APPS*\n"
        message += "✅ V2Box\n"
        message += "✅ V2RayNG\n"
        message += "✅ Nekobox\n\n"
        message += f"#VPN #Reality #VLESS #Update_{today}"

        result = send_to_telegram(BOT_TOKEN, CHAT_ID, message)
        print(f"Telegram response: {result}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_best_keys()

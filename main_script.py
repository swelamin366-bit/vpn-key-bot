import requests
import re
import base64
import json
import time
import os
import concurrent.futures

SOURCES = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/trojan.txt"
]

def decode_base64(data):
    try:
        missing_padding = len(data) % 4
        if missing_padding:
            data += '=' * (4 - missing_padding)
        return base64.b64decode(data).decode('utf-8')
    except:
        return ""

def get_host(config_url):
    try:
        if config_url.startswith("vmess://"):
            content = decode_base64(config_url[8:])
            data = json.loads(content)
            return data.get("add")
        elif "@" in config_url:
            return config_url.split("@")[1].split(":")[0].split("?")[0]
    except:
        pass
    return None

def check_latency(config_url):
    """ GitHub တွင် Ping ပိတ်ထားပါက အလုပ်လုပ်စေရန် requests timeout ဖြင့် လိုင်းမြန်နှုန်း စစ်ဆေးခြင်း """
    host = get_host(config_url)
    if not host:
        return config_url, 9999
    try:
        # HTTP တောင်းဆိုမှု ကြာချိန်ဖြင့် Latency စစ်ဆေးခြင်း (GitHub ပေါ်တွင် ပိုမိုစိတ်ချရသည်)
        start_time = time.time()
        resp = requests.get(f"http://{host}", timeout=1.5)
        latency = (time.time() - start_time) * 1000
        return config_url, latency
    except:
        # HTTP တိုက်ရိုက်မရပါက နောက်တစ်နည်းဖြင့် စမ်းသပ်ခြင်း
        try:
            start_time = time.time()
            requests.head(f"https://{host}", timeout=1.5)
            latency = (time.time() - start_time) * 1000
            return config_url, latency
        except:
            return config_url, 9999

def run():
    print("Scraping keys...")
    all_keys = []
    for url in SOURCES:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                keys = re.findall(r'(?:vmess|vless|ss|trojan)://[^\s\'"<>]+', resp.text)
                all_keys.extend(keys)
        except:
            continue
            
    unique_keys = list(set(all_keys))
    print(f"Found {len(unique_keys)} unique keys. Testing latency...")
    
    # ပထမဆုံး သော့ချက် အခု ၆၀ ကို စမ်းသပ်မည်
    sample_keys = unique_keys[:60]
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        results = list(executor.map(check_latency, sample_keys))
        
    results = [r for r in results if r[1] < 2000]
    results.sort(key=lambda x: x[1])
    
    # အကောင်းဆုံး ၅ ခုကို ရွေးထုတ်ခြင်း
    top_5_keys = results[:5]
    
    if not top_5_keys:
        print("လိုင်းကောင်းသော VPN Key မတွေ့ရှိပါ။")
        return

    # Telegram သို့ ပို့ရန် စာသား ပုံစံပြင်ဆင်ခြင်း
    today = time.strftime("%Y-%m-%d")
    template = f"🚀 <b>FREE VPN KEYS UPDATE</b> | {today} 🚀\n"
    template += "=========================\n\n"
    
    for i, (key, lat) in enumerate(top_5_keys, 1):
        template += f"🔑 <b>NODE {i:02d}</b> (Latency: {int(lat)}ms)\n"
        template += f"<code>{key}</code>\n\n"
        
    template += "=========================\n"
    template += "📱 SUPPORTED APPS\n"
    template += "✓ v2rayNG  ✓ V2Box  ✓ Nekobox\n\n"
    template += "#V2ray #Vless #Vmess #FreeVPN"

    # ဖိုင်ထဲသို့ သိမ်းဆည်းခြင်း
    with open("best_keys.txt", "w", encoding="utf-8") as f:
        for key, lat in top_5_keys:
            f.write(key + "\n")
    print("VPN keys formatted and saved.")

    # Telegram သို့ လှမ်းပို့သည့်အပိုင်း
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if token and chat_id:
        telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": template,
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(telegram_url, json=payload)
            if response.ok:
                print("Telegram channel သို့ အကောင်းဆုံး Keys များ ပို့ပြီးပါပြီ!")
            else:
                print(f"Telegram Error: {response.text}")
        except Exception as e:
            print(f"Error sending to Telegram: {e}")
    else:
        print("Error: Telegram Credentials များကို မတွေ့ပါ။")

if __name__ == "__main__":
    run()

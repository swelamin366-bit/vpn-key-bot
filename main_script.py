import datetime

def get_vpn_keys():
    # ဒီနေ့ရက်စွဲကို ယူပါမယ်
    today = datetime.datetime.now().strftime("%d %b %Y")
    
    # စာသားတွေကို ပုံစံချပါမယ် (လုံခြုံစိတ်ချရအောင် format ပြန်လုပ်ထားပါတယ်)
    template = f"🚀 FREE VLESS KEYS | {today} 🚀\n"
    template += "╔════════════════════╗\n"
    template += "🇬🇪 GEORGIA VLESS🇬🇪\n"
    template += "⚡️ TODAY UPDATE ⚡️\n"
    template += "╚════════════════════╝\n"
    template += "🔐 TLS SECURED\n"
    template += "🚀 DAILY UPDATED\n"
    template += "🌍 STABLE CONNECTION\n"
    template += "━━━━━━━━━━━━━━━━━━\n"
    template += "📦 NODE 01\n"
    template += "vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=edge&insecure=0&allowInsecure=0&type=tcp&headerType=none\n\n"
    template += "📦 NODE 02\n"
    template += "vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=edge&insecure=0&allowInsecure=0&type=tcp&headerType=none\n\n"
    template += "📦 NODE 03\n"
    template += "vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision&security=tls&insecure=0&allowInsecure=0&type=tcp&headerType=none\n\n"
    template += "📦 NODE 04\n"
    template += "vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=chrome&insecure=0&allowInsecure=0&type=tcp&headerType=none\n\n"
    template += "📦 NODE 05\n"
    template += "vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=edge&insecure=0&allowInsecure=0&type=tcp&headerType=none\n\n"
    template += "📦 NODE 06\n"
    template += "vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=chrome&insecure=0&allowInsecure=0&type=tcp&headerType=none\n"
    template += "━━━━━━━━━━━━━━━━━━\n"
    template += "📥 SUPPORTED APPS\n"
    template += "✅ V2Box\n"
    template += "✅ V2RayNG\n"
    template += "✅ Nekobox\n"
    template += "⚠️ Free Nodes May Expire Anytime\n"
    template += "#Georgia #VLESS #VPN #TodayUpdate"

    with open("keys.txt", "w", encoding="utf-8") as f:
        f.write(template)
    print("VPN keys formatted and saved.")

if __name__ == "__main__":
    get_vpn_keys()

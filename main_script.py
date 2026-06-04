import datetime

def get_vpn_keys():
    # ဒီနေ့ရက်စွဲကို ယူပါမယ်
    today = datetime.datetime.now().strftime("%d %b %Y")
    
    # သင်ပေးထားတဲ့ Template အတိုင်း ပုံစံချပါမယ်
    template = f"""🚀 FREE VLESS KEYS | {today} 🚀
╔════════════════════╗
🇬🇪 GEORGIA VLESS🇬🇪
⚡️ TODAY UPDATE ⚡️
╚════════════════════╝
🔐 TLS SECURED
🚀 DAILY UPDATED
🌍 STABLE CONNECTION
━━━━━━━━━━━━━━━━━━
📦 NODE 01
vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=edge&insecure=0&allowInsecure=0&type=tcp&headerType=none

📦 NODE 02
vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=edge&insecure=0&allowInsecure=0&type=tcp&headerType=none

📦 NODE 03
vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision&security=tls&insecure=0&allowInsecure=0&type=tcp&headerType=none

📦 NODE 04
vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=chrome&insecure=0&allowInsecure=0&type=tcp&headerType=none

📦 NODE 05
vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=edge&insecure=0&allowInsecure=0&type=tcp&headerType=none

📦 NODE 06
vless://afcac633-0e1a-46c3-bef2-cc01cc0097c8@r1.mizulina.top:22231?encryption=none&flow=xtls-rprx-vision-udp443&security=tls&sni=r1.mizulina.top&fp=chrome&insecure=0&allowInsecure=0&type=tcp&headerType=none
━━━━━━━━━━━━━━━━━━
📥 SUPPORTED APPS
✅ V2Box
✅ V2RayNG
✅ Nekobox
⚠️ Free Nodes May Expire Anytime
#Georgia #VLESS #VPN #TodayUpdate"""

    with open("keys.txt", "w", encoding="utf-8") as f:
        f.write(template)
    print("VPN keys formatted and saved.")

if __name__ == "__main__":
    get_vpn_keys()

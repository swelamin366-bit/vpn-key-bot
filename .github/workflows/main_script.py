import requests
import re
import base64
import json
import subprocess
import time
import concurrent.futures

SOURCES = [
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/trojan.txt"
]

def decode_base64(data ):
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
    host = get_host(config_url)
    if not host:
        return config_url, 9999
    try:
        cmd = ["ping", "-c", "2", "-W", "1", host]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        match = re.search(r"avg/max/mdev = (\d+\.\d+)/", output)
        if match:
            return config_url, float(match.group(1))
    except:
        pass
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
    sample_keys = unique_keys[:100]
    best_keys = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(check_latency, sample_keys))
    results = [r for r in results if r[1] < 1000]
    results.sort(key=lambda x: x[1])
    with open("best_keys.txt", "w") as f:
        for key, lat in results[:5]:
            f.write(key + "\n")

if __name__ == "__main__":
    run()

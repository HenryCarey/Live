import requests, re, os

channels = {
    "channel1.m3u8": "https://iapp.zcsrmtzx.cn/share/dHZsLTE4MS0x.html",
    "channel2.m3u8": "https://iapp.zcsrmtzx.cn/share/dHZsLTE4MS00.html"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://iapp.zcsrmtzx.cn/"
}

os.makedirs("m3u", exist_ok=True)

for filename, url in channels.items():
    resp = requests.get(url, headers=headers)
    match = re.search(r'https://[^\'"]+\.m3u8', resp.text)
    if match:
        m3u8_url = match.group(0)
        print(f"抓取到 {filename} 地址: {m3u8_url}")
        m3u8_resp = requests.get(m3u8_url, headers=headers)
        if m3u8_resp.status_code == 200 and m3u8_resp.text.strip():
            with open(os.path.join("m3u", filename), "w", encoding="utf-8") as f:
                f.write(m3u8_resp.text)
        else:
            print(f"⚠️ 下载 {filename} 内容失败，返回码 {m3u8_resp.status_code}")

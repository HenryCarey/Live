import requests, re, os

channels = {
    "channel1.m3u8": "https://iapp.zcsrmtzx.cn/share/dHZsLTE4MS0x.html",
    "channel2.m3u8": "https://iapp.zcsrmtzx.cn/share/dHZsLTE4MS00.html"
}

headers = {"User-Agent": "Mozilla/5.0"}
os.makedirs("m3u", exist_ok=True)

for filename, url in channels.items():
    resp = requests.get(url, headers=headers)
    match = re.search(r'https://[^\'"]+\.m3u8', resp.text)
    if match:
        m3u8_url = match.group(0)
        # 下载完整 m3u8 文件内容
        m3u8_resp = requests.get(m3u8_url, headers=headers)
        with open(os.path.join("m3u", filename), "w", encoding="utf-8") as f:
            f.write(m3u8_resp.text)

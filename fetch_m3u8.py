import requests, re, os

channels = {
    "channel1.m3u8": "https://iapp.zcsrmtzx.cn/share/dHZsLTE4MS0x.html",
    "channel2.m3u8": "https://iapp.zcsrmtzx.cn/share/dHZsLTE4MS00.html"
}

headers = {"User-Agent": "Mozilla/5.0"}

# 确保 m3u 文件夹存在
os.makedirs("m3u", exist_ok=True)

for filename, url in channels.items():
    resp = requests.get(url, headers=headers)
    match = re.search(r'https://[^\'"]+\.m3u8', resp.text)
    if match:
        m3u8_url = match.group(0)
        with open(os.path.join("m3u", filename), "w") as f:
            f.write("#EXTM3U\n")
            f.write(m3u8_url + "\n")

# pip install speedtest-cli

import speedtest
s = speedtest.Speedtest()

print("Testing...\n")

DownloadSpeed = s.download() / 1048576
UploadSpeed = s.upload() / 1048576
PingResult = round(s.result.ping)

print(f"Download Speed: {downloadSpeed: 2f} Mbps")
print(f"Upload Speed: {uploadSpeed: 2f} Mbps")
print(f"Ping: {pingResult} ms")
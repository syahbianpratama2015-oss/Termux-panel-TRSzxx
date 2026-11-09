import os
url = input("Link YouTube: ")
os.system("pip install yt-dlp > /dev/null")
os.system(f"yt-dlp {url}")

import os
domain = input("Domain (misal google.com): ")
os.system(f"pkg install dnsutils -y > /dev/null; nslookup {domain}")

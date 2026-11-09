import os
target = input("Domain/IP: ")
os.system(f"pkg install traceroute -y > /dev/null; traceroute {target}")

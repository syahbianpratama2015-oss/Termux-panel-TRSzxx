import time
import sys
import random

chars = "01@#$)(/?+!*_&~£¢^€°%"

try:
    while True:
        chaos = "".join(random.choice(chars) for _ in range(10))
        # Naik 1 baris, hapus baris, print teks baru
        sys.stdout.write(f"\033[F\033[K\033[1;32m╭─[TRSzxx]─[{chaos}]─[{time.strftime('%H:%M:%S')}]\n")
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()

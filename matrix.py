import random, time, os, sys
try:
    while True:
        print("".join(random.choice("01") for _ in range(40)))
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

import datetime, time
try:
    while True:
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    pass

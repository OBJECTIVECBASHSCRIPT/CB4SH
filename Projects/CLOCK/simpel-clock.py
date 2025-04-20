def clock():
    t = __import__('time')
    while True:
        current = t.localtime()
        h = str(current.tm_hour).zfill(2)
        m = str(current.tm_min).zfill(2)
        s = str(current.tm_sec).zfill(2)
        print(f"{h}:{m}:{s}", end='\r')
        t.sleep(1)

clock()

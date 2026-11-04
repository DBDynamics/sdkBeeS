import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 1

for i in range(100):
    time.sleep(0.1)
    ret = m.getActualPosition(mid)
    print(ret)

m.stop()

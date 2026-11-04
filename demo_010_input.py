import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0

for i in range(100):
    time.sleep(0.1)
    ret = m.getInputIO(mid)
    print(ret)

m.stop()

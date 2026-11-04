import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0

m.scanDevices()

for loop in range(0, 100):
    time.sleep(0.1)
    print(m._error_axis_num)

m.stop()

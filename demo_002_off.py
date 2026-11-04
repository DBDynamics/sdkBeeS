import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0
# 默认失能 失能后 释放电机
m.setPowerOff(mid)

m.stop()

import random
import time

from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 1
m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)
m.setAccTime(mid, 500)
m.setTargetVelocity(mid, 4000)
# m.setKPP(mid, 40)

k = 51200 / 40.0
for loop in range(0, 3000):
    m.setTargetPosition(mid, -51200*8)
    m.waitTargetPositionReached(mid)

    m.setTargetPosition(mid, -51200*0.2)
    m.waitTargetPositionReached(mid)

m.stop()

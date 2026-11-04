import random
import time

from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
for mid in range(0, 2):
    m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=1)
    # m.setKFF(mid, 10)
    # m.setKVF(mid, 10)
    m.setAccTime(mid, 500)
    m.setTargetVelocity(mid, 3000)

for loop in range(0, 3000):
    for mid in range(0, 2):
        m.setTargetPosition(mid, -51200 * 8)
    for mid in range(0, 2):
        m.waitTargetPositionReached(mid)

    for mid in range(0, 2):
        m.setTargetPosition(mid, -51200 * 0.2)
    for mid in range(0, 2):
        m.waitTargetPositionReached(mid)

m.stop()

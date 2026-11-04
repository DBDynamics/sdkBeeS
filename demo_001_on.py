import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
mid = 0
# 默认使能 软件限位无效 传感器限位生效 报警释放电机
m.setPowerOn(mid)

# 高级使能
# 软件限位 无效-0 有效-1
# 传感器限位 生效-0 无效-1
# 报警 释放电机-0 自动恢复-1
m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)

m.stop()

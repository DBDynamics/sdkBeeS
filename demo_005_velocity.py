import time
from DBDynamics import BeeS

m = BeeS('/dev/ttyUSB0')
# 这里设置成当前要控制的ID号
mid = 0

# 高级使能
# 软件限位 无效-0 有效-1
# 传感器限位 生效-0 无效-1
# 报警 释放电机-0 自动恢复-1
m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)


# 设置最大运行速度
m.setTargetVelocity(mid, -100)

# 设置加减速时间 单位ms
m.setAccTime(mid, 500)

# 设置成平滑速度模式
m.setVelocityMode(mid)

m.stop()

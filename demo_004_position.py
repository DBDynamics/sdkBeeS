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

# 设置为平滑位置模式
m.setPositionMode(mid)

# 设置最大运行速度
m.setTargetVelocity(mid, 2000)

# 设置加减速时间 单位ms
m.setAccTime(mid, 500)

# 循环
for loop in range(0, 3):
    # 设置目标位置
    m.setTargetPosition(mid, 51200)
    # 等待到位
    m.waitTargetPositionReached(mid)

    # 设置目标位置
    m.setTargetPosition(mid, 0)
    # 等待目标到位
    m.waitTargetPositionReached(mid)

m.stop()

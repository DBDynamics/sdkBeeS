import time
from DBDynamics import BeeS

# 打开端口
m = BeeS('/dev/ttyUSB0')

# 指定ID号
mid = 0

# 设置软件限位 正限位
m.setLimitPositionP(mid, 51200*2)

# 设置软件限位 负限位
m.setLimitPositionN(mid, 5120)

# 软件限位有效
m.setPowerOnPro(id=mid, limit_soft=1, limit_off=0, auto_recovery=0)

# 设置为平滑位置模式
m.setPositionMode(mid)

# 设置最大运行速度
m.setTargetVelocity(mid, 1000)

# 设置加减速时间
m.setAccTime(mid, 500)

print("start testing")

for loop in range(3):
    # 设置一个大于软件限位的位置
    tp = 51200*3
    m.setTargetPosition(mid, tp)
    print("目标位置:", tp)
    # 等待到位
    m.waitTargetPositionReached(mid)
    # 读取当前位置
    ret = m.getActualPosition(mid)
    print("当前位置:", ret)

    # 设置一个小于软件限位的位置
    tp = 51200*0
    m.setTargetPosition(mid, tp)
    print("目标位置:", tp)
    # 等待到位
    m.waitTargetPositionReached(mid)
    # 读取当前位置
    ret = m.getActualPosition(mid)
    print("当前位置:", ret)

    # 设置一个不超过软件限位的位置
    tp = 51200*1
    m.setTargetPosition(mid, tp)
    print("目标位置:", tp)
    # 等待到位
    m.waitTargetPositionReached(mid)
    # 读取当前位置
    ret = m.getActualPosition(mid)
    print("当前位置:", ret)


# 结束后台进程 释放端口
m.stop()

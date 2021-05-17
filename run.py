from controll.controll_origin import Axis_Num
from controll.encapsulation import Encapsulation

base = Encapsulation()
num1 = Axis_Num.Axis_NO_1.value
num2 = Axis_Num.Axis_NO_2.value
# 上电
base.power_on()
# 1,2轴限位传感器设置
print('--------')
base.set_Board_Mode(num1)
print('--------')
# base.set_Board_Mode(num2)
# 运动
base.reset_pos(num1)
# 默认mode=0,为梯形加减速模式
base.set_s_curve(num1)
# set_profile(num1, 10000, 50000, 80000, 80000)默认
# base.set_profile(num=num1)
base.set_profile(num1, 10000, 50000, 80000, 80000)
base.fast_pmove(num1, 1000)


# 下电
# base.power_off()

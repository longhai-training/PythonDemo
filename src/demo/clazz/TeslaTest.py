# from 全类名 import 类名
from demo.clazz.CarTest import ElectricCar
# 赋值
my_new_car = ElectricCar('Tesla', 'Modle S', 2020)
print(my_new_car.get_descriptive_name())
print(my_new_car.charge_battery())

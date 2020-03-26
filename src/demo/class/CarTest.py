class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    # 返回整洁的描述性信息
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 继承Car类,电动汽车的独特之处
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 子类自定义属性
        self.battery_size = 70
    # 重写父类方法
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(self.battery_size)
        return long_name.title()
    # 子类自定义方法
    def charge_battery(self):
        return ('Your '+ self.model + ' is charging')

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
print(my_tesla.charge_battery())






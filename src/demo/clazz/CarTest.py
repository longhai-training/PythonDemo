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
print('--------------------------')

# 继承Car类,电动汽车的独特之处
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 子类自定义属性
        self.date = '2020-01-01'
        self.battery = Battery('Dening',180,'90%')
    # 重写父类方法
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + self.date
        return long_name.title()
    # 子类自定义方法
    def charge_battery(self):
        return ('Your '+ self.model + ' is charging')



# 一次模拟电动汽车电瓶的简单尝试
class Battery():
    def __init__(self, battery_brand,battery_size,battery_remain):
        self.battery_brand = battery_brand
        self.battery_size = battery_size
        self.battery_remain = battery_remain
    def get_descriptive_battery(self):
        return self.battery_brand+' '+str(self.battery_size) +' '+ self.battery_remain

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
print(my_tesla.charge_battery())
print(my_tesla.battery.get_descriptive_battery())



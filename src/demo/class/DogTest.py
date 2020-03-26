#  一次模拟小狗的简单尝试
class Dog():
    #  初始化属性name和age
    def __init__(self, name, age): #开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突
        self.name = name
        self.age = age
    # """模拟小狗被命令时蹲下"""
    def sit(self):
        print(self.name.title() + " is now sitting.")
    # """模拟小狗被命令时打滚"""
    def roll_over(self):
        print(self.name.title() + " rolled over!")

myDog = Dog('Fifi',3)
myDog.sit()
myDog.roll_over()
print("My dog's name is " + myDog.name.title() + ".")
print("My dog is " + str(myDog.age) + " years old.")
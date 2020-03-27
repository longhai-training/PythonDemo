def greet_user(uname):
    print("Hello "+uname)

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 函数显示宠物的信息
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 函数显示宠物的信息 设置默认值为pet_name='willie'; 这种参数声明必须是无默认值跟在有默认值前面
def describe_pet( animal_type,pet_name='willie'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 调用函数
greet_user("young man")
# 传入参数调用函数
describe_pet('hamster', 'harry')
# 位置实参,有序实参方式
describe_pet('hamster', 'harry')
# 关键字实参,无序实参方式
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
# 默认值pet_name='willie'生效
describe_pet(animal_type='dog')

# 函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

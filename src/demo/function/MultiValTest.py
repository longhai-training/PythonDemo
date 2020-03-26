# 打印顾客点的所有配料
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# 传递任意熟练实参;形参名*toppings 中的星号让Python创建一个名为toppings 的空元组,并将收到的所有值都封装到这个元组中
print('--------------任意数量实参----------------')
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 概述要制作的比萨
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
# 结合使用位置实参和任意数量实参
print('--------------结合使用位置实参和任意数量实参----------------')
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
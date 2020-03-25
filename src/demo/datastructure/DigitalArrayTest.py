# 函数range() 让你能够轻松地生成一系列的数字
for value in range(1,5):
    print(value) #函数range() 让Python从你指定的第一个值开始数，并在到达你指定的第二个值 后停止，因此输出不包含第二个值

# 可使用函数list() 将range() 的结果直接转换为列表
numbers = list(range(1,6))
print(numbers)

# 切片：你还可以处理列表的部分元素——Python称之为切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])# 由于没有指定起始索引，Python从列表开头开始提取

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
friend_foods.sort()
for food in friend_foods:
    print(food.title())

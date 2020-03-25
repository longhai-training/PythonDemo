#遍历整个表,for循环,避免缩进错误，或者丢失冒号
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 函数title()如果你不小心遗漏了冒号，将导致语法错误，因为Python不知道你意欲何为
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

# 在代码行for magician in magicians 后面，每个缩进的代码行都是循环的一部分
# 且将针对列表中的每个值都执行一次。因此，可对列表中的每个值执行任意次数的操作。
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")# 认定了你再走
print("Thank you, everyone. That was a great magic show!")




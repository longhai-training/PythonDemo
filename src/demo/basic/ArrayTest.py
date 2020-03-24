# 定义列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)

# 打印列表和修改/添加/删除
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 修改
motorcycles[0] = 'ducati'
print(motorcycles)
# 添加
    # 方法append() 让动态地创建列表易如反掌，
motorcycles.append('ducati')
print(motorcycles)
    # 方法insert() 在索引0 处添加空间，并将值'ducati' 存储到这个地方。这种操作将列表中既有的每个元素都右 移一个位置
motorcycles.insert(0, 'ducati')
print(motorcycles)
# 删除
    # 使用del 可删除任何位置处的列表元素，条件是知道其索引。
del motorcycles[0]
print(motorcycles)
    # 方法pop() 可删除列表末尾的元素，并让你能够接着使用它。
    # 列表末尾的值'suzuki' 已删除，它现在存储在变量popped_motorcycle 中
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
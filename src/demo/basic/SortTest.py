# 函数sort()对列表元素排列顺序的修改是永久性的
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排 列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#要反转列表元素的排列顺序，可使用方法reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#确定队列长度。数组越界错误：IndexError: list index out of rang
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

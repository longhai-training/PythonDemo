# Python将不能修改的值称为不不可可变变的的 ，而不可变的列表被称为元元组组
# 列表非常适合用于存储在程序运行期间可能变化的数据集，列表是可以修改的，元组不可修改；
dimensions = (200, 50)
#遍历
print(dimensions[0])
print(dimensions[1])
#遍历
for v in dimensions:
    print(v)
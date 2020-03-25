# 字典
alien = {'color': 'green', 'points': 5 , 'line' : "bond"}
print(alien["line"])
print(alien)

# 新增键值对
alien['name'] = 'longhai'
print(alien)

# 更新键值对，直接取出键位重新赋值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 删除一组键值对,删除的键—值对永远消失了
del alien_0['points']
print(alien_0)

#
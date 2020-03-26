# 返回简单值
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name('lizee','defa','dfas')
print(name)

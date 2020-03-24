# 修改其中的单词的大小写,title() 以首字母大写的方式显示每个单词
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 合并（（拼接））字符串,Python使用加号（+ ）来合并字符串。
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# 要在字符串中添加制表符，可使用字符组合\t;换行符，可使用字符组合\n;字符串"\n\t" 让Python换到下一行，并在下一行开头添加一个制表符
print("Languages:\nPython\nC\nJavaScript")

# 删除空白 要确保字符串末尾没有空白，可使用方法rstrip() 。
favorite_language = ' hello python '

print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.replace('hello','hi'))

# 在用单引号括起的字符串中，如果包含撇号，就将导致错误。这是因为这会 导致Python将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视为Python代码，从而引发错误。
message = "One of Python's strengths is its diverse community."
print(message)


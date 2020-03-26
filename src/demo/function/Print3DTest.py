# 模拟打印每个设计，直到没有未打印的设计为止 打印每个设计后，都将其移到列表completed_models中
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

# 显示打印好的所有模型
def show_models(completed_models):
    print("\nThe models in list are:")
    for completed_model in completed_models:
        print(completed_model)



# 改变参数unprinted_designs1
unprinted_designs1 = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models1 = []
print_models(unprinted_designs1, completed_models1)
show_models(unprinted_designs1)
show_models(completed_models1)
# 不改变参数unprinted_designs2  【使用切片实现unprinted_designs2的复制，然后作为参数传入，但不会改变原来的参数】
print('--------------------------------')
unprinted_designs2 = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models2 = []
print_models(unprinted_designs2[:], completed_models2)
show_models(unprinted_designs2)
show_models(completed_models2)
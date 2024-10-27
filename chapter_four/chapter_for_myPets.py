#for i in  range(len([1,2,3,4,5]),10):
#    print(i)
'''
myPets = ['Zophie','Pooka','Fat-tail']
print("Enter a pet name:")
name = input("Enter a pet name:")
if name not in myPets:
    myPets=myPets+[name]
    [print(myPets[i]) for i in range(len(myPets))]
    print("I do not have a pet named"+name)
    


else:
    print(name+'is my pet.')

matrix = [[i * j for j in range(3)] for i in range(3)]  
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix) '''
matrix = []  # 初始化空列表
for i in range(3):
    row = []  # 初始化每一行
    for j in range(3):
        row.append(i * j)  # 计算 i * j 并添加到当前行
    matrix.append(row)  # 将完整的一行添加到 matrix

print(matrix)


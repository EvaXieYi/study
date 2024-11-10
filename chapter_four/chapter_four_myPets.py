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
         [[i * j for i in range(3)] for i in range(3)]
print(matrix) '''
matrix = []  # 初始化空列表
for i in range(3):
    row = []  # 初始化每一行
    for j in range(3):
        row.append(i * j)  # 计算 i * j 并添加到当前行
    matrix.append(row)  # 将完整的一行添加到 matrix

print(matrix)


name=[1,2,3]
a,b,c=name
print(a,b)


for x,y in enumerate(name):
    print(x,y)

import random
pets=['Dog','Cat','Moose']
print(random.choice(pets))
#random.choice(pets)==pets[random.randint(0,len(pets)-1)]

print(pets[random.randint(0,len(pets)-1)])
random.shuffle(pets)
print(pets)
a=random.shuffle(pets)
print(a)

a=1
a+=1
a/=1
a-=1
a*=1
a**=1
a%=1

a="aaaaa"
b=["1","2","3"]
b+=[a]
a*=3

print(b)

print(b.index("1"))

b.insert(1,"aaaa")
b.append(a)
print(b)

b.sort(key=str.lower)
# 续行字符，对一行中比较长的代码。进行换行处理，在续行字符之后一行，缩进不重要
c=[1,2,3,"string","float","int","False", \
     "True"]
c.reverse()
print(c)

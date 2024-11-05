squares = [x*2  for x in range(10)]
print(squares)

import random
spam=['cat','bat','rat','elephant',[1,2,3,[4,5,6]]]
print(spam[4][3][1])
print(spam[1-1])
print(spam[-1])
print(spam[:])
print(spam[0:5])
print(len(spam))
print('Hello',spam[0],sep=" ")
def abc(*mc):
    print(mc)




abc(1,2,3,4,5)


a=0
for i in range(2,6):
    a=a+1
    b=10-i
    print("第%s行: 10-%s=%s" %(a,i,b) )
    
for i in range(2,6):  # <1>处填入3，表示从3开始递减到1
    print("第", i-1, "行:", end="\t")  # <2>处填入i，表示行号
    print("10","-", i, "=", 10-i) 


if None=="":
    print("none")
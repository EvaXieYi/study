print((1==1)and(2==2))
print(not(2==2))
print((1!=1)or(2!=2))
print(2+1==4 and not 2+2==5 and 2**2==2+2)
'''
操作符顺序
not > and > or
在python中如果一个长表达式求值的过程中，python会先求值not操作符，在求值and操作符，最后求值or操作符
'''
print(id('我'))
print(id('时'))
print('a' is 'a')
print(33333 and 13333)#错误写法
name = "Mary"
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Worng password')
def abc():

    if name == "aliase":
        print()
    else:
        return 0
if abc() == 0:
    print("该名称不是"+"aliase")
print(abc())



if 1==1:
    print("xie")
elif 1==1:
    print("yi")
else:
    print("xieyi")

while  1==1:
    print(1+1!=1+1)
    break
'''
i=0
while i < 10:
      i+=1
      print(range(i,i+100))
i+=1
i=i+1'''

def num(i):
    print(i)
    return i+1

i=0
while i<5:
    i=num(i)
   
'''
smpa=0
while smpa<5:
    if smpa<5:
        print("Hello world")
    
    smpa +=1'''

'''
name=""
while name !='your name':
    print('Please type your name')
    name=input('你的名字')
print("think your!")


while 1==1:
   print('Please type your name')
   name=input()
   if name=="your name":
      print("think your!")
      break


while True:
     
     name=input("请输入用户名")
     if name != "xieyi":
         print("您输入用户名错误重新输入")
         continue
     print("hello xieyi")
     
     passwd=input("请输入密码")
     if passwd == "123456":
         print("欢迎登录")
         print("Access granted")
         break
    
print(hex(100))
None     
'''
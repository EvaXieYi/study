'''def a(agv,abc=100,*argv,**arag):
     print(f"agv:\t{agv}")
     print(f"abc:\t{abc}")
     print(f"argv:\t{argv}")
     print(f"arag:\t{arag}")
a(1,1,2,3,4,5,6,name="张三",lisi="王五",www="我你")


def spam():
    
    global name
    name="王五"
    spam2()
def spam1():
    name="老四"
def spam2():
    print(name)

name="123"
spam2()
print(name)
'''
def spam():
    print(eggs)
    global eggs
    eggs='spam local'
eggs="abc"
spam()
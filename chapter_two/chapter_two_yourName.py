'''name=""
while not name:
     print("Enter your name:")
     name = input()
print("How many guests will you have")
numOfGuests=int(input())
if numOfGuests:
     print("Be sure to have enough room for all your guests")
print('Done')


print('My name is')
for i in range(5):
    print('jimmy five Times(' +str(i)+')')


total=0
for num in range(101):
    total=total+num
    print(total)


totle=0
a=0
while totle<101:
    a=a+totle
    totle+=1
print(a)
'''
from random import randint


for i in range(10):
     print(randint(1,10))
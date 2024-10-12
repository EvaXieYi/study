'''import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
for guessesTaken in range(1,7):
    print('task a guest')
    
    guess = int(input())
    
    if guess < secretNumber:
        print('You guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else :
        break'''

from random import randint

number=randint(1,20)


try:
    while  True:
  
        a=int(input("输入一个值"))
    

        if a < number:
            print('You guess is too low.')
            continue
        elif a > number:
             print('Your guess is too high.')
             continue
        else :
             break

    if a == number:
        print("输入的字符相等")
    else:
        print("输入错误"+str(a)+"正确的数字是"+str(number))
except ValueError:
     print("类型错误")
except NameError:
     print("无法确认")

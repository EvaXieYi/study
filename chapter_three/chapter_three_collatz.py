import sys
def collatz(namber):
   
        if namber % 2 ==0:
            return namber // 2
        elif namber % 2 ==1:
            return 3 * namber + 1
while True:       
    try:
        number1=int(input("输入一个数字"))
        
        print(collatz(number1))
        if collatz(number1)==1:
              sys.exit()

    except ValueError:
            print("您输入的不是整数")
    
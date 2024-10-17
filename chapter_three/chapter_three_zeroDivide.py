def abc(num,number1=10,**number3,):
    try:
        return  number1 / num
    except ZeroDivisionError as e:
           print(e)
abc(0,14)
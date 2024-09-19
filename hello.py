print('Hello world!')
print('what is your Name!')
name= input()
print('It is good to meth you,'+name)
print('The length of your name is :')
print(len(name))
print('what is your age !')
Age=input()
print('you will be '+str(int(Age)+1)+' in a year')
print([x**2 for x in range(10)])
print([x**3 for x in range(11)])

numbers = [3.14, 2.71, 4.56]
rounded_numbers = [round(num) for num in numbers]
print(rounded_numbers)
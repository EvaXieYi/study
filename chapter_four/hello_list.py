squares = [x*2  for x in range(10)]
print(squares)


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

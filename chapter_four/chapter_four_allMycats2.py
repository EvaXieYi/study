'''catName=[]
print(len(catName))
while True:
    print('Enteer the name of cat\t'+ str(len(catName)+1)+'\t(Or enter nothing to stop.):')
    name=input()

    if name == "":
         break
    
    catName=catName+[name]

print('The cat names are:')
for name in catName:
      print(''+name)
'''

a=[1,3,4,5]

for i in range(len(a)):
     print(i)



print(1 in a)
print(2 in a)
#for i in range(5,10,1000):
#    print(i)

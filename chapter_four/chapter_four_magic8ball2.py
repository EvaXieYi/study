import random
messages=['It is certain','It is decidedly so','Yes definitely','Reply hazy try again','Ask again later' \
          ,'Concentrate and ask again','My reply is no','Outlook not so good','Very doubtful' \
         ]
print(len(messages))
print(messages[random.randint(0,len(messages)-1)])

name="Xieyi"
print(name[0])
print(name[-2])
print(name[3:-1])
print("X" in name)
print("e" not in name)
for i in name:
    print("*****"+i+"*****")

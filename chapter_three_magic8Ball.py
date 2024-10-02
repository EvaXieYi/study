import random
def getAnswerI(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask agin'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
#r =random.randint(1,9)
#fortune = getAnswerI(r)
#print(fortune)
print(getAnswerI(random.randint(1,9)))
<<<<<<< HEAD

print(None)
=======
a=None
print(a)
>>>>>>> a4fee564ff4553ef5b8b6983382c24603f4a4971

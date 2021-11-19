userword = input ("Enter your word: ")
revword = userword[::-1]
print (revword)


userword = input ("Enter your word: ")
lettercount = len(userword)
for i in range(lettercount-1, -1, -1):
    print (userword[i])


userword = input ("Enter your word: ")
lettercount = len(userword)
revword = ""
for i in range(lettercount-1, -1, -1):
    print(revword)

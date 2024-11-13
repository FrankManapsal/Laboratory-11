wordlist=[]
displaywords=[]
while len(wordlist)!=10:
    word=input("Enter a Word: ")
    if word in wordlist:
        print("Word already exists in the list")
        continue
    else:
        wordlist.append(word)
if len(wordlist)==10:
    number=int(input("Please Enter a Number: "))
    for wordz in wordlist:
        if len(wordz)>=number:
            displaywords.append(wordz)
        else:
            continue   
    print(displaywords)
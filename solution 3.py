def consonants():
    letter=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    value=[2,3,4,6,7,8,10,11,12,13,14,16,17,18,19,20,22,23,24,25,26]
    word = input("Enter the magic word: ")
    newWord= word.lower()
    maxValue=0
    print(newWord)
    for char in newWord:
            if char in letter:
                charIndex=letter.index(char)
                charValue=value[charIndex]
                if charValue > maxValue:
                     maxValue=charValue
                     print("The highest Value is " + str(maxValue))
consonants()
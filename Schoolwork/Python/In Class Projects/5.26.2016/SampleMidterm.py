wordList = []
longWords = []
reverseList = []


def userInput():
    global integer
    for i in range(3):
        wordList.append(input("Please enter word #" +str(i+1)))
    integer = int(input("Please enter the maximum amount of characters each word can be."))
    filter_long_words()
    
def filter_long_words():
    global integer
    for item in wordList:
        if len(item) > integer:
            longWords.append(item)
    
userInput()                    
def palindrome():
    for item in longWords:
        reverse = ""
        for letter in range(len(item)-1, -1, -1): #range(start, stop, sequence)
            reverse += item[letter].upper()
        reverseList.append(reverse)
    with open("Output.txt", "w") as text_file:
        for i in range(len(reverseList)):
            text_file.write(str(reverseList[i] + ","))

palindrome()
def isPalindrome():    
    word = input("Please enter a word to see if it is Palindrome")
    reverse = ""

    for letter in range(len(word)-1, -1, -1): #range(start, stop, sequence)
        reverse+=word[letter]
    
    return reverse == word
print(isPalindrome())
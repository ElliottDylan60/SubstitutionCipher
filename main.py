def main():
    cipherText = input("Please enter the cipher text: ")
    letterCount(cipherText.upper())
    key = input("Please enter a possible key: ")
    if(len(key) > 26):
        key = key[:26]
    plainText(cipherText.upper(), key.upper())
    
"""
Calculates and displays the frequency of each letter in the input string "cipherText"
"""
def letterCount(cipherText): 
    print("letter count: ")
    freq = {}
    for i in cipherText:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)
"""
    This function applies a substitution cipher to the input string "cipherText" 
    using the provided "key" to replace each character with a corresponding value.
"""  
def plainText(cipherText, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in cipherText:
        index = key.find(letter)
        if(index > -1):
            result += alphabet[index]
        else:
            result += letter
    
    print(result)

main()
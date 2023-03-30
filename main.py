def main():
    plainText("MXDXBVTZWVMXNSPBQXLIMSCCSGXSCJXBOVQXCJZMOJZCVCTVWJCZAAXZBCSSCJXBQCJZCOJZCNSPOXBXSBTVWJCJZDXGXXMOZQMSCSCJXBOVQXCJZMOJZCNSPJZHGXXMOSPLHJZDXZAAXZBXHCSCJXTCSGXSCJXBOVQX", "ZGEHXIWJVKFLTMSAYBQCPDORNU")
"""
Calculates and displays the frequency of each letter in the input string "cipherText"
"""
def letterCount(cipherText):
    print("letter count")
"""
This function applies a substitution cipher to the input string "cipherText" 
using the provided "key" to replace each character with a corresponding value.
"""
def plainText(cipherText, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in cipherText:
        result += alphabet[key.find(letter)]
    print(result)

main()
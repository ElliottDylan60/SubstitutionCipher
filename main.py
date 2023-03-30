# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:28:33 2023

@author: megan
"""

def main():
    plainText("MXDXBVTZWVMXNSPBQXLIMSCCSGXSCJXBOVQXCJZMOJZCVCTVWJCZAAXZBCSSCJXBQCJZCOJZCNSPOXBXSBTVWJCJZDXGXXMOZQMSCSCJXBOVQXCJZMOJZCNSPJZHGXXMOSPLHJZDXZAAXZBXHCSCJXTCSGXSCJXBOVQX", "ZGEHXIWJVKFLTMSAYBQCPDORNU")
    letterCount("MXDXBVTZWVMXNSPBQXLIMSCCSGXSCJXBOVQXCJZMOJZCVCTVWJCZAAXZBCSSCJXBQCJZCOJZCNSPOXBXSBTVWJCJZDXGXXMOZQMSCSCJXBOVQXCJZMOJZCNSPJZHGXXMOSPLHJZDXZAAXZBXHCSCJXTCSGXSCJXBOVQX")
"""
Calculates and displays the frequency of each letter in the input string "cipherText"
"""
def letterCount(cipherText):
    """
    This function applies a substitution cipher to the input string "cipherText" 
    using the provided "key" to replace each character with a corresponding value.
    """  
    print("letter count: ")
    freq = {}
    
    for i in cipherText:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
            
    print(freq)


def plainText(cipherText, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in cipherText:
        result += alphabet[key.find(letter)]
    print(result)

main()
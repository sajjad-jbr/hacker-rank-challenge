#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    listWords = sentence.split(" ")
    
    res = ""
    for wordIndex in range(len(listWords)-1,-1,-1):
        word = listWords[wordIndex]
        for char in word:
            if char.islower():
                char = char.upper()
            elif char.isupper():
                char = char.lower()
            res+=char 
        res+=" "
    res = res[0:-1]
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()

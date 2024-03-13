import itertools
import operator
import sys
import time
import typing
from typing import List

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
# sys.stderr = open("error.txt", "w")


def read_list_int():
    string_data = input()
    if string_data == "[]":
        return []

    # Remove brackets and split by comma
    list_data = string_data[1:-1].split(",")

    # Convert each element to an integer
    int_list = [int(x) for x in list_data]
    return int_list


def read_int(number_split: int = 1):
    if number_split == 1:
        return int(input())

    return map(int, input().split())


class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        if len(s) ==1:
            return roman2int[s[0]]

        result=0
        for index in range(len(s[0:-1])):
            if roman2int[s[index+1]]> roman2int[s[index]]:
                result -= roman2int[s[index]]
            else:
                result += roman2int[s[index]]
        
        result += roman2int[s[-1]]
     
        return result
    
    
    def romanToInt_another(self, s: str) -> int:
        roman2int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        
        result=roman2int[s[0]]
        for index in range(1,len(s)):
            if roman2int[s[index-1]] < roman2int[s[index]]:
                result += roman2int[s[index]] - 2*roman2int[s[index-1]]
            else:
                result += roman2int[s[index]]
        
        return result


number_of_examples = 3
start_time = time.time()
for _ in range(number_of_examples):
    s = input()
    s = s[1:-1] # remove "" from input
    print(Solution().romanToInt_another(s=s))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"")
print(f"Elapsed time: {(elapsed_time * 1000 /number_of_examples ) :.4f} ms")

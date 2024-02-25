import sys
import typing
from typing import List

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
# sys.stderr = open("error.txt", "w")

def read_list_int() -> List[int]:
    string_data = input()
    if string_data == "[]":
        return []

    # Remove brackets and split by comma
    list_data = string_data[1:-1].split(",")

    # Convert each element to an integer
    int_list = [int(x) for x in list_data]
    return int_list
    
def read_int(number_split:int = 1) :
    if number_split == 1:
        return int(input())

    return map(int, input().split())

number_of_examples = 2
import math

def majorityElement( nums: List[int]) -> int:
    count_dict = {}
    m = math.ceil(len(nums) /2)
    for n in nums:
        if n not in count_dict.keys():
            count_dict[n] = 1
        else:
            count_dict[n] += 1
            if count_dict[n] >=m:
                return n
                # print(n)

def majorityElement_moore( nums: List[int]) -> int:
    # this function use moore voting algorithm
    count=0
    element=0
    for n in nums:
        if count==0:
            element=n
            count=1
        elif element==n:
            count += 1
        else:
            count -=1
    print(element)

for _ in range(number_of_examples):
    nums = read_list_int()
    # majorityElement(nums=nums)
    majorityElement_moore(nums=nums)


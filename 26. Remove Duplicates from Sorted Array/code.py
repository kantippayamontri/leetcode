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

def removeDuplicates( nums: List[int]) -> int:
    num_dup=1
    index=0
    for i in range(1,len(nums)):
        if nums[index] != nums[i]:
            num_dup += 1
            nums[index + 1] = nums[i]
            index += 1
    
    # print(nums)
    # print(num_dup)
    return num_dup
            
            

for _ in range(number_of_examples):
    nums = read_list_int()

    removeDuplicates(nums=nums,)
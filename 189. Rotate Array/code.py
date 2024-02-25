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

def rotate_slow(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            temp = nums[0]
            nums[0] = nums[len(nums)-1]
            for i in range(1,len(nums)):
                store = nums[i]
                nums[i] = temp
                temp = store
        
        print(nums)

def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        last_k = nums[len(nums)-k :len(nums)]
        for i in range(len(nums)-1-k ,-1,-1):
            nums[i+k] = nums[i]
        
        for i in range(k):
            nums[i] = last_k[i]
        
        print(nums)

        # for ele in last_k:
        #     print(ele)

for _ in range(number_of_examples):
    nums = read_list_int()
    k = read_int()
    rotate(nums=nums, k=k)

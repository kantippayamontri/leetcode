import sys
import typing
from typing import List
import time

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

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


def removeElement(nums: List[int], val: int) -> int:
    delete_number = 9999
    search_index=len(nums) -1
    val_index = []

    while search_index >=0:
        if nums[search_index] == val:
            nums[search_index] = delete_number
            search_index -=1
            val_index.append(search_index + 1)
        else:
            search_index -=1
    
    k = len(nums) - len(val_index)
    
    search_index = len(nums) -1

    # sort the nums list 
    for i in val_index:
        if i in range(k):
            while True:
                if nums[search_index] != delete_number:
                    # swap value 
                    nums[i] = nums[search_index]
                    nums[search_index] = delete_number
                    search_index -=1
                    break
                else:
                    search_index -= 1 

    # print(k, nums, val_index)
    return k
         
number_of_examples = 2


def removeElement_2(nums: List[int], val: int) -> int:
    index=0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    # print(index)
    return index

start_time = time.time() # start time
for _ in range(number_of_examples):
    nums = read_list_int()
    val = read_int()

    removeElement_2(nums=nums, val=val)
end_time = time.time() # end time

elapsed_time = end_time - start_time
print(f"-"*50)
print(f"Elapsed time: {(elapsed_time / number_of_examples) :.8f}", )
print(f"-"*50)


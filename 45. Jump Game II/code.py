import sys
from typing import List
import time

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

def Jump( nums: List[int]) -> bool:

    n_jump=0

    if len(nums) ==1:
        return 0

    now_index=0
    while (now_index < len(nums)-1):
        jump = nums[now_index]

        if now_index + jump >= len(nums)-1: 
            n_jump += 1
            return n_jump
        else:
            jump_index_list = [ (nums[now_index +i+1] + (i+1) + now_index, i+1 + now_index) for i in range(jump)]
            #find max jump
            jump_max_index = sorted(jump_index_list, reverse=True)[0][1]

            now_index = jump_max_index
            n_jump += 1
    
    return n_jump
            

# def Jump_best( nums: List[int]) -> bool:
#     """
#     Imagine you have a car, and you have some distance to travel (the length of the array).
#     This car has some amount of gasoline, and as long as it has gasoline, it can keep traveling on this road (the array).
#     Every time we move up one element in the array, we subtract one unit of gasoline.
#     However, every time we find an amount of gasoline that is greater than our current amount, we "gas up" our car by replacing our current amount of gasoline with this new amount.
#     We keep repeating this process until we either run out of gasoline (and return false), or we reach the end with just enough gasoline (or more to spare), in which case we return true.
    
#     Note: We can let our gas tank get to zero as long as we are able to gas up at that immediate location (element in the array) that our car is currently at.
#     """
#     gas =0
#     for n in nums:
#         if gas <  0:
#             return False
#         elif n > gas:
#             gas = n
#         gas -=1
#     return True

start_time = time.time()

for _ in range(number_of_examples):
    nums = read_list_int()
    print(Jump(nums=nums))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"")
print(f"Elapsed time: {(elapsed_time * 1000 /number_of_examples ) :.4f} ms")
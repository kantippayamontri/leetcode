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

number_of_examples =2 

def maxProfit( prices: List[int]) -> int:
    print(prices)
    

for _ in range(number_of_examples):
    nums = read_list_int()
    maxProfit(prices=nums)
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
    def canCompleteCircuit_better(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_surplus = 0
        surplus = 0
        start = 0
        
        for idx in range(n):
            total_surplus += gas[idx] - cost[idx]
            surplus += gas[idx] - cost[idx] # เราต้องการ check ว่าถ้าต้องย้าย station ยังมีนำ้มันเหลือไหม

            if surplus < 0: # ถ้าน้ำมันติดลบ เราจะเลือก station ใหม่เลย
                surplus = 0
                start = idx + 1
        return -1 if total_surplus < 0 else start
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            total_surplus=gas[i]
            prev_cost = cost[i]
            jump_index = (i+1) if (i + 1) < n else 0
            
            while True:
                total_surplus -= prev_cost

                if total_surplus < 0:
                    break

                prev_cost = cost[jump_index]
                total_surplus += gas[jump_index]

                jump_index = (jump_index+1) if (jump_index + 1) < n else 0
                
                if jump_index == i:
                    total_surplus -= prev_cost
                    if total_surplus >=0:
                        return i
                    break
            
        
        return -1

        
    
number_of_examples = 2
start_time = time.time()
for _ in range(number_of_examples):
    gas = read_list_int()
    cost = read_list_int()
    print(Solution().canCompleteCircuit(gas=gas, cost=cost)) #pls use better if use normal in leetcode -> time limit exceed

end_time = time.time()
elapsed_time = end_time - start_time
print(f"")
print(f"Elapsed time: {(elapsed_time * 1000 /number_of_examples ) :.4f} ms")

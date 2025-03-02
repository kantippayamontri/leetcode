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


number_of_examples = 3
start_time = time.time()
for _ in range(number_of_examples):
    nums1 = read_list_int()
    m = read_int()
    # print(Solution().)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"")
print(f"Elapsed time: {(elapsed_time * 1000 / number_of_examples):.4f} ms")

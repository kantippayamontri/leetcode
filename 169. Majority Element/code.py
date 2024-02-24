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

number_of_examples = 3

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    print(nums1,m,nums2,n)

for _ in range(number_of_examples):
    nums1 = read_list_int()
    m = read_int()
    nums2 = read_list_int()
    n = read_int()

    merge(nums1=nums1, m=m, nums2=nums2,n=n)
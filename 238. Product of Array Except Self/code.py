import sys
import typing
from typing import List
import time
import itertools
import operator

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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_result = 1
        if 0 not in nums:
            for mul_iter in itertools.accumulate(nums, operator.mul):
                mul_result = mul_iter
            ans = []
            for n in nums:
                ans.append(int(mul_result / n))
            return ans

        else:
            zero_list = []
            result_list = []
            mul_result = 1
            for index, data in enumerate(nums):
                if data != 0:
                    mul_result *= data
                else:
                    zero_list.append(index)

            for index, data in enumerate(nums):
                if (data != 0) or (data == 0 and len(zero_list) > 1):
                    result_list.append(0)
                else:
                    result_list.append(mul_result)

            return result_list

    def productExceptSelf_better(self, nums: List[int]) -> List[int]:
        count_zero = 0
        mul_non_zero = 1

        for n in nums:
            if n == 0:
                count_zero += 1
            else:
                mul_non_zero *= n

        ans = []
        if count_zero == 0:
            for n in nums:
                ans.append(int(mul_non_zero / n))
        elif count_zero == 1:
            for n in nums:
                if n != 0:
                    ans.append(0)
                else:
                    ans.append(mul_non_zero)
        else:
            ans = [0] * len(nums)

        return ans


number_of_examples = 2
start_time = time.time()
for _ in range(number_of_examples):
    nums = read_list_int()
    # m = read_int()
    print(Solution().productExceptSelf_better(nums=nums))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"")
print(f"Elapsed time: {(elapsed_time * 1000 /number_of_examples ) :.4f} ms")

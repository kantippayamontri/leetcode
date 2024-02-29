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


def read_int(number_split: int = 1):
    if number_split == 1:
        return int(input())

    return map(int, input().split())


number_of_examples = 4


def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy = None
    for i in range(len(prices) - 1):
        if buy is None:
            if prices[i + 1] <= prices[i]:
                continue
            else:
                buy = prices[i]
        else:
            if (prices[i + 1] < prices[i]) and (prices[i] > buy):
                profit += prices[i] - buy
                buy = None
            else:
                ...

    if (buy is not None) and (buy < prices[-1]):
        profit += prices[-1] - buy

    return profit

def maxProfit_2(prices: List[int]) -> int:
    profit=0
    for i in range(1,len(prices)):
        if prices[i-1] < prices[i]:
            profit += prices[i] - prices[i-1]
    
    return profit

for _ in range(number_of_examples):
    nums = read_list_int()
    # print(maxProfit(prices=nums))
    print(maxProfit_2(prices=nums))

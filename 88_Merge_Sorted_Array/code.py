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


number_of_examples = 1


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    # Do not return anything, modify nums1 in-place instead.

    def slide_right_arr(arr, index):
        if index >= len(arr):
            return

        val_before = arr[index]
        for i in range(index + 1, len(arr)):
            temp = arr[i]
            arr[i] = val_before
            val_before = temp
        arr[index] = 0

    def insert_arr(arr, index, value):
        if index >= len(arr):
            return

        val_before = arr[index]
        for i in range(index, len(arr)):
            temp = arr[i]
            arr[i] = val_before
            val_before = temp
        arr[index] = value

    def check_zero(arr, index):
        for i in range(index, len(arr)):
            if arr[i] !=0:
                return True
        return False

    if m == 0 and n != 0:
        for index in range(n):
            nums1[index] = nums2[index]

    elif m != 0 and n == 0:
        ...
    else:
        size_ans = m + n
        index_search = 0
        for index in range(n):
            if nums2[index] >= nums1[index_search]:
                # check how many skip
                for index_check_skip in range(index_search + 1, size_ans):
                    if (nums1[index_check_skip] <= nums2[index]) and (
                        # nums1[index_check_skip] != 0
                        check_zero(arr=nums1, index=index_check_skip)
                    ):
                        index_search += 1

                insert_arr(arr=nums1, index=index_search + 1, value=nums2[index])
                index_search += 1
            else:
                print(index_search, nums1)
                slide_right_arr(arr=nums1, index=index_search)
                print(nums1)
                nums1[index_search] = nums2[index]
                index_search += 1
    
    print(nums1) #remove this line for submit


def merge_2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    if m==0 and n != 0:
        for i in range(n):
            nums1[i] = nums2[i]
    elif m !=0 and n==0:
        pass
    else:
    
        end_idx = m + n -1
        nums1_end = m-1
        nums2_end = n-1
    
        while nums1_end >= 0 and nums2_end >= 0:
            if nums2[nums2_end] > nums1[nums1_end]:
                nums1[end_idx] = nums2[nums2_end]
                nums2_end -=1
                end_idx -=1
            elif nums2[nums2_end] < nums1[nums1_end]:
                nums1[end_idx] = nums1[nums1_end]
                nums1[nums1_end] = 0
                nums1_end -=1
                end_idx-=1
            elif nums2[nums2_end] == nums1[nums1_end]:
                nums1[end_idx] = nums2[nums2_end]
                nums2_end -=1
                end_idx -=1
                
                nums1[end_idx] = nums1[nums1_end]
                nums1_end -=1
                end_idx -=1
            
        
        while end_idx >= 0 and nums2_end >=0:
            nums1[end_idx] = nums2[nums2_end]
            nums2_end -= 1
            end_idx -= 1
            
    
    print(nums1)


for _ in range(number_of_examples):
    nums1 = read_list_int()
    m = read_int()
    nums2 = read_list_int()
    n = read_int()

    merge_2(nums1=nums1, m=m, nums2=nums2, n=n)

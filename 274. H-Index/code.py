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


def read_int(number_split: int = 1):
    if number_split == 1:
        return int(input())

    return map(int, input().split())


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """this method use O(n^2)"""
        h_index = 0
        for index_cite in range(len(citations)):
            if citations[index_cite] == 0:
                continue

            count_index = 1  # count itself

            # search left
            for index_left in range(index_cite):
                if citations[index_left] >= citations[index_cite]:
                    count_index += 1

            # search right
            for index_right in range(index_cite + 1, len(citations)):
                if citations[index_right] >= citations[index_cite]:
                    count_index += 1

            if count_index > citations[index_cite]:
                count_index = citations[index_cite]

            h_index = max(h_index, count_index)

        return h_index

    def hIndex2(self, citations: List[int]) -> int:
        """This method use O( nlogn + n ) , nlogn for sort, n for iterate to find h-index"""
        new_cite = sorted(citations) #use nlogn time
        print(new_cite)
        h_index=0
        last_index = len(new_cite) -1
        print(last_index)
        for i in range(len(new_cite)):
            if new_cite[i]==0:
                continue

            distance =last_index - i +1  
            if (distance >= new_cite[i]) and (distance > h_index):
                h_index = new_cite[i]
                
            print(i, new_cite[i], distance)


        return 0


number_of_examples = 4
start_time = time.time()
for _ in range(number_of_examples):
    nums = read_list_int()
    # print(Solution().hIndex(citations=nums))
    print(Solution().hIndex2(citations=nums))
    # Solution().hIndex(citations=nums)
    print(f"+" * 50)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"")
print(f"Elapsed time: {(elapsed_time * 1000 /number_of_examples ) :.4f} ms")

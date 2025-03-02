from utils import Utils
import sys
import time

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

import random


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.index_check = {}
        return None


    def insert(self, val: int) -> bool:
        if val not in self.index_check:
            self.data.append(val)
            self.index_check[val] = len(self.data) - 1

            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index_check:
            del_index = self.index_check[val]  # index of the value to be deleted
            # swap the value to be deleted with the last value
            self.data[del_index] = self.data[-1]
            self.index_check[self.data[-1]] = del_index

            self.data.pop()
            del self.index_check[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

number_of_examples = 1
start_time = time.time()
for _ in range(number_of_examples):
    commands = Utils.read_list_str()
    nums = Utils.read_list_int_recursive()
    # print(commands)
    # print(nums)
    _random = None
    for cmd, arg in zip(commands, nums):
        match cmd:
            case "RandomizedSet":
                _random = RandomizedSet()
                print(None)
            case "insert":
                print(_random.insert(arg))
            case "remove":
                print(_random.remove(arg))
            case "getRandom":
                print(_random.getRandom())
            case _:  # default case
                pass

end_time = time.time()
elapsed_time = end_time - start_time
print("")
print(f"Elapsed time: {(elapsed_time * 1000 /number_of_examples ) :.4f} ms")

from Utils import utils
from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:
        # get the min len
        min_str = min(strs, key=len)
        # print(f"min_str: {min_str}")
        for i in range(len(min_str)):
            for data in strs:
                if min_str[i] != data[i]:
                    return min_str[0:i]

        return min_str

        #     string_check = ans + min_str[i]
        #     check = True
        #
        #     for data in strs:
        #         if string_check not in data :
        #             check = False
        #             break
        #
        #     # all input string contain string_check
        #     if check:
        #         ans = string_check
        #     else:
        #         return ans
        #
        # return ans


nEx = 3
if __name__ == "__main__":
    import os

    p = os.getcwd() + "/14_Longest_Common_Prefix"
    utils.Utils.setup(path=p)
    for _ in range(nEx):
        str = utils.Utils.read_list_str()
        output = Solution.longestCommonPrefix(strs=str)
        print(output)

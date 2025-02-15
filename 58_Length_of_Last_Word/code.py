from Utils import utils


class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if count == 0:
                    continue
                else:
                    return count
            else:
                count += 1
        return count


nEx = 4
if __name__ == "__main__":
    import os

    p = os.getcwd() + "/58_Length_of_Last_Word"
    utils.Utils.setup(path=p)
    for _ in range(nEx):
        str = utils.Utils.read_str(remove_char='"')
        output = Solution.lengthOfLastWord(s=str)
        print(output)

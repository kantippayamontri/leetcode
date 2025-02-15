from Utils import Utils


class Solution:
    def reverseWords(s: str) -> str:
        ans = ""
        temp = ""
        for i in range(len(s) - 1, -1, -1):
            char = s[i]

            if char != " ":
                temp =  char + temp
            else:
                if temp == "":
                    continue
                ans += temp + " "
                temp = ""

        # add the last word
        if temp == "":
            ans = ans[0:-1]
        else:
            ans += temp

        return ans


nEx = 3
if __name__ == "__main__":
    import os

    p = os.getcwd() + "/151_Reverse_Words_in_a_String"
    Utils.setup(path=p)
    for _ in range(nEx):
        str = Utils.read_str(remove_char='"')
        output = Solution.reverseWords(s=str)
        print(output)

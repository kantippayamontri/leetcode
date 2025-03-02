from Utils import Utils


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack) # len haystack
        len_n = len(needle) # len needle

        if len_h < len_n:
            return -1

        if len_h == len_n:
            if haystack == needle:
                return 0
            return -1

        last_pos = len(haystack) - (len_n - 1)
        for i in range(0, last_pos, 1):
            if haystack[i] == needle[0]:
                # check the text
                if haystack[i : i + len_n] == needle:
                    return i

        return -1


nEx = 4
if __name__ == "__main__":
    import os

    p = os.getcwd() + "/28_Find_the_Index_of_the_First_Occurrence_in_a_String"
    Utils.setup(path=p)
    for _ in range(nEx):
        haystack = Utils.read_str(remove_char='"')
        needle = Utils.read_str(remove_char='"')

        s = Solution()
        output = s.strStr(haystack=haystack, needle=needle)
        print(output)

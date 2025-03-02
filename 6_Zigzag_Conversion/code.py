from os import remove
from Utils import Utils


def print_ans(
    start_idx: int, end_idx: int, row: int, dis: int, ori_str: str, inside: int | None
):
    temp_idx = start_idx
    result = ""
    while temp_idx <= end_idx:
        result += ori_str[temp_idx - 1]  # -1 for real index

        if inside is not None:
            inside_idx = temp_idx + (row - start_idx + inside)
            if inside_idx <= end_idx:
                result += ori_str[inside_idx - 1]

        temp_idx += dis + row

    return result


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    ans = ""
    dis = numRows - 2
    len_str = len(s)
    _inside = dis
    for r in range(1, numRows + 1, 1):
        # for first and last row
        if r in (1, numRows):
            ans += print_ans(
                start_idx=r,
                end_idx=len_str,
                row=numRows,
                dis=dis,
                ori_str=s,
                inside=None,
            )
        else:
            # for inside row
            ans += print_ans(
                start_idx=r,
                end_idx=len_str,
                row=numRows,
                dis=dis,
                inside=_inside,
                ori_str=s,
            )
            _inside -= 1

    return ans


nEx = 3
if __name__ == "__main__":
    import os

    p = os.getcwd() + "/6_Zigzag_Conversion"
    Utils.setup(path=p)
    for _ in range(nEx):
        strs = Utils.read_str(remove_char='"')
        row = Utils.read_int()
        output = convert(s=strs, numRows=row)
        print(output)

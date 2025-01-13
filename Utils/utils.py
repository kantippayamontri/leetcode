class Utils:
    """
    # TODO: add more case like  
    [[], [1,2,3], [2], [2,4,5], [], [1], [2], []]
    [[], [1,2,3, [4,5,6], [2], [2,4,5, [1,2,3], [], [1], [2], []]
    """
    # for read the input like this [[], [1], [2], [2], [], [1], [2], []]
    @staticmethod
    def read_list_int_recursive():
        string_data = input()
        data_list = string_data[1:-1].replace(" ", "").split(",")
        results = []
        for d in data_list:
            if d == '[]':
                results.append([])
            else:
                d_int = int(str(d).replace("[", "").replace("]", "").strip())
                results.append(d_int)

        return results 

    @staticmethod
    def read_list_int():
        string_data = input()
        if string_data == "[]":
            return []

        # Remove brackets and split by comma
        list_data = string_data[1:-1].split(",")

        # Convert each element to an integer
        int_list = [int(x) for x in list_data]
        return int_list

    @staticmethod
    def read_list_str():
        string_data = input()
        if string_data == "[]":
            return []

        # Remove brackets and split by comma
        list_data = string_data[1:-1].split(",")

        # Convert each element to an integer
        str_list = [str(x[1:len(x)-1]) for x in list_data]
        return str_list

    @staticmethod
    def read_int(number_split: int = 1):
        if number_split == 1:
            return int(input())

        return map(int, input().split())

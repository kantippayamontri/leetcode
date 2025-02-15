from Utils import utils


digit_lists = {
	4: [("M", 1)],
	3: [("D", 5), ("C", 1)],
	2: [("L", 5), ("X", 1)],
	1: [("V", 5),("I",1)]
}

def compute(digit: int, val: int):
	"""
	digit = digit of the number
	val = value of the number in these digit
	"""
	# print(f"digit: {digit}, val: {val}")
	if digit >= 4 :
		return "M" * val
	
	ans = ""
	
	# check if digit is 4 or 9
	if val == 4:
		previous_roman = digit_lists[digit][1]
		now_roman = digit_lists[digit][0]
		# if now_roman[1] == 5: # no need to check 
			return previous_roman[0] + now_roman[0]
	
	if val == 9:
		# check is previous digits is 1
		previous_roman = digit_lists[digit+1][-1]
		now_roman = digit_lists[digit][1]
		# if previous_roman[1] == 1: # no need to check
			return now_roman[0] + previous_roman[0]
	

	while val != 0:
		for character, roman_val in digit_lists[digit]: 
			if val >= roman_val:
				val -= roman_val
				ans += character
	
	return ans


	
		

def intToRoman(num: int):
	ans = ""
	digit_list = list(range(1,len(str(num)) +1))
	digit_list.reverse()
	for digit, val  in zip(digit_list, str(num)):
		ans += compute(digit, int(val))
		# print(f"digit: {digit}, ans: {ans}")
	return ans

def best_intToRoman(num: int):
	...

nEx = 3
if __name__ == "__main__":
    import os

    p = os.getcwd() + "/12_Integer_to_Roman/"
    utils.Utils.setup(path=p)
    for _ in range(nEx):
        nums = utils.Utils.read_int(number_split=1)
        output = intToRoman(num=nums)
        print(output)

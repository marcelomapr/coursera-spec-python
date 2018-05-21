import re

#fname = 'regex_sum_42.txt' # test
fname = 'regex_sum_13880.txt' # actual

total = 0

with open(fname) as file:
	for line in file:
		nums = re.findall('[0-9]+', line)
		for num in nums:
			total = total + int(num)

print(total)
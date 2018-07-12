with open('log_dump.txt', 'r') as fp:
	results = fp.readlines()

numbers = []
for idx, r in enumerate(results):
	split_r = r.split(',')[0].split('(')
	name = (''.join(split_r[:-1])).split('\\')[-1].split('.jpg')[0][:-1]
	r_tuple = (idx, name, split_r[-1])
	# print(r_tuple)
	numbers.append(r_tuple)

numbers = sorted(numbers, key=lambda x: x[2])
for x in numbers:
	print(x)
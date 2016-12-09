import sys

def is_reversible(word):
	is_reversible = False
	for i in range(0, len(word)-3):
		new_w = word[i:i+4]

		middle = len(new_w)/2

		if new_w[0] == new_w[1] == new_w[2] == new_w[3]:
			continue

		not_reversible = False
		for i in range(0,middle):
			if new_w[i] != new_w[len(new_w)-1-i]:
				not_reversible = True
				break

		if not_reversible:
			continue

		is_reversible = True

	return is_reversible

def main(arg):
	valid_ip = []
	with open(arg) as f:
		for line in f:
			line = line.replace("\n", "")
			outters = []
			inners = []

			groups = line.split('[')

			for i, group in enumerate(groups):
				if i ==0:
					outters.append(group)
					continue
				sub_group = group.split(']')

				inners.append(sub_group[0])
				outters.append(sub_group[1])

			outter_count = len([i for i in [is_reversible(x) for x in outters] if i == True])
			inner_count = len([i for i in [is_reversible(x) for x in inners] if i == True])

			if inner_count == 0 and outter_count >=1:
				valid_ip.append(line)

	print len(valid_ip)

if __name__ == "__main__":
   main(sys.argv[1])

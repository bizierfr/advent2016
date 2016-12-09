import sys

def is_valid(outters, inners):
	is_valid = False

	combs = []
	for outter in outters:
		for i in range(0, len(outter)-2):
			new_w = outter[i:i+3]

			if new_w[0] == new_w[1] == new_w[2]:
				continue

			if new_w[0] == new_w[2]:
				combs.append(new_w)

	comb_with_eq = []

	for comb in combs:
		new_w = comb[1] + comb[0] + comb[1]

		for inner in inners:
			if new_w in inner:
				comb_with_eq.append(new_w)
	return len(comb_with_eq) >=1

def main(arg):
	valid_ip = []
	with open(arg) as f:
		for line in f:
			line = line.replace("\n", "")
			outters = []
			inners = []

			groups = line.split('[')

			for i, group in enumerate(groups):
				#print group
				if i ==0:
					outters.append(group)
					continue
				sub_group = group.split(']')

				inners.append(sub_group[0])
				outters.append(sub_group[1])

			if is_valid(outters, inners):
				valid_ip.append(line)

	print len(valid_ip)

if __name__ == "__main__":
   main(sys.argv[1])

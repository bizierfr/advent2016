import sys

def main(arg, nb_chars):
	alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u" ,"v" ,"w" ,"x" ,"y" ,"z"]

	positions = []
	for i in range(0,nb_chars):
		positions.append([0]*26)

	with open(arg) as f:
		for line in f:
			line = line.replace("\n", "")
			for i, char in enumerate(line):
				positions[i][alpha.index(char)] += 1

	print positions

	for pos in positions:
		#6-2
		min_ = min([x for x in pos if x != 0])
		print alpha[pos.index(min_)]

		#6-1
		#max_ = max(pos)
		#print alpha[pos.index(max_)]

if __name__ == "__main__":
   main(sys.argv[1], 8)


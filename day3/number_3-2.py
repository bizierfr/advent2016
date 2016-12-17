import sys


def main(arg):
	groups_of_3 = []

	i = 0
	group = []
	with open(arg) as f:
		for line in f:

			coords = []
			for x in line.split("  "):
				if x == "":
					continue
				x = x.replace("\n","")

				print x
				coords.append(int(x))

			print coords

			group.append(coords)

			if i == 2:
				groups_of_3.append(group)
				group = []
				i = 0
			else:
				i = i + 1

		print groups_of_3

	def is_triangle(coords, max_):
		sum_mins = 0;

		equal = 0;
		for coord in coords:
			if coord < max_:
				sum_mins += coord;

			if equal == 0 and coord == max_:
				equal = 1
			elif equal == 1 and coord == max_:
				sum_mins += coord;

		return sum_mins > max_

	triangles = []

	for group in groups_of_3:
		print group

		for i in range(0,3):

			coords = [group[0][i], group[1][i], group[2][i]];
			max_ = max(coords)

			if is_triangle(coords, max_):
				triangles.append(coords)

	print(len(triangles))

if __name__ == "__main__":
   main(sys.argv[1])
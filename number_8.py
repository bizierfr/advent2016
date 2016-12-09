import sys

def main(arg, cols, rows):
	grid = []
	for i in range(0, cols):
		rows_ = []
		for j in range(0 ,rows):
			rows_.append(0)
		grid.append(rows_)

	print grid

	def manage_rect(grid, line):
		coords = line.split(" ")[1].split("x")

		x = int(coords[0])
		y = int(coords[1])

		print "rect " + str(x) + " by " + str(y)

		for i in range(0, x):
			for j in range(0, y):
				print "grid" + str(i) + " " + str(j)
				grid[i][j] = 1

	def manage_col(grid, line):
		coords = line.split("=")[1].split(" by ")

		col_index = int(coords[0])
		by = int(coords[1])

		print "column index " + str(col_index) + " by " + str(by)

		copy_col = []
		for i in range(0, rows):
			copy_col.append(grid[col_index][i])

		for i in range(0, rows):
			swap_index = rows - by + i
			if swap_index >= rows:
				swap_index = swap_index - rows

			grid[col_index][i] = copy_col[swap_index]

	def manage_row(grid, line):
		coords = line.split("=")[1].split(" by ")

		row_index = int(coords[0])
		by = int(coords[1])

		print "row index " + str(row_index) + " by " + str(by)

		copy_row = []
		for i in range(0, cols):
			copy_row.append(grid[i][row_index])

		for i in range(0, cols):
			swap_index = cols - by + i
			if swap_index >= cols:
				swap_index = swap_index - cols

			grid[i][row_index] = copy_row[swap_index]

	with open(arg) as f:
		for line in f:
			line = line.replace("\n", "")

			if "rect" in line:
				manage_rect(grid, line)
			if "column" in line:
				manage_col(grid, line)
			if "row" in line:
				manage_row(grid, line)

			print grid

	sum_ = 0
	for i in range(0, cols):
		sum_ += sum(grid[i])

	print sum_

	for i in reversed(range(0, cols)):
		print "".join(["#" if x == 1 else " " for x in grid[i] ])

if __name__ == "__main__":
   cols = 50
   rows = 6

   main(sys.argv[1], cols, rows)

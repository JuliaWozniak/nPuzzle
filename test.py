




class Puzzle:
	curr = 	[]
	width = 3
	height = 3

	def __init__(self, state):
		self.first_state = state
		self.curr = state
	def move_zero(self, direction):
		i = [x for x in self.curr if 0 in x][0]
		row = self.curr.index(i)
		col = i.index(0)
		

		if direction == Dir.DOWN:
			if row + 1 < self.height:
				self.curr[row][col] = self.curr[row + 1][col]
				self.curr[row + 1][col] = 0
				return 1
		if direction == Dir.UP:
			if row - 1 >= 0:
				self.curr[row][col] = self.curr[row - 1][col]
				self.curr[row - 1][col] = 0
				return 1
		if direction == Dir.RIGHT:
			if col + 1 < self.width:
				self.curr[row][col] = self.curr[row][col+ 1]
				self.curr[row][col+ 1] = 0
				return 1
		if direction == Dir.LEFT:
			if col - 1 >= 0:
				self.curr[row][col] = self.curr[row][col - 1]
				self.curr[row][col - 1] = 0
				return 1
		return 0




















def get_index(puzzle, num):
	for r_index, r in enumerate(puzzle):
		print(r, r_index)
		for c_i, c in enumerate(r):
			if puzzle[r_index][c_i] == num:
				return(r_index, c_i)


def manh_distance(current, goal):

	for n in range(1, 9):
		print(n)
		row, col = get_index(current, n)
		print(n, row, col)


p1 = Puzzle([[1, 2, 3], [0, 5, 6], [7, 8, 4]])
p2 = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

manh_distance(p1.curr, p2.curr)
# n1 = Node(p1)
# n1.describe()

# for dir in [Dir.RIGHT, Dir.LEFT, Dir.UP, Dir.DOWN]:
# 	n1.puzzle.move_zero(dir)
# 	n1.describe()

# print(p1.is_solution())

# a = [[1, 2, 0], [4, 0, 6], [7, 8, 0]]

# x = [x for x in a if 0 in x][0]
# print(a.index(x), x.index(0))
# print(p1.index())
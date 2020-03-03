
class Node():
	def __init__(self,  puzzle, parent=None, dir= None):
		self.parent = parent
		self.puzzle = puzzle
		self.dir = dir

		self.g = 0
		self.h = 0
		self.f = 0

	def describe(self):

		for row in self.puzzle.curr:
			print(row)

	def __eq__(self, other):
		return self.puzzle.curr == other.puzzle.curr

from enum import Enum
class Dir(Enum):
	RIGHT = 1
	LEFT = 2
	UP = 3
	DOWN = 4

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
	for r_i, r in enumerate(puzzle):
		for c_i, c in enumerate(r):
			if puzzle[r_i][c_i] == num:
				return(r_i, c_i)



def manh_distance(current, goal):
	f = 0
	for n in range(1, 9):
		row, col = get_index(current, n)
		g_r = goal[n][0]
		g_c = goal[n][1]
		dy = abs(row - g_r)
		dx = abs(col-g_c)
		f += dy + dx
	return f


def calculate_goal(end_state):
	indices = {}
	for n in range(1,9):
		r, c = get_index(end_state, n)
		indices[n] = (r, c)
	return indices

import copy

def astar(start, end):
	start_node = Node(start)

	end_node = Node(end)
	goal_indices = calculate_goal(end.curr)
	start_node.f = manh_distance(start.curr, goal_indices)
	print(start_node.f)


	open_list = []
	closed_list = []



	open_list.append(start_node)
	start_node.describe()

	while len(open_list) > 0:

		print('/////////////////////')
		print('open  ', len(open_list), 'closed   ', len(closed_list))
		print('/////////////////////')



		current_node = open_list[0]
		current_index = 0
		for index, item in enumerate(open_list):
			if item.f < current_node.f:
				current_node = item
				current_index = index

		open_list.pop(current_index)
		closed_list.append(current_node)

		print('*')
		current_node.describe()
		print('*')

		if current_node == end_node:
			path = []
			current = current_node
			while current is not None:
				path.append(current.dir)
				current = current.parent
			print('HORRAAAY')
			return path[::-1]

		children = []

		print('#######################################')
		for dir in [Dir.RIGHT, Dir.LEFT, Dir.UP, Dir.DOWN]:

			puz = copy.deepcopy(Puzzle(current_node.puzzle.curr))
			if not puz.move_zero(dir):
				continue
			new_node = Node(puz, parent=current_node, dir=dir)
			children.append(new_node)
			

			'''
			into four directions
			'''


		for child in children:
			kost = False
			for closed_child in closed_list:
				if child == closed_child:
					kost = True
			if kost:
				continue
			child.h = manh_distance(child.puzzle.curr, goal_indices)
			child.g = current_node.g + 1
			child.f = child.g + child.h
			child.describe()
			print(child.f)
			

				# Create the f, g, and h values
			
			
		# 	child.g = current_node.g + 1
		# 	child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
		# 	# this will be determined by heuristics

			for open_node in open_list:
				if child == open_node and child.g > open_node.g:
				# if child == open_node:
					continue

			open_list.append(child)
		print('#######################################')




def main():

	start = [[1, 2, 5], [3, 0, 6], [7, 4, 8]]
	end = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
	p1 = Puzzle(start)
	p2 = Puzzle(end)
	
	path = astar(p1, p2)
	print(path)



if __name__ == '__main__':
    main()




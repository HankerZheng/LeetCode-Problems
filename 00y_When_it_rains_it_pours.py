'''
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches. 

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list, computes the total area of standing water accumulated when water is poured from the top and allowed to run off the sides. 

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
'''


def answer(heights):
	# your code here

	def get_rain_drops(lower_wall, higher_wall):
		rain_drops = 0
		if lower_wall[1] < higher_wall[1]:
			for height in heights[lower_wall[1]:higher_wall[1]]:
				rain_drops += lower_wall[0] - height
		else:
			for height in heights[higher_wall[1]+1:lower_wall[1]+1]:
				rain_drops += lower_wall[0] - height
		return rain_drops

	def index_in_range(index, cover_range):
		if index >= cover_range[0] and index <= cover_range[1]:
			return True
		else:
			return False


	if (len(heights) < 3):
		return 0
	#sort the wall
	walls = list()
	for i, item in enumerate(heights):
		walls.append([item,i])
	walls.sort(reverse = True)

	#main loop initializer
	higher_wall = walls[0]
	range_covered = [ walls[0][1] ]
	rain_drops = 0

	#from the highest wall to the lowerest
	for i,lower_wall in enumerate(walls[1:]):
		if len(range_covered) < 2:
			range_covered.append(lower_wall[1])
			range_covered.sort()
			rain_drops += get_rain_drops(lower_wall, higher_wall)
		elif index_in_range(lower_wall[1], range_covered):
			pass
		elif lower_wall[1] < range_covered[0]:
			rain_drops += get_rain_drops(lower_wall, [0, range_covered[0]])
			range_covered[0] = lower_wall[1]
		elif lower_wall[1] > range_covered[1]:
			rain_drops += get_rain_drops(lower_wall, [0, range_covered[1]])
			range_covered[1] = lower_wall[1]
		higher_wall = lower_wall

	return rain_drops






print answer([9,6,1,2,1,6,5,5,4,4,5])

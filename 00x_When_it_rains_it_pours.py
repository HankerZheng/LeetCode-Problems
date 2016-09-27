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
	def mark_the_extreme_max(input_list):
		marked = list()
		trend_old = 0
		for i in range(1,len(input_list)):
			if input_list[i-1] < input_list[i]:
				trend_now = 1
			elif input_list[i-1] == input_list[i]:
				trend_now = trend_old
			else: #input_list[i-1] > input_list[i]
				trend_now = -1
				if trend_old == 1:
					marked.append(i-1)
			trend_old = trend_now
		return marked


	def get_from_left(left, right, items):
		full, rain_drops = items[left], 0
		for i in range(left+1,right):
			if items[i] <= full:
				rain_drops += full - items[i]
			else:
				break
		return rain_drops

	def get_from_right(left, right, items):
		full, rain_drops = items[right], 0
		for i in range(right-1,left,-1):
			if items[i] <= full:
				rain_drops += full - items[i]
			else:
				break
		return rain_drops

#if len < 3, it is impossible to gather water
	if len(heights) <3 :
		return 0
#append start and end so that heights[0] and heights[len-1] could be the extreme numbers
	my_heights = [0] + heights + [0]
#get the markers of the extreme number
	markers = mark_the_extreme_max(my_heights)
	print markers
#if len(markers) < 2, it is impossible to gather water
	if len(markers) <= 1:
		return 0
#main loop to calculate the total water between 2 extreme numbers
	rain_drops = 0
	for i in range(0,len(markers)-1):
		if my_heights[markers[i]] <= my_heights[markers[i+1]]:
			rain_drops += get_from_left(markers[i],markers[i+1], my_heights)
		else:			
			rain_drops += get_from_right(markers[i],markers[i+1], my_heights)
	return rain_drops

print answer([9,7,1,2,1,4,8])
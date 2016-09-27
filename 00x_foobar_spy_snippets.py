
'''
Spy snippets
============

You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known for recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're elbow deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature for the tool called "Snippet Search." While you really wanted to tell him how such a feature is a waste of time in this intense, fast-paced spy organization, you also wouldn't mind getting kudos from a leader. How hard could it be, anyway?

When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a short snippet of the page containing the terms that were searched for. 

Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing all of the given search terms. The search terms can appear in any order.

The length of a snippet is the number of words in the snippet. For example, the length of the snippet "tastiest color of carrot" is 4. (Who doesn't like a delicious snack!)

The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be separated by a single space. A word could appear multiple times in the document.
searchTerms will be a list of words, each word comprised only of lower-case letters [a-z]. All the search terms will be distinct.

Search terms must match words exactly, so "hop" does not match "hopping".

Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello hello where world" and the search terms are ["hello", "world"], you must return "world there hello".

The document will be guaranteed to contain all the search terms.

The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters long. Repeat words in the document are considered distinct for counting purposes.
The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10 letters long.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) document = "many google employees can program"
    (string list) searchTerms = ["google", "program"]
Output:
    (string) "google employees can program"

Inputs:
    (string) document = "a b c d a"
    (string list) searchTerms = ["a", "c", "d"]
Output:
    (string) "c d a"
 '''

import sys, math
import random

def answer(document, searchTerms):
	# your code here

	#given the cali, find the posi (not in chosen_positions) in posi_list having min dist to cali 
	def get_posi_min_to_cali(cali, posi_list, chosen_list):
		min_dis = sys.maxint
		chosen_position = -1
		for posi in posi_list:
			#for each position in posi_list, choose the posi with min distance to cali
			dist = max(chosen_list+[posi]) - min(chosen_list+[posi])
			if dist < min_dis:
				min_dis = dist
				chosen_position = posi
		return chosen_position	


	if len(searchTerms) == 0:
		return []

	search_kw = []
	#pre-process the search terms, prune the repeating terms
	for kw in searchTerms:
		if not kw in search_kw:
			search_kw.append(kw)

	#generate the search_dict, search_dic[keyword_index] = [posi1, posi2, ...]
	word_pool = document.split()
	search_dict = {k:[] for k in range(len(search_kw))}
	for i, word in enumerate(word_pool):
		for j, kw in enumerate(search_kw):
			if kw == word:
				search_dict[j].append(i)
	#set one word as standard, the string of min len containing this word
	#can be found by greedy algorithm -- each other word in the cloest to the standard

	final_choose = []
	min_dis = sys.maxint
	for kw_cali_index in search_dict.keys():
		for posi_cali in search_dict[kw_cali_index]:
			chosen_positions = [posi_cali]
			for kw_index in range(len(search_dict)):
				#for each kw_index, we need to find the posi having min dist to posi_cali
				chosen_position = get_posi_min_to_cali(posi_cali, search_dict[kw_index], chosen_positions)
				if chosen_position == -1:
					#no match found!!
					return []				
				chosen_positions.append(chosen_position)

			start = min(chosen_positions)
			end = max(chosen_positions)
			this_length = end - start
			if  this_length < min_dis:
				min_dis = this_length
				final_choose = [start, end]

	if final_choose == []:
		return []
	else:
		return ' '.join(word_pool[final_choose[0]:final_choose[1]+1])


def right_answer(document, search_terms):
    """Index the position of all search_terms then find the min "score" for a search."""
    index = {k: [] for k in search_terms}
    tokens = document.split()
    for i, token in enumerate(tokens, start=1):
        if token in search_terms:
            index[token].append(i)
    min_score = sys.maxint
    winning_slice = None
    for term in index.keys():  # ignore duplicate terms
        for position in index[term]:
            positions = [position]
            for other_term in index.keys():
                distances = [int(math.fabs(position - x)) for x in index[other_term]]
                positions.append(index[other_term][distances.index(min(distances))])
            score = max(positions) - min(positions) + 1
            if score < min_score:
                winning_slice = (min(positions) - 1, max(positions),)
                min_score = score
    return " ".join(tokens[slice(*winning_slice)])



right = []
my = []
while len(right) == len(my):
	input_str = [random.choice(['a','b','c','d','e']) for i in range(20)]
	input_str = ' '.join(input_str)
	try:
		right = right_answer(input_str, ['a','b','c','d'])
		my = answer(input_str, ['a','b','c','d'])
	except:
		continue

print input_str
print '    my answer is %s' % answer(input_str, ['a','b','c','d'])
print ' right answer is %s' % right_answer(input_str, ['a','b','c','d'])
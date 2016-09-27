
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
#pre-processing
	if len(searchTerms) == 0:
		return []
	search_kw = []
	#pre-process the search terms, prune the repeating terms
	for kw in searchTerms:
		if not kw in search_kw:
			search_kw.append(kw)
	#generate the search_arrays, search_dic[keyword_index] = [posi1, posi2, ...]
	word_pool = document.split()
	search_arrays = [[] for k in range(len(search_kw))]
	for i, word in enumerate(word_pool):
		for j, kw in enumerate(search_kw):
			if kw == word:
				search_arrays[j].append(i)
	if [] in search_arrays:
		#keyword doesn't match, return []
		return []
#choose the smallest as the cali array. note: arrays are given in the sorted way
	final_choices = []
	cali_array = [0 for x in range(len(search_arrays))]
	while 1:
		try:
			choices = [search_arrays[i][item] for i, item in enumerate(cali_array)]
		except:
			break
		min_posi, max_posi = min(choices),max(choices)
		final_choices.append([abs(min_posi - max_posi), min_posi, max_posi])	#[len, start, end]
		array_index_for_min_posi = choices.index(min_posi)
		cali_array[array_index_for_min_posi] += 1
	result = min(final_choices)
	return ' '.join(word_pool[result[1]:result[2]+1])




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


#for 1000 sample, average number of attempts before a dismatch is 919 
statistics = []
for i in range(10):
	right = []
	my = []
	count = 0
	while len(right) == len(my):
		count += 1
		input_str = [random.choice(['a','b','c','d','e']) for i in range(20)]
		input_str = ' '.join(input_str)
		try:
			right = right_answer(input_str, ['a','b','c','d'])
			my = answer(input_str, ['a','b','c','d'])
		except:
			continue
	statistics.append(count)
print statistics

print input_str
print '    my answer is %s' % answer(input_str, ['a','b','c','d'])
print ' right answer is %s' % right_answer(input_str, ['a','b','c','d'])
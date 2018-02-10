#!/usr/bin/python

import sys

# reducer function
def wordsReducer(data):
	current = None
	counter = 1

	# for a line in data
	for aLine in data:
		aWord, acc = aLine.strip().lower().split('t')
		# if current word not None
		if current:
			# if current word is same as a word
			if current == aWord:
				counter += acc
			else:
				# add word and counter to result list
				res.append((current, counter))
				counter = 1
		# change current word
		current = aWord
	# if counter not equal to 1
	if counter > 1:
		# add word and counter to result list
		res.append((current, counter))
	return res

# function call
wordsReducer(sys.stdin)
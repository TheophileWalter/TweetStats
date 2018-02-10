#!/usr/bin/python
import sys

# mapper function
def wordsMapper(data):
	res = []
	# for a line in data
	for aLine in data:
		# for a word in a line
		for aWord in aLine.strip().lower().split():
			# append word and counter set un result list
			res.append((aWord, 1))
	return res

# function call
wordsMapper(sys.stdin)
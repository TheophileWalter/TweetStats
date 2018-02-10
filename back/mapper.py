# Data source
data = "to to tO ta Ta ta\
        ti tI ti to to % ! "

# function mapper
def mapper(data):
	# result
	res =[]
	# to lower case and split into words list
	words = data.lower().split()
	# append 1 to each word
	[res.append((word, 1)) for word in words]
	# return result
	return res

print (mapper(data))
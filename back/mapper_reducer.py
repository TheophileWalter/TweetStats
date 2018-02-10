# data source
data = sc.textFile("file:///home/alexis/Documents/toto.txt")

# mapper and reducer to get word frequency
mapperReducer = data.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

# data output saving
mapperReducer.saveAsTextFile("file:///home/alexis/Documents/tata.txt")
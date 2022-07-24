#Using the built-in method to implement a queue

from queue import Queue
def queue_():
	#intialising
	q = Queue(maxsize = 5)
	
	#qsize is the number of max item allowed
	print(q.qsize())

	#adding items 
	q.put(1)
	q.put(2)
	q.put(3)

	#Return queue if full
	print(q.full())

	#Removing elements
	print(q.get())
	print(q.get())
	print(q.get())

	#Return boolean if empty
	print(q.empty())
	
	q.put(1)

	print(q.empty())
	print(q.full())



queue_()
#There are many types of ways to create stacks in python

def common_way():
	mystack = []
	#Appending is like pushing an item into a stack
	mystack.append(1)
	mystack.append(2)
	mystack.append(3)

	print(mystack)
	mystack.pop()
	mystack.pop()
	mystack.pop()
	
'''With the list approach ^, there are a few issues: for example it can run into speed/retreival issues as the size 
increases. If the list gets bigger than the block of memory, then appending items to the stack will take longer. 

Using 'collection.deque' will help you get around the reallocation memory problem
'''

#Deque -> "deck" -> "double-ended queue"
from collections import deque
def efficient_way():
	mystack = deque()
	mystack.append(1)
	mystack.append(2)
	mystack.append(3)
	print(mystack)
	mystack.pop()
	mystack.pop()
	mystack.pop() 

'''The reason behind using both approaches is different. With using a list, if the block of allocated memory is full, and after pushing a item into the stack, the computer will need to get another block, which will take longer for ".append()"
Whereas with a "deque", it uses a linked list data structure. Each entry of the item is stored in its own memory block, and has a reference pointing to the next item in the list. Each entry has references pointing to the previous and next item in the linked list.
'''
 

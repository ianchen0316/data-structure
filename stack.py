from abc import ABCMeta, abstractmethod 

#TODO: Add docs for stack methods 
#TODO: Add expand if stack overflows 
#TODO: Add test cases 
#TODO: Combine with CICD on AWS 


class AbstractStack(metaclass=ABCMeta): 

	""" API for Stack Data Structure """

	@abstractmethod
	def push(self, val): 
		pass 

	@abstractmethod
	def pop(self): 
		pass 

	@abstractmethod
	def top(self): 
		pass 

	@abstractmethod
	def is_empty(self): 
		pass 

	@abstractmethod
	def __len__(self): 
		pass 


class ArrayStack(AbstractStack): 

	def __init__(self, capacity=10):

		self._array = [None] * capacity 
		self._top = -1  # index of top element (-1: no element yet)

	def push(self, val): 

		self._top += 1 
		self._array[self._top] = val 

	def pop(self): 

		if self.is_empty(): 
			raise IndexError("Stack is empty")
		val = self._array[self._top]
		self._top -= 1 
		return val 

	def top(self): 

		if self.is_empty():
			raise IndexError("Stack is empty")
		return self._array[self._top]

	def is_empty(self): 

		return self._top == -1 

	def __len__(self): 

		return self._top + 1 











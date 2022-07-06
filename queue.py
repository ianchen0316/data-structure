from abc import ABCMeta, abstractmethod 

#TODO: add API documentation 
#TODO: solve front/back_next modulus problem
#TODO: add array expansion 

class AbstractQueue(metaclass=ABCMeta): 

	@abstractmethod
	def enqueue(self, val): 

		pass 

	@abstractmethod
	def dequeue(self): 

		pass 

	@abstractmethod
	def front(self): 

		pass 

	@abstractmethod
	def is_empty(self): 

		pass 

	@abstractmethod
	def __len__(self): 

		pass


class CircularArrayQueue(AbstractQueue): 


	def __init__(self, capacity=10):

		self._array = [None]*capacity 
		self._front = 0
		self._back_next = 0
		self._size = 0 

	def enqueue(self, val): 

		self._array[self._back_next] = val 
		self._back_next += 1 
		self._size += 1

	def dequeue(self): 

		if self.is_empty(): 
			raise IndexError("Queue is empty")

		val = self._array[self._front]
		self._array[self._front] = None 
		self._front += 1
		self._size -= 1 

		return val 

	def front(self): 

		if self.is_empty(): 
			raise IndexError("Queue is empty")

		return self._array[self._front]

	def is_empty(self): 

		return self._size == 0 

	def __len__(self): 

		return self._size 






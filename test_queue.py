"""
Unit tests for queue 

"""

from queue import CircularArrayQueue 


class TestQueue: 

	def test_normal_case1(self): 

		q = CircularArrayQueue(capacity=10)
		q.enqueue(1)
		q.enqueue(2)
		q.enqueue(3)

		# test __len__: 
		assert len(q) == 3 

		# test is_empty(): 
		assert q.is_empty() == False 

		# test front(): 
		val = q.front() 
		assert val == 1 

		# test dequeue(): 
		val = q.dequeue() 
		assert val == 1 
		assert len(q) == 2 
		assert q.front() == 2 

	def test_underflow1(self): 

		pass 

	def test_overflow1(self): 

		pass 

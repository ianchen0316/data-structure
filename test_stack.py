""" Unit Tests for Stack """

from stack import ArrayStack 


class TestArrayStack: 

	def test_normal_case1(self): 

		""" Normal Operation 1 """

		s = ArrayStack(capacity=10)

		s.push(1)
		s.push(2)
		s.push(3) 

		# test __len__: 
		assert len(s) == 3

		# test is_empty(): 
		assert s.is_empty() == False 

		# test top(): 
		assert s.top() == 3 

		# test pop(): 
		assert s.pop() == 3 
		assert len(s) == 2    # stack length after pop
		assert s.top() == 2   # top of stack after pop


	def test_underflow1(self): 

		""" Stack Underflow """

		pass 


	def test_overflow1(self): 

		pass 
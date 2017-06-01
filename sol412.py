




412. Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.


key points:


	module calculation.





class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""

		if n==0:
			return []

		ans=[]

		for i in range(1,n+1):
			tmp=""

			if i%3==0:
				tmp+="Fizz"
			if i%5==0:
				tmp+="Buzz"

			if len(tmp)==0: 
				tmp=str(i)

			ans.append(tmp)

		return ans
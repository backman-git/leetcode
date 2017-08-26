
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


key point:

	bin(), int(,2)




class Solution(object):

	def flip(self,strs):
		res=""
		for c in strs:
			if c =='1':
				res+='0'
			else:
				res+='1'
		return res

	def flip2(self,strs):

		return ''.join(['1' if x=='0' else '0' for x in strs])

	def findComplement(self, num):
		"""
		:type num: int
		:rtype: int
		"""

		numBit=bin(num)[2:]

		numBitComplement = self.flip(numBit)

		return int(numBitComplement,2)

sol =Solution()

print sol.findComplement(5)
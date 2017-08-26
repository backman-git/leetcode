The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.


Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

key points:
	
	1. ^ operation  is XOR


	python bin() and count()



class Solution(object):
	def hammingDistance(self, x, y):
		return bin(x^y).count("1")



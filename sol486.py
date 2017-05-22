
486. Predict the Winner






Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.




key points:

	
	1. min max algorithm appear at math function

	2. 


	P.S. 重點複習




class Solution(object):
	

	def PredictTheWinner(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		
		dp={}


		def point(nums):

			if len(nums)==0:
				return 0

			if len(nums) ==1:
				return nums[0]

			if len(nums)==2:
				return max(nums[0],nums[1])

			if nums in dp:
				return dp[nums]


			dp[nums]=max(nums[0] - point(nums[1:]),nums[-1]-point(nums[:-1])  )

			return dp[nums]

		nums=tuple(nums)

		return point(nums)>=0






sol = Solution()


print sol.PredictTheWinner([1,5,233,7])       





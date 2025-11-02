'''
A playful child is climbing a staircase with n steps. At each move, the child can press a “button” in their imagination — choosing to climb either 1 step or 2 steps. 
The child wonders: “How many different ways can I reach the top of the staircase?”
Task
Write a program to calculate the number of unique ways the child can climb to the top.
'''

class Solution:
	def climbStairs(self, n: int) -> int:
 		# TODO: implement the logic to calculate the number of unique ways to climb n steps
 		if n == 1 or n == 0:
 		    return 1 
 		dp = [0] * (n+1)
 		
 		dp[0], dp[1] = 1, 1 
 		
 		for i in range(2, n+1):
 		    dp[i] = dp[i-1] + dp[i-2]
 		    
 		return dp[n]

if __name__ == "__main__":
	solution = Solution()
	print(solution.climbStairs(3))	# Expected: 3
	print(solution.climbStairs(4))	# Expected: 5
	print(solution.climbStairs(0))	# Expected: 1

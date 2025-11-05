'''
Deep in the crypt of Skeletal Caverns, a greedy skeleton king has left behind a hoard of enchanted bones. Each bone has two attributes: a weight (how heavy it is) and a magical value (how powerful it is). 
The adventurer must collect bones without exceeding their carrying capacity, while maximizing the total magical value. Important: Each bone can be picked at most once.
How to Think About It
For each bone, the adventurer has a choice: take it (if the weight fits in the bag) or leave it and move on. The best solution comes from exploring both choices for every bone and keeping the maximum value. 
This can be done efficiently using dynamic programming instead of brute force.
Task
Write a program that determines the maximum magical value the adventurer can collect without exceeding capacity.
'''

class Solution:
	def knapSack(self, weights: list[int], values: list[int], capacity: int) -> int:
 		# TODO: implement 0/1 knapsack to maximize total value without exceeding capacity
 		# Each item can be picked at most once
 		# Return the maximum possible value
 		n = len(weights)
 		dp = [[0]*(capacity+1) for _ in range(n+1)]
 		
 		for i in range(1, n+1):
 		    for w in range(capacity+1):
 		        if weights[i-1] <= w:
 		            dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
 		        else:
 		            dp[i][w] = dp[i-1][w]
 		return dp[n][capacity]

if __name__ == "__main__":
	solution = Solution()
	print(solution.knapSack([2,3,4,5], [3,4,5,6], 5))	# Expected: 7
	print(solution.knapSack([1,2,3], [10,15,40], 6))	# Expected: 65

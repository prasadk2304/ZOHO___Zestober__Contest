'''
At a bustling marketplace, you are working as a cashier. Customers pay with large bills, and it’s your job to make the best deal by returning the exact change using the fewest coins possible. You have an infinite supply of coins in certain denominations (given in an array). If the target amount can be formed, return the minimum number of coins needed. If it’s impossible, return -1.
Task
Write a program to compute the minimum number of coins required to make up a given target amount.
'''
class Solution:
	def coinChange(self, coins: list[int], amount: int) -> int:
 		# TODO: implement the logic to compute the minimum number of coins to make up the target amount
 		dp = [float('inf')] * (amount + 1)
 		dp[0] = 0
 		
 		for coin in coins:
 		    for i in range(coin, amount+1):
 		            dp[i] = min(dp[i], dp[i - coin] + 1)
 		          
 		return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
	solution = Solution()
	print(solution.coinChange([1, 2, 5], 11))	# Expected: 3
	print(solution.coinChange([2], 3))	# Expected: -1
	print(solution.coinChange([1, 4, 5], 13))	# Expected: 3

'''
A logger is cutting down a massive tree trunk into equal sections. After cutting, he carefully stacks the sections one by one. But to keep the stack stable and safe, he must split the trunk into two groups of sections such that both groups have the same total weight.
Task
Write a program to determine if the given array of section weights can be partitioned into two subsets with equal sum.
'''

class Solution:
	def canSplitEqually(self, sections: list[int]) -> bool:
 		# TODO: implement the logic to check if the array can be partitioned into two subsets with equal sum
 		total = sum(sections)
 		
 		if total % 2 != 0:
 		    return False
 		target = total // 2
 		n = len(sections)
 		dp = [False] * (target + 1)
 		dp[0] = True
 		for num in sections:
 		    for i in range(target, num - 1, -1):
 		        dp[i] = dp[i] or dp[i - num]
 		        
 		return dp[target]

if __name__ == "__main__":
	solution = Solution()
	print(solution.canSplitEqually([1, 5, 11, 5]))	# Expected: True
	print(solution.canSplitEqually([1, 2, 3, 5]))	# Expected: False

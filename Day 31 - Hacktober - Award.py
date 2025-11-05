'''
At the Grand Academy, students compete for the Golden Award. To win, a student must collect badges from different contests. 
Each contest gives a badge with a certain score. The student wants to collect badges such that the total score is at least K. The student can skip contests, but once skipped, cannot go back.
Task
Write a program to find the minimum number of badges needed to reach at least score K. If it’s impossible to reach K, return -1.
'''

class Solution:
	def minBadges(self, badges: list[int], K: int) -> int:
 		# TODO: find the minimum number of badges needed to reach at least K total score
 		# - You can pick badges in any order
 		# - If total sum of all badges < K, return -1
 		# - Otherwise, minimize the number of badges used
 		if sum(badges) < K:
 		    return -1
 		    
 		badges.sort(reverse = True)
 		total = 0
 		count = 0 
 		
 		for score in badges:
 		    total += score
 		    count += 1
 		    if total >= K:
 		        return count
 		return -1

if __name__ == "__main__":
	solution = Solution()
	print(solution.minBadges([5,2,3,7,1], 8))	# Expected: 2
	print(solution.minBadges([1,1,1,1,1], 4))	# Expected: 4
	print(solution.minBadges([2,3,4], 15))	# Expected: -1

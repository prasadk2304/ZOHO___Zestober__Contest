'''
In a long corridor of rooms, each room has a cleanliness score represented by numbers in an array. A positive number means the room is clean. A negative number means the room is dirty. A zero means the room is average. The janitor wants to impress the inspectors by choosing a stretch of consecutive rooms that looks the best. The score of this stretch is the sum of the cleanliness scores of those rooms. Your job is to find the highest possible total cleanliness score among all such consecutive stretches.
Task
Given an integer array rooms, find the maximum sum of cleanliness scores among all contiguous subarrays (consecutive rooms).
'''
class Solution:
	def maxCleanlinessScore(self, rooms: list[int]) -> int:
 		# TODO: implement the logic to find the maximum total cleanliness score among all contiguous subarrays
 		maxsum = rooms[0]
 		currsum = rooms[0]
 		
 		for i in range(1, len(rooms)):
 		    currsum = max(rooms[i], currsum + rooms[i])
 		    maxsum = max(maxsum, currsum)
 		    
 		return maxsum

if __name__ == "__main__":
	solution = Solution()
	print(solution.maxCleanlinessScore([3, -2, 5, -1]))	# Expected: 6
	print(solution.maxCleanlinessScore([-1, -2, -3]))	# Expected: -1
	print(solution.maxCleanlinessScore([4, -1, 2, -2, 3, -5, 4]))	# Expected: 6

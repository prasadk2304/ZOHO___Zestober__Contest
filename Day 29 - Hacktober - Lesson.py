'''
At the Academy of Lessons, teachers must schedule classes in a single classroom. Each class has a start time and an end time. To avoid conflicts, no two classes can overlap in time. 
The academy wants to know the maximum number of classes that can fit into the schedule without overlapping.
Task
Write a program to determine the maximum number of non-overlapping classes that can be scheduled.
'''

class Solution:
	def maxClasses(self, classes: list[list[int]]) -> int:
 		# TODO: implement the logic to find the maximum number of non-overlapping intervals
 		# Sort by end time and use a greedy approach to select compatible classes
 		classes.sort(key = lambda x:x[1])
 		count = 0 
 		lastend = 0 
 		
 		for start, end in classes:
 		    if start >= lastend:
 		        count += 1 
 		        lastend = end
 		return count

if __name__ == "__main__":
	solution = Solution()
	print(solution.maxClasses([[1,3],[2,5],[4,6]]))	# Expected: 2
	print(solution.maxClasses([[7,9],[1,2],[3,4],[5,6]]))	# Expected: 4
	print(solution.maxClasses([[1,10],[2,3],[4,5],[6,7],[8,9]]))	# Expected: 4

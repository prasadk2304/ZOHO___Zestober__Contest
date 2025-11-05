'''
In the city of Inferno, multiple fires have broken out across districts. The mayor wants to map out the continuous periods when the city was ablaze. 
Some fires overlap in time, and multiple overlapping fires are considered as a single continuous blaze. Your task is to merge all overlapping fire intervals into a list of continuous burning periods.
Task
Write a program that merges overlapping intervals.
'''
class Solution:
	def mergeFires(self, fires: list[list[int]]) -> list[list[int]]:
 		# TODO: implement the logic to merge all overlapping intervals into continuous blaze periods
 		if not fires:
 		    return []
 		
 		fires.sort(key=lambda x:x[0])
 		merged = [fires[0]]
 		
 		for current in fires[1:]:
 		    last = merged[-1]
 		    if current[0] <= last[1]:
 		        last[1] = max(last[1], current[1])
 		    else:
 		        merged.append(current)
 		return merged

if __name__ == "__main__":
	solution = Solution()
	print(solution.mergeFires([[1,3],[2,5],[6,8],[7,9]]))	# Expected: [[1,5], [6,9]]
	print(solution.mergeFires([[1,4],[5,6],[7,8]]))	# Expected: [[1,4], [5,6], [7,8]]
	print(solution.mergeFires([[1,10],[2,6],[3,5],[7,9]]))	# Expected: [[1,10]]

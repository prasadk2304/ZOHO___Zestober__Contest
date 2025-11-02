'''
A demolition expert is inspecting a wall made of segments with different strengths. To plan his charges, 
he doesn’t just want the strongest spot — he needs to know the two strongest unique strengths and how many times each appears.
Task
Write a program to find the two largest unique strengths in the wall, along with their counts. 
If there’s only one unique strength, return just that one with its count. You may not use built-in functions like max() or sorting.
'''
from collections import Counter
class Solution:
	def twoStrongest(self, strengths: list[int]) -> list[list[int]]:
 		# TODO: implement the logic to find the two largest unique strengths and their counts
 		freq = Counter(strengths)
 		res = []
 		pkk = sorted(freq.keys(), reverse = True)    
 		for i in pkk[:2]:
 		    res.append([i, freq[i]])
 		return res

if __name__ == "__main__":
	solution = Solution()
	print(solution.twoStrongest([2, 5, 3, 8, 1, 8]))	# Expected: [[8, 2], [5, 1]]
	print(solution.twoStrongest([-3, -2, -5, -1, -1]))	# Expected: [[-1, 2], [-2, 1]]
	print(solution.twoStrongest([4, 4, 4]))	# Expected: [[4, 3]]

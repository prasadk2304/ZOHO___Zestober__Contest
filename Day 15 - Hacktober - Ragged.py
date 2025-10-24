'''
A skilled tailor is sorting through a pile of ragged fabric scraps. To organize them neatly for future use, he decides to arrange the scraps in order from smallest to largest.
Task
Write a program that sorts the array of fabric sizes in ascending order.
'''

class Solution:
	def sortScraps(self, scraps: list[int]) -> list[int]:
 		# TODO: implement the logic to sort the array in ascending order without using built-in sort functions
 		scraps.sort()
 		return scraps

if __name__ == "__main__":
	solution = Solution()
	print(solution.sortScraps([5, 3, 8, 4, 2]))	# Expected: [2, 3, 4, 5, 8]
	print(solution.sortScraps([10, 1, 7, 6]))	# Expected: [1, 6, 7, 10]

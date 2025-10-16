'''
In a busy warehouse, the manager keeps track of crates arranged in a single line. Each crate has a specific weight, represented by numbers in an array. To make loading and unloading easier, the manager wants to quickly identify the heaviest crate. If there are multiple crates tied for the heaviest weight, the manager will always choose the first one in line.
Task
Write a program that finds the index of the heaviest crate in the array.
'''
class Solution:
	def findHeaviestCrate(self, crates: list[int]) -> int:
 		# TODO: implement the logic to find the index of the heaviest crate (first occurrence if tied)
 		maxwight = max(crates)
 		
 		return crates.index(maxwight)

if __name__ == "__main__":
	solution = Solution()
	print(solution.findHeaviestCrate([50, 75, 20, 75, 60]))	# Expected: 1
	print(solution.findHeaviestCrate([10, 20, 30, 40, 50]))	# Expected: 4

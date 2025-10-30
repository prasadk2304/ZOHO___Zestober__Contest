'''
A skilled jeweler is examining two ornate collections of gems. Some gems appear in both collections, while others remain unique. But the jeweler is very precise — he not only wants the common gems but also wants them listed in sorted order without duplicates.
Task
Write a program to find the unique gems that appear in both collections and return them sorted in ascending order.
'''
class Solution:
	def findCommonGems(self, collection1: list[int], collection2: list[int]) -> list[int]:
 		# TODO: implement the logic to find unique gems appearing in both collections, sorted in ascending order
 		common  = set(collection1) & set(collection2)
 		
 		return sorted(common)

if __name__ == "__main__":
	solution = Solution()
	print(solution.findCommonGems([1, 2, 3, 4], [3, 4, 5, 6]))	# Expected: [3, 4]
	print(solution.findCommonGems([7, 8, 9], [10, 11, 12]))	# Expected: []
	print(solution.findCommonGems([4, 1, 2, 2, 3], [3, 4, 4, 5]))	# Expected: [3, 4]

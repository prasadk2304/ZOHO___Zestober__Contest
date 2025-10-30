'''
Two rival chefs are preparing for a cooking contest. As they compare their ingredient lists, they notice that some ingredients are anagrams of each other — same letters, just in a different order. To settle their rivalry, they want to group all such ingredients together.
Task
Write a program to group all ingredients that are anagrams into separate lists.
'''
from collections import defaultdict
class Solution:
	def groupAnagrams(self, ingredients: list[str]) -> list[list[str]]:
 		# TODO: implement the logic to group all anagrams together
 		ag = defaultdict(list)
 		for word in ingredients:
 		    key = ''.join(sorted(word))
 		    ag[key].append(word)
 		return list(ag.values())

if __name__ == "__main__":
	solution = Solution()
	print(solution.groupAnagrams(["salt", "tals", "pepper", "prepep", "sugar"]))	# Expected: [['salt','tals'], ['pepper','prepep'], ['sugar']]
	print(solution.groupAnagrams(["egg", "gge", "garlic"]))	# Expected: [['egg','gge'], ['garlic']]

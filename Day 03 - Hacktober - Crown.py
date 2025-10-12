'''
In a magical land where words carried mystical power, the prestigious Crown Words were honored with a regal sequence of letters. According to legend, only words that start and end with the same letter could earn the title of Crown Word.
Task - Given an array of strings, count how many words qualify as Crown Words.
'''
class Solution:
	def countCrownWords(self, words: list[str]) -> int:
		# TODO: implement the logic to count Crown Words 
		    count = 0
		    for word in words:
		            if word[0] == word[-1]:
		                   count += 1
		    return count

if __name__ == "__main__":
	solution = Solution()
	print(solution.countCrownWords(["apple", "civic", "crown", "aba"]))    
	# Expected: 2

	print(solution.countCrownWords(["noon", "level", "moon", "night", "racecar"]))  
	# Expected: 3

	print(solution.countCrownWords(["a", "b", "c", "aa", "bb", "ab"]))  
	# Expected: 5

'''
In the land of Alphabeta, a magical string s held a curious mix of lowercase and uppercase letters. Among them were the murky letters — the lonely ones that appeared only once.
Task - Given a string s, count the number of letters that appear exactly once. Treat uppercase and lowercase letters as the same. '''

class Solution:
	def countMurkyLetters(self, s: str) -> int:
		# TODO: implement the logic to count murky letters
            count = 0
            for ch in s:
                    if s.count(ch) == 1:
            		        count += 1
            return count

if __name__ == "__main__":
	solution = Solution()
	print(solution.countMurkyLetters("murky")) # Expected: 5
	print(solution.countMurkyLetters("murmur")) # Expected: 0
	print(solution.countMurkyLetters("AlphaBeta")) # Expected: 6

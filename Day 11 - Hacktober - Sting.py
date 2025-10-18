'''
A diligent beekeeper is studying the movement of bees inside a hive. Each bee’s journey is recorded as a sequence of characters, representing their path. To better understand their behaviour, the beekeeper wants to know how many times a specific path pattern occurs in the recorded sequence. If the same pattern overlaps, those occurrences should also be counted. If the pattern doesn’t appear at all, the result should be 0.
Task - Given a string paths and another string pattern, count how many times pattern occurs inside paths.
'''
class Solution:
	def countPatternOccurrences(self, paths: str, pattern: str) -> int:
 		# TODO: implement the logic to count how many times pattern occurs in paths (including overlapping)
 		count = 0 
 		m = len(pattern)
 		for i in range(len(paths) - m + 1):
 		    if paths[i:m+i] == pattern:
 		        count += 1
 		return count

if __name__ == "__main__":
	solution = Solution()
	print(solution.countPatternOccurrences("ABACABA", "ABA"))	# Expected: 2
	print(solution.countPatternOccurrences("AAAAA", "AA"))	# Expected: 4
	print(solution.countPatternOccurrences("XYZ", "A"))	# Expected: 0

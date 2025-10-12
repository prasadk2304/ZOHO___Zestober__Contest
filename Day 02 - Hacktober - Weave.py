'''In a quiet town, two mystical threads, s1 and s2, awaited a weaver to combine them. The artisan’s task was simple yet elegant: weave the strings by alternating their characters. 
If one thread was longer, its remaining part would be added at the end.
Task - Write a program that weaves two strings together by alternating their characters. If one string is longer, append the extra characters to the end. '''

class Solution:
	def weaveStrings(self, s1: str, s2: str) -> str:
		# TODO: implement the logic to weave two strings pass
		    result = []
		    minlen = min(len(s1), len(s2))
		    
		    for i in range(minlen):
		            result.append(s1[i])
		            result.append(s2[i])
		    
		    result.append(s1[minlen:])
		    result.append(s2[minlen:])
		    
		    return ''.join(result)

if __name__ == "__main__":
	solution = Solution()
	print(solution.weaveStrings("abc", "pqr"))     # Expected: "apbqcr"
	print(solution.weaveStrings("ab", "pqrs"))     # Expected: "apbqrs"
	print(solution.weaveStrings("abcd", "xy"))     # Expected: "axbycd"

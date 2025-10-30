'''
A researcher is studying ice core layers deep in the Arctic. Some layers repeat in sequence, while others form patterns that mirror themselves. The researcher wants to identify the longest sequence of layers that reads the same forward and backward — in other words, the longest palindromic substring in the given string of ice layers.
Task
Write a program to find the longest palindromic substring in the given string. If multiple substrings of the same maximum length exist, return the one that appears first.
'''
class Solution:
	def longestPalSubstring(self, layers: str) -> str:
 		# TODO: implement the logic to find the longest palindromic substring (return the first if multiple)
 		maxlen = 0
 		start = 0
 		
 		for i in range(len(layers)):
 		    for j in range(i, len(layers)):
 		        sub = layers[i:j+1]
 		        if sub == sub[::-1] and len(sub) > maxlen:
 		            maxlen = len(sub)
 		            start = i
 		return layers[start:start+maxlen]

if __name__ == "__main__":
	solution = Solution()
	print(solution.longestPalSubstring("abccba"))	# Expected: "abccba"
	print(solution.longestPalSubstring("babad"))	# Expected: "bab"

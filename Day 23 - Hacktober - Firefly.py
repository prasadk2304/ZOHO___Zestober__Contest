'''
In a quiet meadow at night, fireflies glow in a magical sequence. The brightness of each firefly depends on the sum of the brightness of the previous two fireflies. 
The first two fireflies always shine with a brightness of 1 (unless otherwise specified). The naturalist studying the meadow realizes that this sequence is not random at all — it is the famous Fibonacci sequence. 
Your task is to calculate the brightness of the nth firefly.
Task
Write a program to calculate the brightness of the nth firefly, which follows the Fibonacci pattern.
'''

class Solution:
	def fireflyBrightness(self, n: int) -> int:
 		# TODO: implement the logic to calculate the brightness of the nth firefly (Fibonacci sequence)
 		a, b = 1, 1
 		for _ in range(3, n+1):
 		    a, b = b, a+b 
 		return b

if __name__ == "__main__":
	solution = Solution()
	print(solution.fireflyBrightness(5))	# Expected: 5
	print(solution.fireflyBrightness(7))	# Expected: 13

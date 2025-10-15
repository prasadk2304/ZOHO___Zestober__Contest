'''
In a thrilling stunt show, a fearless driver performs a breathtaking series of jumps. Each jump has a specific height, represented by a number in an array. To add suspense and excitement, the stunt driver decides to perform the jumps in reverse order — beginning with the last jump and finishing with the very first one.
Task
Write a program to reverse the array of jump heights in-place, without using any built-in reverse functions.
'''

class Solution:
	def reverseJumps(self, jumps: list[int]) -> list[int]:
 		# TODO: implement the logic to return the reversed array without using built-in reverse
            n = len(jumps)
            res = []
            for i in range(n-1, -1, -1):
                res.append(jumps[i])
            return res

if __name__ == "__main__":
	solution = Solution()
	print(solution.reverseJumps([3, 5, 2, 8, 6]))	# Expected: [6, 8, 2, 5, 3]
	print(solution.reverseJumps([1, 2, 3]))	# Expected: [3, 2, 1]

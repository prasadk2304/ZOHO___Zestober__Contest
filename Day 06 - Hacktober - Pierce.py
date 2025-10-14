'''
A skilled blacksmith is crafting a circular blade. Around the edge of the blade, he carefully marks n notches, each at equal distance. These notches are represented as numbers arranged in a circular sequence. To test the durability and symmetry of his blade, he wants to rotate the notches clockwise by k positions. Since the blade is circular, if the rotation count k is greater than n, the notches will simply wrap around.
Task - Given an array arr of length n and an integer k, rotate the array clockwise by k positions and return the result.
'''

class Solution:
	def rotateClockwise(self, arr: list[int], k: int) -> list[int]:
		# TODO: implement the logic to rotate array clockwise by k positions
		    n = len(arr)
		    k = k % n 
		    
		    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
	solution = Solution()
	print(solution.rotateClockwise([1, 2, 3, 4, 5], 2))         # Expected: [4, 5, 1, 2, 3]
	print(solution.rotateClockwise([10, 20, 30, 40], 6))        # Expected: [30, 40, 10, 20]

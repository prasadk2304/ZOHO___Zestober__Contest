'''
A careless architect made a blunder while designing a temple floor. The floor is a square grid, but the two diagonals don’t balance. To evaluate the mistake, the architect needs to know the absolute difference between the sums of the primary diagonal (top-left to bottom-right) and the secondary diagonal (top-right to bottom-left).
Task
Write a program to calculate the absolute difference between the sums of the two diagonals of a square matrix.
'''

class Solution:
	def diagonalDifference(self, grid: list[list[int]]) -> int:
 		# TODO: implement the logic to calculate the absolute difference between primary and secondary diagonal sums
 		n = len(grid)
 		p_sum = 0 
 		s_sum = 0 
 		
 		for i in range(n):
 		    p_sum += grid[i][i]
 		    s_sum += grid[i][n-1-i]
 		    
 		return abs(p_sum - s_sum)

if __name__ == "__main__":
	solution = Solution()
	grid1 = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	print(solution.diagonalDifference(grid1))	# Expected: 0

	grid2 = [
		[11, 2, 4],
		[4, 5, 6],
		[10, 8, -12]
	]
	print(solution.diagonalDifference(grid2))	# Expected: 15

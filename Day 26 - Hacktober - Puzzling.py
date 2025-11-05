'''
In the archives of the Puzzling Society, you discover an ancient Sudoku board. Some cells are filled with numbers 1–9, while others are empty. To unlock its secrets, 
you must check if the Sudoku board is valid so far: each row must not contain duplicates (ignoring empty cells), each column must not contain duplicates, and each 3×3 sub-grid must not contain duplicates.
Task
Write a program that checks whether the given Sudoku board is valid.
'''
class Solution:
	def isValidSudoku(self, board: list[list[int]]) -> bool:
 		# TODO: check rows, columns, and 3x3 sub-grids for duplicates (ignore zeros)
 		def hasduplicates(nums):
 		    seen = set()
 		    for num in nums:
 		        if num != 0:
 		            if num in seen:
 		                return True
 		            seen.add(num)
 		    return False
 		    
 		for row in board:
 		    if hasduplicates(row):
 		        return False
 		        
 		for col in range(9):
 		    column = [board[row][col] for row in range(9)]
 		    if hasduplicates(column):
 		        return False
 		       
 		for boxrow in range(0, 9, 3):
 		    for boxcol in range(0, 9, 3):
 		        subgrid = []
 		        for i in range(3):
 		            for j in range(3):
 		                subgrid.append(board[boxrow + i][boxcol + j])
 		        if hasduplicates(subgrid):
 		            return False
 		return True

if __name__ == "__main__":
	solution = Solution()
	board1 = [
		[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,9]
	]
	print(solution.isValidSudoku(board1))	# Expected: True

	board2 = [
		[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,5]
	]
	print(solution.isValidSudoku(board2))	# Expected: False

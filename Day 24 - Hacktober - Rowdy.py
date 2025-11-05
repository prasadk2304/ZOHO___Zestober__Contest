'''
On a college campus, a notorious Rowdy gang has taken over some rooms in a hostel. The hostel is represented as a 2D grid (matrix), where: 1 means the room is occupied by the gang, and 0 means the room is empty. 
Two rooms belong to the same gang if they are connected horizontally or vertically (not diagonally). The warden wants to know: “How many separate gangs are hiding inside the hostel?”
Task
Write a program that uses Depth-First Search (DFS) on the matrix to count the number of distinct Rowdy gangs.
'''
class Solution:
	def countRowdyGangs(self, matrix: list[list[int]]) -> int:
 		# TODO: implement DFS to count the number of connected components of 1s (4-directional)
 		if not matrix or not matrix[0]:
 		    return 0
 		
 		rows, cols = len(matrix), len(matrix[0])
 		visited = [[False for _ in range(cols)] for _ in range(rows)]
 		
 		def dfs(r, c):
 		    if r < 0 or r >= rows or c < 0 or c >= cols:
 		        return 
 		    if matrix[r][c] == 0 or visited[r][c]:
 		        return 
 		    visited[r][c] = True
 		    
 		    dfs(r+1, c)
 		    dfs(r-1, c)
 		    dfs(r, c+1)
 		    dfs(r, c-1)
 		    
 		count = 0
 		for r in range(rows):
 		    for c in range(cols):
 		        if matrix[r][c] == 1 and not visited[r][c]:
 		            dfs(r, c)
 		            count += 1
 		     
 		return count

if __name__ == "__main__":
	solution = Solution()
	print(solution.countRowdyGangs([
		[1, 1, 0, 0],
		[1, 0, 0, 1],
		[0, 0, 1, 1],
		[0, 0, 0, 0]
	]))	# Expected: 2
	print(solution.countRowdyGangs([
		[1, 1],
		[1, 1]
	]))	# Expected: 1
	print(solution.countRowdyGangs([
		[0, 0],
		[0, 0]
	]))	# Expected: 0

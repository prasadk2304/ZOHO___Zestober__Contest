'''
A gardener is planting a special Onion Garden. The garden is a grid of size n × n, and there are exactly n onion types available (for example: ["red", "white", "yellow"] when n = 3). 
The gardener wants to plant them so that no row contains the same onion type twice and no column contains the same onion type twice.
Task
Write a program to generate one valid planting layout. If no valid layout exists, return an empty grid.
'''

class Solution:
	def plantOnionGarden(self, n: int, types: list[str]) -> list[list[str]]:
 		# TODO: generate an n x n Latin square using the given onion types
 		# Constraints: no duplicate type in any row or column
 		# If no valid layout exists, return an empty list []
 		if len(types) != n:
 		    return []
 		    
 		garden = []
 		for i in range(n):
 		    row = []
 		    for j in range(n):
 		        row.append(types[(i+j) % n])
 		        
 		    garden.append(row)
 		return garden

if __name__ == "__main__":
	solution = Solution()
	print(solution.plantOnionGarden(2, ["red", "white"]))	# Expected: [['red','white'], ['white','red']]
	print(solution.plantOnionGarden(3, ["red", "white", "yellow"]))	# One possible: [['red','white','yellow'], ['white','yellow','red'], ['yellow','red','white']]

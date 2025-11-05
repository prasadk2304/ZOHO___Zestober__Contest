'''
In the city of Vacantia, a new underground parking system is being tested. The parking lot has n slots arranged in a single row: 0 → vacant, 1 → occupied. 
Incoming cars arrive in groups; each car has a length k and requires k consecutive vacant slots. 
The rules are strict: no two parked cars can be adjacent (there must be at least one empty slot between any two parked cars), cars must be attempted in the given order, and if a car cannot be placed, you must skip 
it and try the next one.
Task
Write a program to simulate the process and return the total number of cars that were successfully parked.
'''
class Solution:
	def simulateParking(self, slots: list[int], cars: list[int]) -> int:
 		# TODO: simulate parking with rules:
 		# - cars placed in given order
 		# - car of length k needs k consecutive 0s (vacant)
 		# - no two parked cars can be adjacent (leave at least one 0 between parked blocks)
 		# - if a car can't be placed anywhere, skip it and continue
 		# Return the count of successfully parked cars
 		
 		n = len(slots)
 		parked = 0
 		i = 0 
 		
 		for carlen in cars:
 		    placed = True
 		    while i <= n - carlen:
 		        if all(slots[i+j] == 0 for j in range(carlen)):
 		            
 		            beforeok = (i == 0) or (slots[i-1] == 0)
 		            afterok = (i + carlen >= n) or (slots[i+carlen] == 0)
 		            if beforeok and afterok:
 		                
 		                for j in range(carlen):
 		                    slots[i+j] = 1 
 		                parked += 1 
 		                i += carlen + 1 
 		                
 		                placed = True
 		                break 
 		        i += 1     
 		    if not placed:
 		        i = 0 
 		return parked

if __name__ == "__main__":
	solution = Solution()
	print(solution.simulateParking([0,0,0,1,0,0,0,0], [2,1,3]))	# Expected: 2
	print(solution.simulateParking([0,0,1,0,0,0], [1,2,2]))	# Expected: 2
	print(solution.simulateParking([1,1,1,1], [1,2,3]))	# Expected: 0

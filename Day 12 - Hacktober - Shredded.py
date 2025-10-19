'''
A chef is preparing for a big culinary show. To keep his secret recipes safe, he shreds each recipe document into strips. ( marks the start of a strip, ) marks the end of a strip. Now, to ensure the recipes can be reconstructed correctly, the chef wants to verify that all strips are balanced — meaning every opening ( has a matching closing ) and they are properly nested.
Task
Write a program that determines whether a given recipe string is balanced.
'''
class Solution:
	def isRecipeBalanced(self, recipe: str) -> bool:
 		# TODO: implement the logic to check if the recipe string is balanced (properly nested parentheses)
 		balance = 0
 		for ch in recipe:
 		    if ch == '(':
 		        balance += 1
 		    elif ch == ')':
 		        balance -= 1 
 		    
 		    if balance < 0:
 		        return False
 		      
 		return balance == 0

if __name__ == "__main__":
	solution = Solution()
	print(solution.isRecipeBalanced("(())()"))	# Expected: True
	print(solution.isRecipeBalanced("(()))("))	# Expected: False
	print(solution.isRecipeBalanced(""))	# Expected: True

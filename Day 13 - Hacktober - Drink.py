'''
At a school fair, a juice stall is offering a variety of drinks like apple juice, orange juice, and lemonade. The drinks are listed by their names in a single string, separated by spaces. The stall owner wonders: “If I have n unique drinks, how many different pairs can I mix?” At first, he could try listing them one by one… but that feels slow. Instead, he starts to think: Each drink can pair with every other drink. So the first drink makes (n-1) pairs, the second makes (n-2) new pairs (since one was already counted), and so on. Adding them up gives a neat shortcut. 👉 Can you figure out how this reasoning leads to the formula for the number of pairs? (2n)=2n⋅(n−1). Your task is to help the stall owner by finding how many unique drinks are available, and then computing how many unique pairs can be made.
Task
Write a program that takes the string of drinks and returns the number of unique pairs of drinks.
'''
class Solution:
	def countUniqueDrinkPairs(self, drinks_str: str) -> int:
 		# TODO: implement the logic to count unique drinks and compute total unique pairs (nC2)
 		drinks = drinks_str.split()
 		
 		unique = set(drinks)
 		
 		m = len(unique)
 		
 		return m * (m - 1) // 2

if __name__ == "__main__":
	solution = Solution()
	print(solution.countUniqueDrinkPairs("Apple Orange Mango Pineapple"))	# Expected: 6
	print(solution.countUniqueDrinkPairs("Mango Apple Apple Orange"))	# Expected: 3
	print(solution.countUniqueDrinkPairs("Mango"))	# Expected: 0

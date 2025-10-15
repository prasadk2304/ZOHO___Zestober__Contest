'''
In the deep ocean, where corals gleam and pearls whisper ancient secrets, a wise starfish guarded the sea’s magical treasures. One day, the Ocean King challenged the starfish:

“Can you discover whether some of these treasures together weigh exactly the sacred target weight?”
Task
Given a list of positive integers representing treasures and an integer target, determine whether it is possible to select some treasures (each treasure at most once) such that their total weight equals the target.
'''

class Solution:
	def canReachTarget(self, treasures: list[int], target: int) -> str:
 		# TODO: implement the logic to check if a subset sums to the target
            n = len(treasures)
            for i in range(n):
                    total = 0
                    for j in range(n):
                            if i < j:
                                    total += treasures[j]
                    if total == target:
                            return 'Yes'
            return 'No'

if __name__ == "__main__":
	solution = Solution()
	print(solution.canReachTarget([2, 3, 5], 8))	# Expected: Yes
	print(solution.canReachTarget([1, 4, 6], 8))	# Expected: No
	print(solution.canReachTarget([2, 3, 7, 8], 12))	# Expected: Yes

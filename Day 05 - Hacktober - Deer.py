'''
In a vast forest, wildlife researchers studied deer by tracking their unique tag numbers. Each day, rangers recorded sightings, creating a record of how often each deer appeared.
Task
Given a list of integers representing deer tag numbers, return the tag number of the deer with the most sightings. If multiple deer have the same maximum sightings, choose the one with the smallest tag number.
'''

class Solution:
	def mostSightedDeer(self, sightings: list[int]) -> int:
    		# TODO: implement logic to find deer with most sightings
            freq = {}
            for deer in sightings:
                    freq[deer] = freq.get(deer, 0) + 1
                		    
            maxdeer = max(freq, key=lambda x: (freq[x], -x))
            return maxdeer

if __name__ == "__main__":
	solution = Solution()
	print(solution.mostSightedDeer([101, 102, 101, 103, 102, 101, 104, 103]))  # Expected: 101
	print(solution.mostSightedDeer([201, 202, 201, 202, 203]))                  # Expected: 201

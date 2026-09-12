'''
Time complexity:
Space complexity:

Example:
nums = [2, -1, 1, 2]

Brute force solution:
- For each number, loop ahead and keep a track of sum, and then increment res when you get a sum of k

Better solution:
nums = [2, -1, 1, 2]
prefixSum = [2, 1, 2, 4]
A subarray [i, j] adds up to k where:
prefixSum(j) - prefixSum(i - 1) = k
In other words:
prefixSum(i-1) = prefixSum(j) - k

If we can keep a count of the number of prior prefixSum(i-1) in a hashmap, then per jth element, if we look back and find out out the number of count(prefixSum(i-1)), then we will know how many sub arrays, such that prefixSum(j) - prefixSum(i - 1) = k

Constraints:
- There will always be at least one number


Trace:
res = 4
nums = [2, -1, 1, 2]
i = 3
prefix_sum_count = {0:1, 2: 2, 1:1, 4:1}
prefix_sum = 4


'''

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0

        prefix_sum_count = defaultdict(int)

        prefix_sum = 0
        prefix_sum_count[0] = 1

        for i in range(len(nums)):
            prefix_sum += nums[i]
            res += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] += 1

        return res
        
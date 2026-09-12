"""
TC:
SC:

For a list l, the ith element is a pivot index iff:
    - sum(l[:i]) == sum(l[i+1:])

Initial thinking:
- Let's get the sum of all numbers excluding itself
- Then return the index where the sum is 0 
- Let's do postfix first, and then prefix, and then in the prefix loop when we detect the first 0 we can shortcircuit with the index


Tracing through the example:
nums = [1, 7, 3, 6, 5, 6]

postfix_without_self = [27, 20, 17, 11, 6, 0]
postfix_sum = 17

nums = [1, 7, 3, 6, 5, 6]
i = 3
postfix_without_self = [27, 20, 17, 11, 6, 0]
prefix_sum = 11



Constraints:
- There could be two pivot index's in the list, return the left most pivot index
- There will always be at least one number provided
- Numbers could be negative
- There could be no pivot index, in that case return -1

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postfix_sums_wo_self = [0] * len(nums)

        postfix_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix_sums_wo_self[i] = postfix_sum
            postfix_sum += nums[i]

        prefix_sum = 0
        for i in range(len(nums)):
            if postfix_sums_wo_self[i] - prefix_sum == 0:
                return i
            prefix_sum += nums[i]


        return -1
        



        
        
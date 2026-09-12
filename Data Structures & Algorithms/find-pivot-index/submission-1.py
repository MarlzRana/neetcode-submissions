"""
TC: O(n)
SC: O(1)

For a list l, the ith element is a pivot index iff:
    - sum(l[:i]) == sum(l[i+1:])

Initial thinking:
- Let's get the sum of all numbers excluding itself
- Then return the index where the sum is 0 
- Let's do postfix first, and then prefix, and then in the prefix loop when we detect the first 0 we can shortcircuit with the index

Optimal thinking:
- If we calculate the total, we can easily get the right sum on the fly using postfix_wo_self = total-curr_elem-prefix, whilst computing the prefix sum  


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
        total = sum(nums)

        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
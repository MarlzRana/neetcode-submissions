'''
Time complexity:
Space complexity:

Problem:
Given a list of nums and a target, return (i, j), such that nums[i] + nums[j] == target

Constraints:
- Only one valid example exists (and it will always exist)
- 2 <= nums.length <= 1000 (there is always at least two numbers in nums)
- Can get negative nums (in nums and as the target)
- Must return the smallest index first

Working through logical solution:
nums = [3, 4, 5, 6] target = 7
numsToIdx: {3: 0}
target_diff = 3
return [0, 1] / [target_diff_idx, curr_idx]

Try an example with negative nums:
nums = [-1, 5, 7, 3] target =6
numsToIdx = {-1: 0, 5: 1,  }
target_diff = -1
return [0, 2]


curr_num + difference_from_target = target
difference_from_target = target - curr_num

Trying an example 1 with code:
nums = [3, 4, 5, 6] target = 7
idx = 1, num = 4
seen_nums_idxs = {3: 0}
target_diff = 3
0, 1

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums_idx = {}

        for (idx, num) in enumerate(nums):
            target_diff = target - num
            if target_diff in seen_nums_idx:
                return [seen_nums_idx[target_diff], idx]
            seen_nums_idx[num] = idx
        
        raise Exception("There did not exist two pairs of numbers in nums that added up to the target")
            
            

        
# Time complexity: 
# Space complexity:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in nums_idx:
                return [nums_idx[complement], idx]

            nums_idx[num] = idx

        raise Exception("There should be two indices from nums that sum to make target")
        
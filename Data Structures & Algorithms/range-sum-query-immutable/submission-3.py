'''
__init__:
TC: O(n)
SC: O(n)

sumRange:
TC: O(1)
SC: O(1)


[-2, 0, 3, -5, 2, 1]
[0, -2, -2, 1, -4, -2, -1]


Constraints:
- there will always be at least one number
- left and right are always valid indexs
- left and right are inclusive

Edge cases:
- left = 0
- left = right
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0]

        for i in range(len(nums)):
            self.prefix_sums.append(self.prefix_sums[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
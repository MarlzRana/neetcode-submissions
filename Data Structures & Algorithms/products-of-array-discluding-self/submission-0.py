'''
TC:
SC:

input = [1, 2, 4, 6]
lProducts = [1, 1, 2, 8, 48]
rProducts = [48, 48, 24, 6, 1]

output: [1 * rightProducts[0] , leftProducts[0] * rightProducts[1], leftProducts[1] * rightProducts[2], leftProducts[2] * 1]

constraints:
- there will always be at least two numbers
- numbers can be negative or postive 
- actual result will always fit in a 32 bit number
'''

from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_products = deque([1])
        right_products = deque([1])
        
        for i in range(len(nums)):
            left_products.append(left_products[-1] * nums[i])
            right_products.appendleft(right_products[0] * nums[len(nums) - 1 - i])


        res = []

        for i in range(len(nums)):
            res.append(left_products[i] * right_products[i + 1])

        return res

        
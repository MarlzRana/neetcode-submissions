'''
TC: O(n)
SC: O(n)

input = [1, 2, 4, 6]
i = 3
res = [1, 1, 2, 8]
prefix_product = 48

input = [1, 2, 4, 6]
i = 0
res = [48, 24, 12, 8]
postfix_product = 48

output: [1 * rightProducts[0] , leftProducts[0] * rightProducts[1], leftProducts[1] * rightProducts[2], leftProducts[2] * 1]

constraints:
- there will always be at least two numbers
- numbers can be negative or postive 
- actual result will always fit in a 32 bit number
'''

from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = 1
        postfix_product = 1

        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix_product
            postfix_product *= nums[i]
            
        return res

        

        


        
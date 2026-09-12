'''
TC:
SC:

Brute force:
For each number, calculate the max length consecutive sequence you could make, and then max those; TC: O(n^2)

Smarter approach:
- The key thing to remember here is that order of the numbers does not matter, and also duplicates can be ignored, so we can apply the set operation safely
- Also that you can identify the beginning of a potential consequtive sequence by not finding x - 1 in the array
- We also need a way to check if a subsequent element can be found (set)

- let's set the entire thing
- For each num in the set, find the beginning element of any potential sequence, and see how long you can make a consecutive sequence out of it 

Constraints:
- There could be 0 numbers
- nums (a, b) are consectutive iff a + 1 = b; a and b do not have to be consectutive in the orignal


'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
    
        nums_set = set(nums)
        longest_seq_length = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                curr_seq_len = 1
                curr_num = num
                while curr_num + 1 in nums_set:
                    curr_seq_len += 1
                    curr_num += 1
                longest_seq_length = max(curr_seq_len, longest_seq_length)

        return longest_seq_length
                





        
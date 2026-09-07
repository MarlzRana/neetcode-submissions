'''
Time complexity: O(n)
Space complexity: O(n)

Work through an example logically:
nums = [1, 2, 2, 3, 3, 3] k = 2

sol 1:
We keep a elem->count map and then we sort by count at the end and pop off count descending up to k time
TC: n + nlog(n) = nlog(n)
SC: n

sol 2:
- We keep a elem->count map: O(n)
- heapify: O(n)
- heappop k times: k * O(log(n))
Time complexity: O(n)

sol 3 (using the idea of bucket sort):
- Make an elem->count map: O(n)
- Create len(nums) buckets: O(n)
- For each bucket (in reverse order) pick out k items: O(n + k) = O(n) as n >= k
TC: O(n)
SC: O(n)


Constraints
- Test cases ensure answer is always unique
- There will always be at least one number
- Numbers can be postivie or negative
- k is always less than set(nums) 

Trying out the solution on an example:
nums = [1,2,2,3,3,3] k = 2
elem_freq = {1: 1, 2: 2, 3: 3}
freq_buckets = [[1],[2],[3],[],[],[]]
res = [3, 2]
curr_bucket_idx = 0
k = 0

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build the elem->freq map
        elem_freq = defaultdict(int)
        for num in nums:
            elem_freq[num] += 1

        # Create the frequency buckets
        freq_buckets = [[] for _ in range(len(nums))]
        for (elem, freq) in elem_freq.items():
            freq_buckets[freq - 1].append(elem)

        # Go through the frequency buckets in reverse order, picking out k elements along the way
        res = []
        curr_bucket_idx = len(freq_buckets) - 1
        while curr_bucket_idx > -1 and k > 0:
            if not freq_buckets[curr_bucket_idx]:
                curr_bucket_idx -= 1
                continue
            res.append(freq_buckets[curr_bucket_idx].pop())
            k -= 1

        return res



        
'''
Time complexity:
Space complexity:


Going through it logically
anagram_bags = {a1,c1,t1: ["act", "cat"] }
return keys

Constraints:
- There will be at least one string
- You can get empty strings
- Only lowercase letters
- Can return the bag in any order

Working through an example in the code:
strs = ["act","pots","tops","cat","stop","hat"]
char_count = p1, o1, t1, s1 
anagram_bags = {(a1, c1, t1): ["act"], (o1, p1, s1, t1): ["pots", "]}
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_bags = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            anagram_bags[tuple(char_count)].append(word)
        
        return list(anagram_bags.values())


'''
Time complexity: O(n) + O(n) = O(n)
Space complexity: O(1)
Constraints:
- Only lowercase English characters
- Length of strings never 0

Anagram condition:
For a given string s and t, s and t are anagrams iff:
    - len(s) == len(t)
    - for each unique char c in s, num(c, s) == num(c, t)

Examples:
r: 2, 2
a: 2, 2
c: 2, 2
e: 1, 1

Trace an example through the worked solution:
- s = "r", t = "m"
a, j, m, r 
char_diffs = [0, 0, -1, 1]

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_diffs = [0] * 26

        for (char_s, char_t) in zip(s, t):
            char_diffs[ord(char_s) - ord('a') ] += 1
            char_diffs[ord(char_t) - ord('a') ] -= 1

        return all(char_diff == 0 for char_diff in char_diffs)
        

        

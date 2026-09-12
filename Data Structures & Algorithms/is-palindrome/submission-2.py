'''
TC: O(n)
SC: O(1)

Problem:
Return true iff s are a palindrome
s and t are a palindrome iff s = rev(s)

Constraints:
- You cannot get the empty string
- S is ascii characeters only
- Ignore non-alphanumeric characters and case sensitivity
'''



class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True


        

        
        
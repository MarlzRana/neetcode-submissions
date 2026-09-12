'''
TC:
SC:

Constraints:
- Will never get the empty string
- String only contains brackets
'''

class Solution:
    def isValid(self, s: str) -> bool:
        brac_stack = []

        open_bracs = {'(', '{', '['}

        for i in range(len(s)):
            if s[i] in open_bracs:
                brac_stack.append(s[i])
            else:
                if not brac_stack:
                    return False
                last_brac_on_stack = brac_stack.pop(-1)
                if (
                    (s[i] == ')' and last_brac_on_stack != '(')
                    or (s[i] == '}' and last_brac_on_stack != '{')
                    or (s[i] == ']' and last_brac_on_stack != '[')
                    ):
                    return False

        return not brac_stack
        
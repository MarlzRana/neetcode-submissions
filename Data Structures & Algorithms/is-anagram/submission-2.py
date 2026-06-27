class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_diffs = [0] * 26

        for s_char, t_char in zip(s, t):
            char_diffs[ord(s_char) - ord('a')] += 1
            char_diffs[ord(t_char) - ord('a')] -= 1

        return all(char_diff == 0 for char_diff in char_diffs)

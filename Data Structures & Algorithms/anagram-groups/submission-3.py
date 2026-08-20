class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_words = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            char_count_words[tuple(char_count)].append(word)
        return list(char_count_words.values())
             
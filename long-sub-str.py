class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        if isinstance(s, str):
            char_set = set()
            start = 0
            longest_len = 0
            for end in range(len(s)):
                char = s[end]
                while char in char_set:
                    char_set.remove(s[start])
                    start += 1
                char_set.add(char)
                longest_len = max(longest_len, end - start + 1)
            return longest_len
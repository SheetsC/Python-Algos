class Solution:
    def wordPattern(self, s: str, pattern: str):
        split_s = s.split()

        if len(split_s) != len(pattern):
            return False
        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, split_s):
            if char not in char_to_word and not word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char
            elif char in char_to_word and char_to_word[char] != word:
                return False
            elif word in word_to_char and word_to_char[word] != char:
                return False
        return True
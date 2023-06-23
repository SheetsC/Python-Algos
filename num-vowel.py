class Solution:
    def count_vowels(self, s: str):
        vowel = ['a','e','i','o','u']
        count = 0
        for char in s.lower():
            if char in vowel: 
                count += 1
        return count
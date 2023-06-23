class Solution:
    def reverse_a_sentence(self, sentence: str) -> str:
        split_s = sentence.split(' ')
        l = 0 
        r = len(split_s) -1 
        new_split = []
        for word in split_s:
            new_split.append(split_s[r])
            l += 1
            r -= 1
        revrsd_s = ' '.join(new_split)
        return revrsd_s

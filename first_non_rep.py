# first non repeating char in a string
class Solution:
    def find_non_repeating_char(self,s):
        my_dic = {}
        for char in s:
            my_dic[char] = my_dic.get(char, 0) + 1
        for char in s:
            if my_dic[char] == 1:
                return char
        return None
class Solution:
    def gcd_of_str(self, str1: str, str2: str):
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        len1, len2 = len(str1), len(str2)
        if str1 + str2 != str2 + str1:
            return ""
        common_len = gcd(len1, len2)
        return str1[:common_len]
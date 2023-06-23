class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        reversed_str_x = str_x[::-1]
        reversed_x = int(reversed_str_x)
        
        if x < 0:
            reversed_x = -reversed_x
        
        if reversed_x < -2**31 or reversed_x > (2**31 - 1):
            return 0
        
        return reversed_x


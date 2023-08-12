class Solution:
    def addOne(self, digits):
        joined_digits = int(''.join(map(str, digits)))
        new_array = [int(digit) for digit in str(joined_digits + 1)]
        return new_array
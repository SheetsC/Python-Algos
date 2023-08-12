class Solution:
    def sumFourDivisors(self, nums) :
        res = 0 
        for num in nums:
            divisor = set()
            for i in range(1,int (num ** 0.5)+1):
                if num % i == 0:
                    divisor.add(num // i)
                    divisor.add(i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                res += sum(divisor)
        return res
class Solution:
    def maxSubArray(self, nums):
        current_max = num_max = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            num_max = max(num_max, current_max)
        return num_max
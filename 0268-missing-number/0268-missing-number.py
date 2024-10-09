class Solution(object):
    def missingNumber(self, nums):
        # n = len(nums)
        # for i in range ( n + 1): # in n + 1 also include the missing number
        #     if i not in nums:
        #         return i
        n = len(nums)
        expectedSum = n * ( n + 1 ) // 2
        actualSum = sum(nums)
        return expectedSum - actualSum
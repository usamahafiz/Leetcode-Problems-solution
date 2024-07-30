class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target: #greater than equal to use bcz it find in what position the mising element inserted
                return i
        return len(nums)
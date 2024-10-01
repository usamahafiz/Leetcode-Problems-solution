class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0

        i = 0
        for j in range(1, len(nums)): 
            if nums[j] != nums[i]: #means unique element is present 
                i += 1
            nums [i] = nums[j] #assign value of j to i

        return i + 1
        
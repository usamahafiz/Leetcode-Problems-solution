class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()  # sorted in the ascending order
        arr = (nums[-1] - 1) * (nums[-2] - 1) # multiply last and second last element of array then get max product 
        return arr

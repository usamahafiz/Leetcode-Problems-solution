class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= [] 
        nums.sort()
        for i , a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # check duplicate current element from the previous element
                continue
        
            l , r = i + 1 , len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a , nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:#check duplicate of the second and third elements and increament left by one
                        l += 1
        return res


        
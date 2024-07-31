class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0 , len(numbers) - 1
        while left < right: # in this step we avoid indices over reach in a same list element/number
            if numbers[left] + numbers[right] > target:
                right -= 1 #bcz we know list sorted in increasing order fron smaller to larger one
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1] #in this step we add one separately in both indices whose sum equals to target 
            

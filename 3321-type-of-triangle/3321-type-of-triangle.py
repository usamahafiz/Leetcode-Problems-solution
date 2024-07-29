class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a+b > c and b+c > a and c+a > b: # we use and bcz of all three conditions fullfilled
            if a == b == c:
                return "equilateral"
            if a == b or b == c or c == a: # any of condition must be true
                return "isosceles"
            else:
                return "scalene"
        return "none"

        
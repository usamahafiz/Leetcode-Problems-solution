class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        res_num = 0
        while num > 0:
            digit = num % 10 # we get last digit as a remainder
            res_num =  (res_num * 10) + digit
            num = num // 10 # by this remove the last digit of the input 

        return res_num == x
           

        
       




        
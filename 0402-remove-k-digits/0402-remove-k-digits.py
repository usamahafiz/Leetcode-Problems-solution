class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop() #remove that element which fullfill the conditions
            stack.append(c) 
        stack = stack[:-k] if k else stack
        res = "".join(stack) #again join string in the stack 
        return res.lstrip('0') or '0' if res else '0' #we return res convert into integer so that leading zeros removed and again convert into string 
#if res is empty then we return "0" as else 
        
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:  # means character are duplicates
                stack.pop() #pop (remove) duplicate character
            else:
                stack.append(c)  # append the charater in the string
        return "".join(stack) 
#time complexity O(n)
#space complexity O(n)

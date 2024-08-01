class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_mapping = {')':'(','}':'{',']':'['}
        for char in s:
            if (char in bracket_mapping):
                top_element = stack.pop() if stack else '#' # if both brackets match then pop(remove) that pair of brackets 
                if bracket_mapping[char] != top_element:
                    return False #bcz opening bracket not match with the closing bracket
            else:
                stack.append(char)  #if it is an opening bracket push onto the stack
        return not stack        
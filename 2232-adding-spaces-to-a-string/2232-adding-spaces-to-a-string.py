class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        string_index = 0
        for i in range(len(s)):
            if string_index < len(spaces) and i == spaces[string_index]:
                result.append(" ")
                string_index += 1
            result.append(s[i])
        return"".join(result)

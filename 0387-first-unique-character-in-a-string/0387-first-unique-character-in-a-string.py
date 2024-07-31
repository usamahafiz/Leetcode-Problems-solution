class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1  # if character not repeat then char_count become 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index  # bcz it is actually the first non-repeating character
        return -1

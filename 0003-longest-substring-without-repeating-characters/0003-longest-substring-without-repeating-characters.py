class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        sb = 0
        for r in range(len(s)):
            if s[r] in hashmap:  # check the current character in hashmap
                l = max(l, hashmap[s[r]] + 1)  #if it present then update l max value between l and current hashmap index + 1
            hashmap[s[r]] = r # otherwise out the and upgrade hashmap index value to the current index
            sb = max(sb, r - l + 1) # also update sb to the max one b/t sb and lenght of sb
        return sb

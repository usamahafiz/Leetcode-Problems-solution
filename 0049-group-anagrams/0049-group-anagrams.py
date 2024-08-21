class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))  # words in the list sorted alphabeticaly
            anagrams[sorted_str].append(s) # append the words which behave as anagram on the basis of key
        return anagrams.values() #at last return only group of anagrams 
#time complexity O(k.n logn)
# 'k' is the number of string and 'n' is the length of the string 
#space complexity O(k . n) # 'k' is the number of string and 'n' is the length of the string 
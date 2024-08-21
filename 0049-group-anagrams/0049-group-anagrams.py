class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))  # words in the list sorted alphabeticaly
            anagrams[sorted_str].append(s)
        return anagrams.values()

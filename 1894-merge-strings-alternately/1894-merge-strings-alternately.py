class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        merge_str = ""
        for i in range (min_length):
           merge_str += word1[i] + word2[i]
        if len(word2) > min_length:
           merge_str += word2[min_length:]
        if len(word1) > min_length:
            merge_str += word1[min_length:]
        return merge_str

        
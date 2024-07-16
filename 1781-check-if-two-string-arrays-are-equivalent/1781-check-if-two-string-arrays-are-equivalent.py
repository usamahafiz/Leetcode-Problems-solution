class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        arr_word1 = "".join(word1)
        arr_word2 = "".join(word2)
        return arr_word1 == arr_word2

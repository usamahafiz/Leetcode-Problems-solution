class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)): #iterate over the indices of words
            if x in words[i]: #given x is present in the words at index i
                arr.append(i) #if true append(move) in the list arr
        return arr

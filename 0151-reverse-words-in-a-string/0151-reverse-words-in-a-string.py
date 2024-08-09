class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.split() #split each word in a sentence with comma
        # s = s[::-1] #then slicing(reverse) the sentence
        words = s.split()
        words.reverse()
        return " ".join(words) #at last join the string and have space between them
        
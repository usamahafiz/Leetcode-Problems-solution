class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split() #split each word in a sentence with comma
        s = s[::-1] #then slicing(reverse) the sentence
        return " ".join(s) #at last join the string and have space between them
        
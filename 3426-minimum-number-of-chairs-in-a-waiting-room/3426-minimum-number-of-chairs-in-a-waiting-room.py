class Solution:
    def minimumChairs(self, s: str) -> int:
        curPeople = 0
        maxPeople = 0
        
        for char in s:
            if char == 'E':
               curPeople += 1
            if curPeople > maxPeople:
                maxPeople = curPeople
            if char == 'L':
                curPeople -=1
        return maxPeople



        
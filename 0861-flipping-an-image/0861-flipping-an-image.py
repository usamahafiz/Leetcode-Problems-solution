class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range (len(image)):
            image[i].reverse() #to flip or reverse the imege horizontally
            for j in range (len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1 #if number become zero it convert into one 
                else:
                    image[i][j] = 0 #otherwise it remains as zero
        return image
#time complexity O(m x n) where 'm' is row and 'n' is the elements in the row 
#space complexity O(1)
        
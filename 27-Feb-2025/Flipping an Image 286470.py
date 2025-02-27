# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        result = []
        for row in image:
            reverse = row[::-1]
            result.append(reverse)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][j] == 0:
                    result[i][j] = 1
                else:
                    result[i][j] = 0
        return result

            

            
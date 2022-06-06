class Solution:
    
    def floodFillUtil(self, image, i, j, prevC, newC):
        
        if i < 0 or j < 0 or i > len(image) -1 or j > len(image[i])-1:
            return
        if image[i][j] != prevC:
            return
        else:
            image[i][j] = newC
            if i - 1 >= 0 and image[i - 1][j] == prevC:
                image[i - 1][j] = newC
            if i + 1 <= (len(image) - 1) and image[i + 1][j] == prevC:
                image[i + 1][j] = newC
            if j - 1 >= 0 and image[i][j - 1] == prevC:
                image[i][j - 1] = newC
            if j + 1 <= (len(image[i]) - 1) and image[i][j + 1] == prevC:
                image[i][j + 1] = newC
            return

    def floodFill(self, image, sr, sc, newColor):
        prevColor = image[sr][sc]

        self.floodFillUtil(image, sr + 1, sc, prevColor, newColor)
        self.floodFillUtil(image, sr - 1, sc, prevColor, newColor)
        self.floodFillUtil(image, sr, sc + 1, prevColor, newColor)
        self.floodFillUtil(image, sr, sc - 1, prevColor, newColor)
        image[sr][sc] = newColor	
        return image


ob = Solution()
ob.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)

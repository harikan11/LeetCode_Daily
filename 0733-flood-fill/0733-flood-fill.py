class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        
        if old_color != newColor:
            self.helper(image, sr, sc, old_color, newColor)
        
        return image
        
    def helper(self, image, i, j, old_color, new_color):
        
        if i < 0 or i > len(image) - 1:
            return
        
        if j < 0 or j > len(image[0]) - 1:
            return
        
        if image[i][j] != old_color:
            return
        else:
            image[i][j] = new_color
            
            self.helper(image, i, j - 1, old_color, new_color)            
            self.helper(image, i, j + 1, old_color, new_color)            
            self.helper(image, i - 1, j, old_color, new_color)            
            self.helper(image, i + 1, j, old_color, new_color)
        

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]
        
        def dfs(sr, sc):
            if sr not in range(rows): return
            if sc not in range(cols): return
            if image[sr][sc] == newColor: return
            if image[sr][sc] != original_color: return
            
            image[sr][sc] = newColor
            
            dfs(sr-1, sc)
            dfs(sr+1, sc)
            dfs(sr, sc-1)
            dfs(sr, sc+1)
        
        dfs(sr, sc)
        return image
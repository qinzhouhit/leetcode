'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    # O(N) for S and T, N as the number of pixels in the image    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:        R, C = len(image), len(image[0])        color = image[sr][sc]        if color == newColor:             return image                def dfs(r, c):            if image[r][c] == color:                image[r][c] = newColor                if r >= 1: dfs(r-1, c)                if r+1 < R: dfs(r+1, c)                if c >= 1: dfs(r, c-1)                if c+1 < C: dfs(r, c+1)                dfs(sr, sc)        return image        def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:        r, c = len(image), len(image[0])        color = image[sr][sc]        def dfs(i, j):            if i < 0 or i>=r or j < 0 or j >= c:                return            if image[i][j] == newColor or image[i][j] != color:                return            image[i][j] = newColor            dfs(i+1, j)            dfs(i-1, j)            dfs(i,j+1)            dfs(i, j-1)        dfs(sr, sc)        return image                                
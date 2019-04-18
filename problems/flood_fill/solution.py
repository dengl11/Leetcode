class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                cx, cy = r + dx, c + dy
                if cx >= 0 and cx < m and cy >= 0 and cy < n:
                    if image[cx][cy] == color:
                        stack.append((cx, cy))
        return image
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0],[0,1],[0,-1],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        # print(fresh, q)

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for i,j in directions:
                    dr, dc = r+i, c+j
                    if dr < 0 or dr >= rows or dc < 0 or dc >= cols or grid[dr][dc]!=1:
                        continue
                    grid[dr][dc] = 2
                    q.append((dr,dc))
                    fresh-=1

            time +=1
            
        
        return time if fresh == 0 else -1

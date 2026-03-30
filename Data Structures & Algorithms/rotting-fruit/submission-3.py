class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        # seen = set()
        fresh = 0
        q = deque()
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                r,c = node
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr < 0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] != 1:
                        continue
                    fresh-=1
                    grid[nr][nc] = 2
                    q.append((nr,nc))

            time+=1
        return time if fresh == 0 else -1
                


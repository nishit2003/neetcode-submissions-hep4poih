class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        def addcell(r,c):
            if(r < 0 or r>= rows) or (c < 0 or c >= cols) or grid[r][c] != 1:
                return
            q.append((r,c))
            grid[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                addcell(r-1,c)
                addcell(r+1,c)
                addcell(r,c-1)
                addcell(r,c+1)
            fresh -= len(q)
            time += 1


        return time if fresh == 0  else -1
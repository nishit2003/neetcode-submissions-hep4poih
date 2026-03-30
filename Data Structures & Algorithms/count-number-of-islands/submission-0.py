class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Edge case: if the grid is empty
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()  # A set to track visited cells

        def dfs(r, c):
            # If out of bounds, already visited, or it's water, return
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visit or grid[r][c] == '0'):
                return
            visit.add((r, c))  # Mark the current cell as visited
            # Explore the four neighboring cells
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        island_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                # If we find an unvisited land cell
                if grid[r][c] == '1' and (r, c) not in visit:
                    island_count += 1  # Found a new island
                    dfs(r, c)  # Run DFS to mark the entire island

        return island_count

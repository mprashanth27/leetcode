from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        
        length = 0 # As counting from 0th min
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    for x in range(ROWS):
                        for y in range(COLS):
                            if (grid[x][y] == 1):
                                return -1
                    return length
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 2):
                        continue
                    if (grid[r][c] == 2 and grid[r + dr][c + dc] != 0):
                        grid[r + dr][c + dc] = 2
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))           
            length += 1

test_obj = Solution()

grid_1 = [[2,1,1],[1,1,0],[0,1,1]]
grid_2 = [[2,1,1],[0,1,1],[1,0,1]]
grid_3 = [[0,2]]

print(test_obj.orangesRotting(grid_1))
print(test_obj.orangesRotting(grid_2))
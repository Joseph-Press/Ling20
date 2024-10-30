from collections import deque

class Castle:
    def __init__(self, rows, cols, walls, escape_point):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        for (r, c) in walls:
            self.grid[r][c] = -1  # Mark walls in the grid
        self.escape_point = escape_point

    def is_valid_move(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != -1

    def escape_castle(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        queue = deque([(0, 0, 0)])  # (row, col, steps)
        visited = set([(0, 0)])

        while queue:
            r, c, steps = queue.popleft()  # Add parentheses here

            if (r, c) == self.escape_point:
                return steps

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if self.is_valid_move(new_r, new_c) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, steps + 1))

        return -1  # No valid path found

def escape_castle(rows, cols, walls, escape_point):
    castle = Castle(rows, cols, walls, escape_point)
    return castle.escape_castle()

# Test with the provided sample input
rows = 2
cols = 2
walls = [(1, 0), (1, 1)]
escape_point = (1, 1)

# Execute the function
result = escape_castle(rows, cols, walls, escape_point)
print(result)  # Output should be 2

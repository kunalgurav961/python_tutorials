import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost from start node
        self.h = h  # Heuristic (estimated cost to goal)
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    open_list = []
    closed_set = set()
    
    start_node = Node(start, None, 0, heuristic(start, end))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == end:
            return reconstruct_path(current_node)

        closed_set.add(current_node.position)

        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            new_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if new_pos in closed_set or not is_valid(grid, new_pos):
                continue

            g = current_node.g + 1
            h = heuristic(new_pos, end)
            new_node = Node(new_pos, current_node, g, h)

            heapq.heappush(open_list, new_node)

    return None  # No path found

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan Distance

def is_valid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == 0

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  # Reverse the path

# Example Grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)
path = astar(grid, start, end)
print("Path:", path)

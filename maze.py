# The name and location of each node is based as described on maze.png
graph = {
    'A1': set(['A2']),
    'A2': set(['A1','A3']),
    'A3': set(['A2','A4']),
    'A4': set(['A3','B4','A5']),
    'A5': set(['A4']),
    'B1': set(['B2','C1']),
    'B2': set(['B1','B3']),
    'B3': set(['B2','B4']),
    'B4': set(['A4','B3','B5','C4']),
    'B5': set(['B4','C5']),
    'C1': set(['B1','D1']),
    'C2': set(['D2']),
    'C3': set(['D3']),
    'C4': set(['B4']),
    'C5': set(['B5','D5']),
    'D1': set(['C1','D2']),
    'D2': set(['C2']),
    'D3': set(['C3','E3']),
    'D4': set(['E4']),
    'D5': set(['C5','D5']),
    'E1': set(['E2']),
    'E2': set(['E3']),
    'E3': set(['D3','E2','E4']),
    'E4': set(['D4','E3','E5']),
    'E5': set(['D5','E4'])
}

from collections import deque

def bfs(graph, start, goal):
    # Initialize the queue and set to keep track of visited nodes
    queue = deque()
    visited = set()

    # Initialize the queue with the start node
    queue.append((start, [start]))

    while queue:
        node, path = queue.popleft()

        if node == goal:
            # If we reach the goal, return the path
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    # Enqueue the neighbor and update the path
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

    # If no path is found
    return None



# Set the start and end nodes
start = 'A1'
goal = 'C2'
path = bfs(graph, start, goal) # Call the bfs function

if path:
    print("Path from", start, "to", goal, ":", " -> ".join(path))
else:
    print("No path found from", start, "to", goal)

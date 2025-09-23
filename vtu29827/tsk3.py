class Graph:
    def __init__(self, adjacency_list, heuristic):
        self.adjacency_list = adjacency_list
        self.heuristic = heuristic

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def a_star(self, start, goal):
        open_list = set([start])
        closed_list = set()

        g = {start: 0}
        parents = {start: None}

        while open_list:
            # Select node with lowest f = g + h
            current = min(open_list, key=lambda n: g[n] + self.heuristic.get(n, float('inf')))

            if current == goal:
             
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                path.reverse()
                return path, g[goal]

            open_list.remove(current)
            closed_list.add(current)

            for neighbor, cost in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                tentative_g = g[current] + cost

                if neighbor not in open_list:
                    open_list.add(neighbor)
                elif tentative_g >= g.get(neighbor, float('inf')):
                    continue

                parents[neighbor] = current
                g[neighbor] = tentative_g

        return None, float('inf')


if __name__ == "__main__":
    adj_list = {
        'a': [('b', 2), ('c', 4), ('d', 1)],
        'b': [('e', 7), ('f', 3)],
        'c': [('f', 1)],
        'd': [('g', 5)],
        'e': [('g', 2)],
        'f': [('e', 2), ('g', 1)],
        'g': []
    }

    heuristic = {
        'a': 7,
        'b': 6,
        'c': 2,
        'd': 3,
        'e': 1,
        'f': 1,
        'g': 0
    }

    graph = Graph(adj_list, heuristic)
    start_node = 'a'
    goal_node = 'g'

    path, cost = graph.a_star(start_node, goal_node)
    if path:
        print(f"Path found: {path}")
        print(f"Total cost: {cost}")
    else:
        print("No path found")

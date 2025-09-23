Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import collections
... 
... graph = collections.defaultdict(list)
... 
... def add_edge(u, v, cost):
...   graph[u].append((v, cost))
...   graph[v].append((u, cost))
... 
... add_edge('A', 'B', 5)
... add_edge('A', 'C', 3)
... add_edge('B', 'D', 2)
... add_edge('C', 'D', 4)
... add_edge('C', 'E', 6)
... add_edge('D', 'E', 1)
... 
... def get_edge_cost(start_node, end_node):
...     for neighbor, cost in graph[start_node]:
...         if neighbor == end_node:
...             return cost
...     return float('inf')
... 
... def calculate_path_cost(path):
...     total_cost = 0
...     for i in range(len(path) - 1):
...         start_node = path[i]
...         end_node = path[i+1]
...         cost = get_edge_cost(start_node, end_node)
...         if cost == float('inf'):
...             return float('inf')
...         total_cost += cost
...     return total_cost
... 
... print("Cost from A to B:", get_edge_cost('A', 'B'))
... print("Cost from C to E:", get_edge_cost('C', 'E'))
... print("Cost from A to D (no direct edge):", get_edge_cost('A', 'D'))
... 
... path1 = ['A', 'C', 'D', 'E']
path2 = ['A', 'B', 'D', 'E']
path3 = ['A', 'C', 'E']

print("Cost of Path 1:", calculate_path_cost(path1))
print("Cost of Path 2:", calculate_path_cost(path2))
print("Cost of Path 3:", calculate_path_cost(path3))

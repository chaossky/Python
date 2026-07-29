
def dijkstra(graph, source):
   # Initialize distances and visited set
   num_nodes = len(graph)
   distances = [float('inf')] * num_nodes
   distances[source] = 0
   visited = [False] * num_nodes
   for _ in range(num_nodes):
       # Find the unvisited node with the smallest distance
       min_distance = float('inf')
       min_node = -1
       for i in range(num_nodes):
           if not visited[i] and distances[i] < min_distance:
               min_distance = distances[i]
               min_node = i
       # Mark the node as visited
       visited[min_node] = True
       # Update distances for neighbors of the current node
       for neighbor, weight in enumerate(graph[min_node]):
           if weight > 0 and not visited[neighbor]:
               new_distance = distances[min_node] + weight
               if new_distance < distances[neighbor]:
                   distances[neighbor] = new_distance
   return distances
# Example Usage
# Graph represented as an adjacency matrix
graph = [
   [0, 4, 0, 0, 0, 0],
   [4, 0, 8, 0, 0, 0],
   [0, 8, 0, 7, 0, 4],
   [0, 0, 7, 0, 9, 14],
   [0, 0, 0, 9, 0, 10],
   [0, 0, 4, 14, 10, 0]
]
source_node = 0
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from source:", shortest_distances)
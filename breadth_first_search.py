import Queue

def shortest_path(graph, start_vertex, end_vertex):
  distance_from_start_vertex = dict()
  distance_from_start_vertex[start_vertex] = 0

  q = Queue.Queue()
  q.put(start_vertex)

  while not q.empty():
    vertex = q.get()

    if vertex is end_vertex:
      return distance_from_start_vertex[end_vertex]

    for adjacent_vertex in graph[vertex]:
      if adjacent_vertex in distance_from_start_vertex:
        continue

      distance_from_start_vertex[adjacent_vertex] = distance_from_start_vertex[vertex] + 1
      q.put(adjacent_vertex)

graph = {
  's': ['a', 'b'],
  'a': ['s', 'c'],
  'b': ['s', 'c', 'd'],
  'c': ['a', 'b', 'd', 'e'],
  'd': ['b', 'c', 'e'],
  'e': ['c', 'd']
}

print(shortest_path(graph, 's', 'e'))
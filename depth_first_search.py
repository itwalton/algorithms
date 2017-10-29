def topological_sort(graph):
  order = []
  explored = dict()

  def depth_first_search(vertex):
    # mark vertex as 'explored'
    explored[vertex] = True

    # iterate over vertices joined by edges from current vertex
    for v in graph[vertex]:
      if v not in explored:
        depth_first_search(v)

    # ends at 'sink node' and works up the call stack to the start element
    order.insert(0, vertex)

  # loop over all vertices in graph (order is arbitrary)
  for vertex, edges in graph.iteritems():

    # ignore vertices explored in previous dfs calls
    if vertex not in explored:
      depth_first_search(vertex)

  return order

graph = {
  'u': ['x'],
  'w': ['x'],
  's': ['u', 'w'],
  'x': []
}

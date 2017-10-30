import sys, threading
import operator

sys.setrecursionlimit(800000)
threading.stack_size(67108864)

def build_graph(filename):
  graph = dict()
  with open(filename, 'r') as f:
    for line in f:
      s,t = line.split()
      s,t = int(s), int(t)
      dest_nodes = graph.get(s, list())
      dest_nodes.append(t)
      graph[s] = dest_nodes
  return graph

def reverse_graph(graph):
    reversed_graph = dict()

    # reverse edges in graph
    for vertex, edges in graph.iteritems():
      for v in edges:
        if v not in reversed_graph: reversed_graph[v] = [vertex]
        else: reversed_graph[v].append(vertex)

    return reversed_graph

def calc_finishing_times(graph):
  global finishing_time

  finishing_time = 0
  explored = dict()
  times_graph = dict()

  def dfs(vertex):
    global finishing_time

    explored[vertex] = True
    if vertex in graph:
      for v in graph[vertex]:
        if v not in explored:
          dfs(v)

    # calc finishing times
    finishing_time += 1
    times_graph[vertex] = finishing_time

  for vertex in range(len(graph), 0, -1):
    if vertex not in explored:
      dfs(vertex)

  return times_graph

def translate_graph_by_finishing_times(times_graph, graph):
  translated_graph = dict()
  for vertex, edges in graph.iteritems():
    if vertex in times_graph:
      translated_graph[times_graph[vertex]] = []
      for v in edges:
        if v in times_graph:
          translated_graph[times_graph[vertex]].append(times_graph[v])

  return translated_graph

def calc_strongly_connected_components(graph):
  global leader

  sccs = dict()
  explored = dict()

  def dfs(vertex):
    explored[vertex] = True

    if vertex in graph:
      for v in graph[vertex]:
        if v not in explored:
          dfs(v)

    sccs[leader].append(vertex)

  for vertex in range(len(graph), 0, -1):
    if vertex not in explored:
      leader = vertex
      sccs[leader] = []
      dfs(vertex)

  return sccs

def kosaraju(graph):
  # reverse the graph & calculate finishing times
  times_graph = calc_finishing_times(reverse_graph(graph))

  # translate original graph by finishing times
  translated_graph = translate_graph_by_finishing_times(times_graph, graph)

  # calculate strongly connected components
  strongly_connected_components = calc_strongly_connected_components(translated_graph)

  return strongly_connected_components

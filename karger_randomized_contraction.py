#################
# Karger's Randomized Contraction Algorithm
#################
#   Description
#       Solves minimum cut of undirected graph through randomized consolidation of vertices
#       Derived from Coursera's Divide & Conquer Algorithms by Tim Roughgarden
#
#   Algorithm
#     While there are more than 2 vertices:
#         1. Pick a remaining edge (u, v) uniformly at random
#         2. Merge, or "contract", u and v into a single vertex
#         3. Remove self-loops [edges between the two vertices]
#
#   Runtime Complexity: O(mn^2) [where n is # of vertices and m is the # of edges]
#   Space Complexity: O(mn)
##########################
import random
import copy

def get_random_edge(graph):
  # take random key from graph dictionary
  u = graph.keys()[random.randint(0, len(graph) - 1)]

  # take random vertex from list of edges in vertex1
  v = graph[u][random.randint(0, len(graph[u]) - 1)]

  # return tuple of vertices
  return (u, v)

def contract(graph, edge):
    u, v = edge

    # copy edges from vertex 2 to vertex 1
    graph[u].extend(graph[v])

    # remove vertex 2 from dictionary
    del graph[v]

    # map references to vertex 2 to vertex 1
    for key, value in graph.iteritems():
      graph[key] = [u if vertex is v else vertex for vertex in graph[key]]

    # remove loops (edges to itself)
    graph[u] = [vertex for vertex in graph[u] if vertex is not u]

def min_cut(graph):
  # continue contractions until two vertices remain
  while len(graph) > 2:
    random_edge = get_random_edge(graph)
    contract(graph, random_edge)

  # return count of edges between remaining vertices
  return len(graph[graph.keys()[0]])

def min_cut_over_consecutive_trials(graph, trials):
  min_cut_results = []

  for i in range(trials+1):
    # run the minimum cut algorithm against a fresh graph
    result = min_cut(copy.deepcopy(graph))

    # save the results
    min_cut_results.append(result)

  # return the lowest min-cut
  return min(min_cut_results)

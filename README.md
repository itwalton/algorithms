# Algorithms

A collection of popular algorithms used to solve commonly-occurring problems in computer science.


## Karatsuba Integer Multiplication

### Original Karatsuba Recursion
**Description:** Divide & Conquer algorithm for efficient integer multiplication.

**Equation:** *10^n(ac) + 10^n/2(ad + bc) + bd*

**Time Complexity:** *O(n^2)*

**Example**

`original_karatsuba_recursion(123456789, 987654321) # => 121932631112635269`

### Optimized Karatsuba Recursion
**Description:** Leverages Gauss' Law to reduce recursive calls in Original Karatsuba Recursion by one.

**Equation:** *10^n(ac) + 10^(n/2)(ac - (ac + ad + bc + bd) - bd) + bd*

**Time Complexity:** *O(n^ln3)*

**Example**

`optimized_karatsuba_recursion(123456789, 987654321) # => 121932631112635269`

__Sources__
* [Karatsuba Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
* [Gauss' Law (Wikipedia)](https://en.wikipedia.org/wiki/Gauss%27_law)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Merge Sort

**Description:** Recursively split input array of length n into n arrays of length 1 and walk pointers over subarrays to "merge" them back together.

**Time Complexity:** *O(nlogn)*

**Space Complexity:** *O(n)*

**Example**

`merge_sort([1, 3, 5, 2, 4]) # => [1, 2, 3, 4, 5]`

__Sources__
* [Merge Sort (Wikipedia)](https://en.wikipedia.org/wiki/Merge_sort)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Quick Sort

**Description:** Recursively sort array by randomly chosen 'pivot' element.

**Time Complexity (worst case):** *O(n^2)*

**Time Complexity (best case):** *O(nlog(n))*

**Space Complexity:** *O(log(n))*

**Example**

`alist = [1, 3, 5, 2, 4]`

`print(quick_sort(alist, 0, len(alist)-1))`

__Sources__
* [Quicksort (Wikipedia)](https://en.wikipedia.org/wiki/Quicksort)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Randomized Selection

**Description:** Finds ith order statistic from unordered list by partitioning around random element and recursing over subset

**Algorithm**

1. Choose pivot p from A uniformly at random
2. Order elements around the pivot, so that elements < pivot are on the left and elements >= pivot are on the right
3. If the pivot index is < requested ith order, traverse the right subarray
4. If the pivot index is > requested ith order, traverse the left subarray
5. If the pivot index is the requested ith order, return pivot

**Time Complexity (worst case):** *O(n^2)*

**Time Complexity (best case):** *O(n)*

**Space Complexity:** *O(log(n))*

**Example**

`alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]`

`print(randomized_selection(alist, 5, 0, len(alist)-1)) # => 5`

__Sources__
* [Randomized Selection (YouTube)](https://www.youtube.com/watch?v=AHaaFVmAsvA)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Closest Pair of Points

### Brute-force Method
**Description:** Determine the closest pair of two-dimensional points

**Algorithm**

1. Iterate over every single set of points
2. Return closest pair in set

**Time Complexity:** *O(n^2)*

**Example**

`closest_pair_brute_force([(-12, -9), (-10, -4), (-1, -1), (1, 1), (7, 11), (9, 15)]) # => [(-1, -1), (1, 1)]`

### Divide & Conquer Method
**Description:** Optimize brute-force method by pre-sorting points by x and y axis, partitioning the points into quadrants and finding closest x, y, and split pairs then comparing.

**Algorithm**

1. Partition points P into Q, the left half, and R, the right half
2. Create arrays Qx, Qy, and Rx, Ry, the points in Q and R sorted by x/y coordinates respectively
3. Find the closest pair in left-sector recursively
4. Find the closest pair in the right-sector recursively
5. Find the closest split pair
6. Compare delta and return closest pair

**Time Complexity:** *O(nlog(n))*

**Example**

`P = [(-12, -9), (-10, -4), (-1, -1), (1, 1), (7, 11), (9, 15)]`

`Px = sort_points_by_axis(P, True)`

`Py = sort_points_by_axis(P, False)`

`closest_pair(Px, Py) # => [(1, 1), (1, 1)]`

__Sources__
* [Closest Pair of Points (Wikipedia)](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Counting Inversions

**Inversion:** # of pairs (i, j) of array indices with i < j & A[i] > A[j]

### Brute-force Method

**Description:** Iterate over every pair of indices and sum the inversions

**Time Complexity:** *O(n^2)*

**Example**

`count_inversions_brute_force([9, 1, 2, 3, 4]) # => 4`

### Divide & Conquer Method

**Description:** Optimize brute-force method by pre-sorting points by x and y axis, partitioning the points into quadrants and finding closest x, y, and split pairs then comparing.

**Inversion types**:

1. Left inversion (i, j < n/2) # => compute recursively
2. Right inversion (i, j > n/2) # => compute recursively
3. Split inversion (i <= n/2 <= j) # => compute by sorting left/right & counting right insertions

**Algorithm**

1. Recursively split array of length n into n subarrays of length 1
2. "Merge" array back together, counting inversions between left/right arrays

**Time Complexity:** *O(nlog(n))*

**Example**

`count_inversions([9, 1, 2, 3, 4]) # => {'list': [1, 2, 3, 4, 9], 'inversion_count': 4}`

__Sources__
* [Counting Inversions (YouTube)](https://www.youtube.com/watch?v=MxiQa22KrSQ)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Strassen's Matrix Multiplication

### Brute-force Method (Square)

**Description:** Iterate over every cell in both matrices and output the product

**Time Complexity:** *O(n^3)*

**Example**

`square_matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]) # => [[19, 22], [43, 50]]`

### Divide & Conquer Method (Square)

**Description:** Split matrices into 8 equal quadrants, recursively multiply the quadrants, and combine to output array

**Time Complexity:** *O(n^3)*

**Example**

`recursive_square_matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]) # => [[19, 22], [43, 50]]`

### Strassen's Algorithm

**Description:** Optimization of divide & conquer strategy, resulting in one less recursive call

**Algorithm**

1. Divide the input matrices A, B and output matrix C into n/2 * n/2 submatrices

2. Create 10 matrices S1-S10 of size n/2 * n/2 and the (+/-) of 2 matrices from Step #1

3. Recursively compute 7 matrix products P1-P7 each of size n/2 * n/2

4. Compute the desired submatrices C11, C12, C21, C22 (4 quatrices of output)

**Time Complexity:** *O(n^log7)*

**Example**

`recursive_square_matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]) # => [[19, 22], [43, 50]]`

__Sources__
* [Strassen's Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Strassen_algorithm)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Karger's Randomized Contraction Algorithm

**Description:** Determine the minimum cut of an undirected graph, to a considerable degree of confidence, by contracting an edge at random, repeated over many trials.

**Algorithm**

While there are more than 2 vertices:

1. Pick a remaining edge (u, v) uniformly at random
2. Merge, or "contract", u and v into a single vertex
3. Remove self-loops (i.e. edges between the two vertices)

**Time Complexity:** *O(mn^2), where n is the # of vertices and m is the # of edges*
**Space Complexity:** *O(mn)*

**Example**

`graph = { 1: [2, 3, 5], 2: [1, 3, 4], 3: [1, 2, 4, 5], 4: [2, 3, 5], 5: [1, 3, 4] }`

`min_cut_over_consecutive_trials(graph, 100) # => 3`

__Sources__
* [Karger's Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Karger%27s_algorithm)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Breadth-First Search

**Description:** Traverse graph in "layers" by exploring all adjacent vertices.

**Algorithm**

Starting at vertex s,

1. Mark s as explored

2. Initialize queue with s

3. While queue is not empty,
* remove the first node in queue
* iterate over it's edges
* marking the adjacent vertices as "explored"
* add adjacent vertex to queue


### Shortest Path

**Description:** Determine minimum # of edges between two vertices, s and v.

**Time Complexity:** *O(m+n), where n is the # of vertices and m is the # of edges*

**Example**

`graph = {
  's': ['a', 'b'],
  'a': ['s', 'c'],
  'b': ['s', 'c', 'd'],
  'c': ['a', 'b', 'd', 'e'],
  'd': ['b', 'c', 'e'],
  'e': ['c', 'd']
}`

`shortest_path(graph, 's', 'e') # => 3`

__Sources__

* [Breadth-First Search (Wikipedia)](https://en.wikipedia.org/wiki/Breadth-first_search)
* [Graph Search & Connectivity (Coursera)](https://www.coursera.org/learn/algorithms-graphs-data-structures)

## Depth-First Search

**Description:** Traverse graph by following edges to termination, backtracking only when necessary.

**Algorithm**

Starting at vertex s,

1. Mark s as explored

2. Initialize stack with s

3. While stack is not empty:
* iterate over edges (s, v)
* if v is unexplored, recursively call DFS with v


### Topological Ordering

**Description:** Sequence vertices in a directed, acyclic graph.

**Time Complexity:** *O(m+n)*

**Example:**

`graph = {
  's': ['u', 'w'],
  'u': ['x'],
  'w': ['x'],
  'x': []
}`

`topological_sort(graph) # => ['s', 'v', 'w', 'x'] OR ['s', 'w', 'v', x']`

__Sources__

* [Depth-first Search (Wikipedia)](https://en.wikipedia.org/wiki/Depth-first_search)
* [Graph Search & Connectivity (Coursera)](https://www.coursera.org/learn/algorithms-graphs-data-structures)


## Kosaraju's Two-Pass Algorithm

**Description:** Compute strongly connected components in a directed graph in linear time.

**Algorithm**

1. Reverse all arcs in the directed graph

2. Run DFS from every node in the graph, tracking finishing times

3. Translate vertices on the original graph by the finishing times in #2

4. Run DFS from every node in the graph, tracking leaders

**Time Complexity:** *O(m+n)*

**Example**

`graph = {
  1: [4, 7],
  2: [8],
  3: [9],
  4: [],
  5: [2],
  6: [3, 8],
  7: [9, 10],
  8: [5],
  9: [6],
  10: [1]
}`

`kosaraju(graph) # => {9: [8, 7, 9], 10: [10], 3: [2, 1, 3], 6: [5, 4, 6]}`

__Sources__

* [Kosaraju's algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm)
* [Graph Search & Connectivity (Coursera)](https://www.coursera.org/learn/algorithms-graphs-data-structures)
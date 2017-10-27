# Algorithms

A collection of popular algorithms used to solve commonly-occuring problems in computer science.


## Karatsuba Integer Multiplication

### Original Karatsuba Recursion
**Description:** Divide & Conquer algorithm for efficient integer multiplication.

**Equation:** *10^n(ac) + 10^n/2(ad + bc) + bd*

**Time Complexity:** *O(n^2)*

**Example:**

`original_karatsuba_recursion(123456789, 987654321) => 121932631112635269`

### Optimized Karatsuba Recursion
**Description:** Leverages Gauss' Law to reduce recursive calls in Original Karatsuba Recursion by one.

**Equation:** *10^n(ac) + 10^(n/2)(ac - (ac + ad + bc + bd) - bd) + bd*

**Time Complexity:** *O(n^ln3)*

**Example:**

`optimized_karatsuba_recursion(123456789, 987654321) => 121932631112635269`

__Sources__
* [Karatsuba Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
* [Gauss' Law (Wikipedia)](https://en.wikipedia.org/wiki/Gauss%27_law)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Merge Sort

**Description:** Recursively split input array of length n into n arrays of length 1 and walk pointers over subarrays to "merge" them back together.

**Time Complexity:** *O(nlogn)*

**Space Complexity:** *O(n)*

**Example:**

`merge_sort([1, 3, 5, 2, 4]) => [1, 2, 3, 4, 5]`

__Sources__
* [Merge Sort (Wikipedia)](https://en.wikipedia.org/wiki/Merge_sort)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)


## Quick Sort

**Description:** Recursively sort array by randomly chosen 'pivot' element.

**Time Complexity (worst case):** *O(n^2)*

**Time Complexity (best case):** *O(nlog(n))*

**Space Complexity:** *O(log(n))*

**Example:**

`alist = [1, 3, 5, 2, 4]`

`print(quick_sort(alist, 0, len(alist)-1))`

__Sources__
* [Quicksort (Wikipedia)](https://en.wikipedia.org/wiki/Quicksort)
* [Divide & Conquer Algorithms (Coursera)](https://www.coursera.org/learn/algorithms-divide-conquer)
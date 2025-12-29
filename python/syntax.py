# ==============================================================================
#  PYTHON MASTER SHEET FOR DSA & COMPETITIVE PROGRAMMING
#  Author: Gemini
#  Purpose: One file to rule them all. No external searches needed.
# ==============================================================================

import sys
import math
import random
import bisect
import heapq
from collections import deque, Counter, defaultdict, namedtuple
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate, chain, product

def fast_io():
    """ 
    1. FAST I/O TEMPLATE 
    Essential for competitive programming to prevent TLE (Time Limit Exceeded).
    """
    input = sys.stdin.readline  # Overwrite input() to be faster
    
    # Example Usage:
    # n = int(input())
    # arr = list(map(int, input().split()))
    # s = input().strip() # strip() removes newline characters
    print("Fast I/O initialized")

def python_basics_and_tricks():
    """ 2. CORE SYNTAX & ONE-LINERS """
    
    # --- Variables & Swapping ---
    a, b = 5, 10
    a, b = b, a  # Swap in O(1) without temp var
    x, y, z = [1, 2, 3] # Unpacking

    # --- Ternary Operator ---
    val = "Even" if a % 2 == 0 else "Odd"

    # --- Slicing (The most powerful tool) ---
    arr = [0, 1, 2, 3, 4, 5]
    rev = arr[::-1]      # Reverse: [5, 4, 3, 2, 1, 0]
    sub = arr[1:4]       # Slice: [1, 2, 3]
    step = arr[::2]      # Step: [0, 2, 4]
    
    # --- Looping Tricks ---
    # Enumerate: Get index and value
    for i, x in enumerate(['a', 'b', 'c']):
        pass # i=0, x='a' ...

    # Zip: Loop two arrays simultaneously
    names = ["Alice", "Bob"]
    scores = [90, 85]
    for n, s in zip(names, scores):
        pass # ('Alice', 90)

    # --- 2D Array Initialization (CRITICAL: Do NOT use [[0]*N]*M) ---
    rows, cols = 3, 4
    # Correct way: independent rows
    matrix = [[0] * cols for _ in range(rows)] 

    # --- Infinity ---
    max_val = float('inf')
    min_val = float('-inf')

def string_manipulation():
    """ 3. STRING MASTERY """
    s = "Hello World"
    
    # --- ASCII Conversions (Crucial for Hashing/Sliding Window) ---
    char_code = ord('a') # 97
    char_from_code = chr(97) # 'a'
    
    # --- String Operations ---
    reversed_str = s[::-1]
    is_alnum = s.isalnum() # Check if alphanumeric
    words = s.split() # Split by space
    joined = "-".join(words) # "Hello-World"
    
    # --- f-strings (Fastest formatting) ---
    name, age = "Kai", 25
    msg = f"{name} is {age} years old"

def list_comprehensions():
    """ 4. LIST COMPREHENSIONS (Speed & Brevity) """
    nums = [1, 2, 3, 4, 5]
    
    # Filter and Map in one line
    # [expression for item in list if condition]
    squares_even = [x**2 for x in nums if x % 2 == 0] 
    
    # Flatten a 2D matrix
    matrix = [[1, 2], [3, 4]]
    flat = [num for row in matrix for num in row] # [1, 2, 3, 4]

def data_structures_advanced():
    """ 5. ADVANCED DATA STRUCTURES (The DSA Toolkit) """

    # --- A. DEQUE (Doubly Linked List / Queue / Stack) ---
    # Use for BFS (O(1) popleft) or Sliding Window Maximum
    q = deque([1, 2, 3])
    q.append(4)      # Push right
    q.appendleft(0)  # Push left
    q.pop()          # Pop right
    q.popleft()      # Pop left (O(1)) -> Normal list pop(0) is O(N)
    q.rotate(1)      # Rotate elements

    # --- B. COUNTER (Hash Map for Frequency) ---
    # Use for Anagrams, Majority Element, Frequency counts
    arr = [1, 1, 2, 3, 3, 3]
    counts = Counter(arr) # {3: 3, 1: 2, 2: 1}
    most_common = counts.most_common(1)[0] # (Element, Count)
    # Subtract counts like set math
    c1 = Counter("aabb"); c2 = Counter("aa")
    remaining = c1 - c2 # {'b': 2}

    # --- C. DEFAULTDICT (Graph Adjacency List) ---
    # Never worry about KeyErrors again
    adj = defaultdict(list) # Default value is []
    adj['node1'].append('neighbor1') 
    
    int_map = defaultdict(int) # Default value is 0 (Good for sums)

    # --- D. HEAP (Priority Queue) ---
    # Python heaps are Min-Heaps by default.
    nums = [5, 1, 3]
    heapq.heapify(nums) # O(N) - Convert list to heap
    heapq.heappush(nums, 2) # O(log N)
    min_val = heapq.heappop(nums) # O(log N) -> Returns 1
    
    # TRICK: Max Heap -> Multiply by -1
    max_heap = []
    heapq.heappush(max_heap, -5)
    max_val = -heapq.heappop(max_heap)

    # --- E. SETS (Math Operations) ---
    s1, s2 = {1, 2, 3}, {3, 4, 5}
    union = s1 | s2
    intersection = s1 & s2
    difference = s1 - s2
    
    # --- F. NAMEDTUPLE (Clean Code for Coordinates/Structs) ---
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    # p.x, p.y is readable compared to p[0], p[1]

def algos_libraries():
    """ 6. BUILT-IN ALGORITHMS (Don't reinvent the wheel) """

    # --- A. BISECT (Binary Search) ---
    # Works on SORTED lists. O(log N)
    arr = [1, 3, 3, 3, 5, 7]
    idx_left = bisect.bisect_left(arr, 3)  # Returns 1 (First occurrence)
    idx_right = bisect.bisect_right(arr, 3) # Returns 4 (Insertion point after last 3)
    # Count occurrences of x: bisect_right - bisect_left
    
    # --- B. ITERTOOLS (Combinatorics) ---
    # Permutations: Order matters (ABC != CBA)
    perms = list(permutations([1, 2, 3], 2)) 
    
    # Combinations: Order doesn't matter (AB == BA)
    combs = list(combinations([1, 2, 3], 2))
    
    # Accumulate (Prefix Sums)
    nums = [1, 2, 3, 4]
    prefix_sum = list(accumulate(nums)) # [1, 3, 6, 10]

    # --- C. FUNCTOOLS (Caching & Sorting) ---
    # Memoization decorator for DP (Dynamic Programming)
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    # Custom Comparator for Sorting
    # Compare x and y: return -1 if x<y, 0 if x==y, 1 if x>y
    def compare(x, y):
        # Example: Sort by string length desc, then alphabetical
        if len(x) != len(y): return len(y) - len(x)
        return -1 if x < y else 1

    strs = ["apple", "bat", "car"]
    sorted_strs = sorted(strs, key=cmp_to_key(compare))

def math_and_bits():
    """ 7. MATH & BITWISE HACKS """
    
    # --- Math ---
    gcd_val = math.gcd(12, 18)
    lcm_val = (12 * 18) // gcd_val
    ceil_val = math.ceil(4.2) # 5
    floor_val = math.floor(4.8) # 4
    
    # --- Bitwise Operations (Fast) ---
    # x << 1  (Multiply by 2)
    # x >> 1  (Divide by 2)
    # x & 1   (Check if odd: 1=True, 0=False)
    # x & (x-1) (Turn off rightmost 1-bit / count set bits loop)
    # x ^ x   (0)
    
    # Check if power of 2:
    n = 16
    is_pow2 = (n > 0) and (n & (n - 1) == 0)

def recursion_limit():
    """ 8. SYSTEM CONFIGURATION """
    # Python default recursion limit is 1000. Increase for deep DFS/Graph problems.
    sys.setrecursionlimit(10**6)

def common_dsa_patterns():
    """ 9. COMMON PATTERNS & SNIPPETS """
    
    # --- Sorting with Lambda (Complex Sorts) ---
    data = [[1, 10], [1, 5], [2, 3]]
    # Sort by index 0 ascending, then index 1 descending
    data.sort(key=lambda x: (x[0], -x[1])) 
    
    # --- Graph: BFS (Template) ---
    def bfs(start_node, graph):
        queue = deque([start_node])
        visited = {start_node}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # --- Graph: DFS (Iterative - safer than recursion) ---
    def dfs_iterative(start_node, graph):
        stack = [start_node]
        visited = set()
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    stack.append(neighbor)

# ==============================================================================
#  CHEATSHEET SUMMARY
# ==============================================================================
# 1. Arrays/Strings: Use slicing [::-1], zip(), enumerate()
# 2. Hash Maps: Use collections.Counter, defaultdict
# 3. Queues/Stacks: Use collections.deque
# 4. Heaps: Use heapq (remember min-heap is default)
# 5. Sorting: Use data.sort(key=lambda x: ...)
# 6. Binary Search: Use bisect_left, bisect_right
# 7. DP: Use @lru_cache(None)
# ==============================================================================

if __name__ == "__main__":
    # Test any function here
    print("Python Master Sheet Loaded. Ready for DSA.")
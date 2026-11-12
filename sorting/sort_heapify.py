################----
# nums = [1, 3, 4, 10, 5]

# Index:  0  1  2   3  4
# Value:  1  3  4  10  5


#                  1 (0) 
#                 /     \
#              3 (1)   4 (2)
#              / \
#           10 (3) 5 (4)


# (i - 1) // 2

# Current index 3 with value 10, what is parent?
# idx = 3-1/2=1 with value 3

# 2 * i + 1
# Current index 1 value 3, who is left child
# idx=2 * 1 + 1 = 3 with value 10 is lhs node

# 2 * i + 2
# Current index 1 value 3, who is right child
# idx=2 * 1 + 2 = 4 with value 4 is rhs node

################----
# INITIAL HEAP

#              3 (0)
#             /     \
#          5 (1)    8 (2)

# Array: [3, 5, 8]


# STEP 1: Insert 2 at the END

#              3 (0)
#             /     \
#          5 (1)    8 (2)
#          /
#        2 (3)

# Array: [3, 5, 8, 2]

# New element index = 3
# Parent index = (3 - 1) // 2 = 1
# Parent value = heap[1] = 5

# Condition: Is 2 < 5?
# Result: TRUE

# ACTION: Swap 2 and 5.


# STEP 2: After swapping

#              3 (0)
#             /     \
#          2 (1)    8 (2)
#          /
#        5 (3)

# Array: [3, 2, 8, 5]

# Current element index = 1
# Parent index = (1 - 1) // 2 = 0
# Parent value = heap[0] = 3

# Condition: Is 2 < 3?
# Result: TRUE

# ACTION: Swap 2 and 3.


# STEP 3: After swapping

#              2 (0)
#             /     \
#          3 (1)    8 (2)
#          /
#        5 (3)

# Array: [2, 3, 8, 5]

# Current element index = 0

# Parent exists?
# NO → STOP.


# FINAL MIN HEAP

# Array: [2, 3, 8, 5]

#              2
#             / \
#            3   8
#           /
#          5





# --------
# Heap Sort / Top K with Heaps
# We need the three largest elements.
# Without a heap, you might scan the entire array each time.
# Crude:
# nums.sort(reverse=True)
# answer = nums[:k]

# What if we only need the largest 3 elements from a million numbers??
    # element at index i
    #           Parent (i)
    #            /     \
    #           /       \
    #    Left (2i+1)  Right (2i+2)


# MAXHEAP: Max Heap: [10, 8, 9, 4, 5, 3] Root MAX
#               10
#              /  \
#             8    9
#            / \  /
#           4   5 3

# MINHEAP: [1, 3, 2, 8, 5, 9] Root MIN
#                1
#               / \
#              3   2
#             / \  /
#            8   5 9


# Array = [3, 2, 1, 5, 6, 4]
# K = 3
# Top K Largest problem finds the K largest elements from an array using a heap.
# Top 3 Largest = [4, 5, 6]
# Initialize Min Heap
# 3 ,2, 1
#         1
#        / \
#       3   2
# 5 > 1 --> Remove 1 and insert 5.
#         2
#        / \
#       3   5
# 6 > 2 --> Remove 2 and insert 6
#         3
#        / \
#       6   5
# 4 > 3 Remove 3 and insert 4
#         4
#        / \
#       6   5
# Top 3 Largest = [4, 5, 6]

import heapq

# to find largest element u need heap that throw away small element from heap -- minheap has min element at root
def top_k_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k: #top element of heaps are small pop them
            heapq.heappop(min_heap)

    return min_heap

arr = [3, 2, 1, 5, 6, 4]

print(top_k_largest(arr, 3))

# ---
# TOP K LARGEST  ---> MIN HEAP
# TOP K SMALLEST ---> MAX HEAP

import heapq

def top_k_smallest(arr, k):
    max_heap = []

    for num in arr:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return sorted([-x for x in max_heap])


arr = [7, 10, 4, 3, 20, 15]

print(top_k_smallest(arr, 3))

##---------
## python support minheap by default
## to make it work we use -num and -sorted to get max heap behavior

# arr = [7, 10, 4, 3]
# [-7 -10 -4 -3]

#        -10 #-10 represents 10 - smallest element for mean heap but we getting 10 at top for maxheap
#        /  \
#      -7   -4
#      /
#    -3
# final tree transtioned to max_heap = [-7, -3, -4]
#      -7 
#     /  \
#    -3  -4
# [-x for x in max_heap]
# [7 3 4]
# sorted()
# [3, 4, 7] result
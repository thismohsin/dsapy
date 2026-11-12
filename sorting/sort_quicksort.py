
# 1. slow and scan start together
# 2. pivot is last element
# 3. scan keep going forward till last element (start at slow before that are in general addressed)
# 4  if scan element is less then pivot then swap small and scan element and move small and move scan
# such that we are create range of small element followed by range of high element
# 5. if not element left then swap pivot with slow

# [ Smaller elements | Unclassified elements | Pivot ]
#                    ↑                       ↑
#                    i slow                  j scans

# Smaller than pivot | Pivot | Greater than or equal to pivot
#####
def quick_sort(nums):

    def partition(low, high):
        pivot = nums[high]
        i = low

        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[high] = nums[high], nums[i]
        return i

    def quicksort(low, high):
        if low >= high:
            return

        p = partition(low, high)

        quicksort(low, p - 1)
        quicksort(p + 1, high)

    quicksort(0, len(nums) - 1)
    return nums
#
# INITIAL ARRAY

# Index:    0   1   2   3   4
# Value:    4   2   7   1   3
#           ↑               ↑
#           i             Pivot
#                           high

# pivot = 3
# i = 0


# ==================================================
# STEP 1: j = 0
# ==================================================

# Array:   [4, 2, 7, 1, 3]
#           ↑
#           j

# Condition:
# nums[j] < pivot
# 4 < 3 → FALSE

# ACTION:
# Do nothing.

# Why?
# 4 does not belong in the smaller group.

# i remains 0.


# ==================================================
# STEP 2: j = 1
# ==================================================

# Array:   [4, 2, 7, 1, 3]
#               ↑
#               j

# Condition:
# nums[j] < pivot
# 2 < 3 → TRUE

# ACTION:
# Swap nums[i] and nums[j].

# Swap nums[0] and nums[1].

# Before: [4, 2, 7, 1, 3]
# After:  [2, 4, 7, 1, 3]

# Now increment i.

# i = 1

# Why?
# 2 belongs to the smaller group.
# We have placed it at index 0.


# ==================================================
# STEP 3: j = 2
# ==================================================

# Array:   [2, 4, 7, 1, 3]
#                   ↑
#                   j

# Condition:
# nums[j] < pivot
# 7 < 3 → FALSE

# ACTION:
# Do nothing.

# i remains 1.


# ==================================================
# STEP 4: j = 3
# ==================================================

# Array:   [2, 4, 7, 1, 3]
#                       ↑
#                       j

# Condition:
# nums[j] < pivot
# 1 < 3 → TRUE

# ACTION:
# Swap nums[i] and nums[j].

# Swap nums[1] and nums[3].

# Before: [2, 4, 7, 1, 3]
# After:  [2, 1, 7, 4, 3]

# Increment i.

# i = 2


# ==================================================
# STEP 5: LOOP FINISHED
# ==================================================

# Array: [2, 1, 7, 4, 3]

# i = 2
# pivot = 3

# Now place the pivot at index i.

# Swap nums[i] and nums[high].

# Swap nums[2] and nums[4].

# Before: [2, 1, 7, 4, 3]
# After:  [2, 1, 3, 4, 7]

# ==================================================
# FINAL PARTITION
# ==================================================

# Index:    0   1   2   3   4
# Value:    2   1   3   4   7
#           └───┘   ↑   └───┘
#           < 3   Pivot   >= 3

# Pivot index = 2

# Return 2




##############################################################
###############################################################

# INITIAL CALL
# ============

# quicksort(0, 4)

# Array: [4, 2, 7, 1, 5]
#         └──── ACTIVE RANGE ────┘

# low = 0, high = 4
# Pivot = 5

#         partition(0, 4)
#                |
#                v
#         [4, 2, 1, 5, 7]
#                  ↑
#               Pivot
#             index = 3

#         Pivot is now FIXED.
#         It will never move again.

#         Divide into two ranges:

#         LEFT                  RIGHT
#         [4, 2, 1]             [7]
#         0 to 2                4 to 4

#                |
#         ┌──────┴──────┐
#         v             v

#    quicksort(0, 2)  quicksort(4, 4)
#         |                  |
#         |                  └── BASE CASE
#         |                      low >= high
#         |                      Return
#         |
#         v
#    partition(0, 2)

#    Array: [4, 2, 1, 5, 7]
#            └───┘
#    Pivot = 1

#    Partition result:

#    [1, 2, 4, 5, 7]
#     ↑
#    Pivot index = 0

#    Pivot is FIXED.

#    Divide remaining range:

#    LEFT                  RIGHT
#    Empty                 [2, 4]
#    0 to -1               1 to 2

#         |
#    ┌────┴─────┐
#    v          v

# quicksort(0,-1)  quicksort(1,2)
#      |                |
#      |                v
#      |           partition(1,2)
#      |                |
#      |           Array: [1, 2, 4, 5, 7]
#      |                       ↑  ↑
#      |                    Pivot
#      |                    value 4
#      |                    index 2
#      |
#      |           Divide:
#      |           LEFT       RIGHT
#      |           [2]        Empty
#      |           1 to 1     3 to 2
#      |             |          |
#      |          Return     Return
#      |
#    Return


# ALL RECURSIVE CALLS COMPLETE

# Final array:

# [1, 2, 4, 5, 7]
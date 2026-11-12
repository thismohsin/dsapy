# START:
# [5] [2] [4] [1]

# AFTER ONE PASS:
# [2] [4] [1] [5]

# Still NOT sorted!

# ---
# i   = WHICH ROUND AM I ON?

# j   = WHICH TWO POSITIONS AM I COMPARING?

# if  = SHOULD I SWAP THESE VALUES?

# --
# Why does j use range(n - 1 - i)?
# -i : element sorted and move to RHS in comparison round
# -1: nums[j] > nums[j + 1] -- out of index
#     0       1       2       3
#     0-1     1-2     2-3


nums = [5, 2, 4, 1]
n = len(nums)

# OUTER LOOP: Controls the number of passes
for i in range(n):

    # Each completed pass fixes one largest element
    # at the right side of the array.

    # INNER LOOP: Compare adjacent elements
    # Reduce comparisons because right-side elements
    # are already in their correct positions.
    for j in range(n - 1 - i):

        # CASE 1: Left value is greater than right value
        # Ascending order is violated, so swap.
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)

# Output: [1, 2, 4, 5]


### -----------
# Two Pointers After Sorting
# nums = [8, 1, 6, 3, 5, 2]
# target = 8
# We need to find two numbers whose sum equals 8.
# Sort: 
# Index:    0   1   2   3   4   5
# Array:   [1] [2] [3] [5] [6] [8]
#           L                   R

# [left has small element ----- right has largest element]
# total == target #found 
# total < target # move left+
# total > target # move right+

def two_sum(nums, target):

    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:

        total = nums[left] + nums[right]

        # CASE 1: Sum is too small
        if total < target:
            left = left + 1

        # CASE 2: Sum is too large
        elif total > target:
            right = right - 1

        # CASE 3: Exact sum found
        elif total == target:
            return [nums[left], nums[right]]

    return []



###----
# Cyclic Sort is an array sorting algorithm 
# used when array elements are in a known range, usually 1 to n

# arr = [3, 5, 2, 1, 4]
# o/p = [1, 2, 3, 4, 5]

# Index:  0  1  2  3  4
# Array: [3, 5, 2, 1, 4]

# Number = 1  → Index = 0
# Number = 2  → Index = 1
# Number = 3  → Index = 2
# Number = 4  → Index = 3
# Number = 5  → Index = 4
# correct_index = arr[i] - 1

# 3 belongs at index 2.
# Swap index 0 and index 2.
# Before: [3, 5, 2, 1, 4]
# After:  [2, 5, 3, 1, 4]


# nums[i] != nums[nums[i] - 1]
# value != value[expectedposition] where expectedposition = num[i]-1

# while looping i am getting element
# i am check what is expectedposition for this element by value-1
# if not then we swap

# Most important concept: Why don't we increment i after swapping?
# Because swapping changes the number at the current index.
# We must check that new number before moving forward. forver unless correct

# if correct then only increment idx will move



# [5, 3, 1, 4, 2]
#  ↓ Swap 5 and 2
# [2, 3, 1, 4, 5]
#  ↓ Swap 2 and 3
# [3, 2, 1, 4, 5]
#  ↓ Swap 3 and 1
# [1, 2, 3, 4, 5]
#  ↓
# Index 0 is correct.
# NOW increment index.


def cyclic_sort(arr):
    i = 0

    while i < len(arr):

        correct_index = arr[i] - 1 # take element-1 => position where it belong

        if arr[i] != arr[correct_index]: # if element is not placed at correct index element

            arr[i], arr[correct_index] = (
                arr[correct_index], arr[i] # then swap
            )

        else:
            i += 1

    return arr


arr = [3, 5, 2, 1, 4]

print(cyclic_sort(arr))

#Dutch National Flag (DNF) / Three-Way Partition
# All 0s come first.
# All 1s come in the middle.
# All 2s come last.


# INITIAL STATE
# Index:   0  1  2  3  4  5
# Array:  [2, 0, 2, 1, 1, 0]
#          L
#          M              H

# ------------------------------------------------
# STEP 1: nums[mid] == 2
# Action: Swap mid with high; high--

# Before: [2, 0, 2, 1, 1, 0]
#          L              H
#          M

# After:  [0, 0, 2, 1, 1, 2]
#          L           H
#          M

# NOTE: M DOES NOT MOVE.
#       New element at M is 0, still needs checking.

# ------------------------------------------------
# STEP 2: nums[mid] == 0
# Action: Swap low with mid; low++, mid++

# Before: [0, 0, 2, 1, 1, 2]
#          L
#          M           H

# After:  [0, 0, 2, 1, 1, 2]
#             L
#             M        H

# NOTE: Both L and M move right.

# ------------------------------------------------
# STEP 3: nums[mid] == 2
# Action: Swap mid with high; high--

# Before: [0, 0, 2, 1, 1, 2]
#             L
#             M        H

# After:  [0, 0, 1, 1, 2, 2]
#             L     H
#             M

# NOTE: M DOES NOT MOVE.
#       New element at M is 1, still needs checking.

# ------------------------------------------------
# STEP 4: nums[mid] == 1
# Action: mid++

# Before: [0, 0, 1, 1, 2, 2]
#             L
#             M     H

# After:  [0, 0, 1, 1, 2, 2]
#             L
#                M  H

# NOTE: Only M moves right.

# ------------------------------------------------
# STEP 5: nums[mid] == 1
# Action: mid++

# Before: [0, 0, 1, 1, 2, 2]
#             L
#                M  H

# After:  [0, 0, 1, 1, 2, 2]
#             L
#                   M
#                   H

# NOTE: M has crossed H.

# ------------------------------------------------
# STOP CONDITION: mid > high

# FINAL ARRAY:
# [0, 0, 1, 1, 2, 2]

# We find mid by changing low and high
# condition      | swap       | change
# -------------------------------------
# nums[mid] == 0 | low ↔ mid  | low++, mid++
# nums[mid] == 1 | None       | mid++
# nums[mid] == 2 | mid ↔ high | high--

def sortColors(nums):

    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:

            # 0 belongs on left
            # Swap and move both pointers
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:

            # 1 belongs in middle
            # Already correct, just move mid
            mid += 1

        else:

            # 2 belongs on right
            # Swap with high and shrink right boundary
            # Do NOT move mid: incoming element is unknown
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

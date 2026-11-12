# Dutch National Flag / Three-Way Partition

nums = [2, 0, 2, 1, 1, 0]
[0, 0, 1, 1, 2, 2]


# [ 0s | 1s | UNKNOWN | 2s ]

# What does each pointer do?
# 1. low
# Marks the boundary for zeros.
# When we find 0, we swap it with nums[low].
# Increment low.
# 2. mid
# Examines the current element.
# Decides what action to take.
# Sometimes increments and sometimes stays in place.
# 3. high
# Marks the boundary for twos.
# When we find 2, we swap it with nums[high].
# Decrement high.

def sort_colors(nums):

    low = 0
    mid = 0
    high = len(nums) - 1

    #mid is scanner all we moving mid and compare with low and high
    while mid <= high:

        # Condition 1: Current element is 0
        if nums[mid] == 0:

            nums[low], nums[mid] = nums[mid], nums[low]

            low += 1
            mid += 1

        # Condition 2: Current element is 1
        elif nums[mid] == 1:

            mid += 1

        # Condition 3: Current element is 2
        elif nums[mid] == 2:

            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

    return nums


nums = [2, 0, 2, 1, 1, 0]

print(sort_colors(nums))

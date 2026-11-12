# [1, 2, 3, 4, 5, 6, 7]
# rotate
# [4, 5, 6, 7, 1, 2, 3]
# We need to find the minimum value: 1.
# 7>1<2 is point of break
# Values before the rotation break are larger.
# Values after the rotation break are smaller.
# The minimum is at the rotation break.
# Our goal: Find where the ascending order starts again.

# Let compare mid with right 

# 6 7 1 2 3 -- 1M < 3H or 2M < 3H  1234 doesnt guarantee correct answer so we keep moving mid=high unless found 1
#           -- 6M > 3H or 7M > 3H  46713 this says answer is in left


# nums = [1, 2, 3, 4, 5, 6]
# Index:   0   1   2   3   4   5
# Array:  [1] [2] [3] [4] [5] [6]
#          L       M           R
# nums[mid] <= nums[right]
# 3 <= 6  # True 
# high = mid  # high = 2 -- 1st case move right to mid

# nums = [6, 7, 8, 1, 2, 3, 4]
# 1 <= 4  # True
# high = mid

# Index:   0   1   2   3   4   5   6
# Array:  [6] [7] [8] [1] [2] [3] [4]
#          L           H   x   x   x
# 7 > 1  # True --- case 2 move left to mid

# Index:   0   1   2   3   4   5   6
# Array:  [6] [7] [8] [1] [2] [3] [4]
#          x   x   L   H   x   x   x

# 8 > 1  # True

# Index:   0   1   2   3   4   5   6
# Array:  [6] [7] [8] [1] [2] [3] [4]
#          x   x   x   L
#                      H


class Solution:
    def findMin(self, nums: list[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            # Minimum is in the right half
            if nums[mid] > nums[high]:
                low = mid + 1

            # Minimum is at mid or in the left half
            else:
                high = mid

        return nums[low]


# [4, 5, 6, 7 | 1, 2, 3]
#               ^
#              MIN

# Index:   0   1   2   3   4   5   6
# Array:  [4] [5] [6] [7] [1] [2] [3]
#          L           M           H

# Left half: [4, 5, 6, 7] sorted 
# Right half: [1, 2, 3] sorted 

# # LOOK MID AND HIGH
# # R1
# nums[mid]  = 7
# nums[high] = 3
# MID > HIGH : 7 > 3, TRUE The rightmost value is smaller than the middle value.
# ******* rotation break is somewhere in RIGHT
# # R2
# nums = [7, 8, 9, 1, 2, 3, 4, 5]
# Index:   0   1   2   3   4   5   6   7
# Array:  [7] [8] [9] [1] [2] [3] [4] [5]
#          L           M               H

# nums[mid] = 1
# nums[high] = 5

# MID > HIGH:  1 < 5 FALSE rotation break is somewhere in LEFT

# #####
# CASE 1: MID > HIGH

# [4, 5, 6, 7 | 1, 2, 3]
#              M       H

# Minimum is RIGHT of MID.
# low = mid + 1


# CASE 2: MID < HIGH
# [7, 8, 9 | 1, 2, 3, 4, 5]
#           M               H

# Minimum is AT MID or LEFT of MID.
# high = mid
# The unsorted section contains the rotation break and therefore the minimum.

def findMin(nums):

    low = 0
    high = len(nums) - 1

    while low < high:

        mid = (low + high) // 2

        # there has to be no equal checks we dont know what we finding
        if nums[mid] < nums[high]:
            high = mid

        else:
            low = mid + 1

    return nums[low]


# ***************
# Instead of asking:
# "Which half is unsorted?"

# Ask:
# "Is MID smaller or greater than HIGH?"

# Why?
# Because this comparison tells us which side can contain the minimum.

# CASE 1: IF: MID is smaller than HIGH
# Array: [7, 9 | 1, 2, 3, 4, 5, 6]
#               M               H
# 1 < 6  TRUE then check between LHS + mid 7 9 1

# CASE 2: ELSE: MID is greater than HIGH
# Array: [4, 5, 6, 7 | 9, 1, 2, 3]
#               M                   H
# 6 > 3  TRUE then check between RHS  9 1 2 3
# ***************

        #             START
        #               |
        #    [4, 5, 6, 7, 9, 1, 2, 3]
        #     L           M           H
        #                 |
        #      Is nums[MID] > nums[HIGH]?
        #                7 > 3
        #             /       \
        #           YES        NO
        #            |          |
        #            |       [NOT TAKEN]
        #            |
        #   MINIMUM IS RIGHT OF MID
        #   ELIMINATE LEFT INCLUDING MID
        #            |
        #        KEEP RIGHT
        #         [1, 2, 3]
        #          L  M  H
        #             |
        #  Is nums[MID] > nums[HIGH]?
        #            2 > 3
        #           /     \
        #         YES      NO
        #          |        |
        #      [NOT TAKEN]  |
        #                   |
        #      MINIMUM IS AT MID OR LEFT
        #      ELIMINATE EVERYTHING RIGHT OF MID
        #                   |
        #               KEEP LEFT
        #                [1, 2]
        #                 L  H
        #                   |
        #             FIND MIN = 1
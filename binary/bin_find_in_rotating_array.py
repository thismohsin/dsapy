# [?] [?] [?] [?] [?] [?] [?]
#  L           M           H

# Left half:  UNSORTED
# Right half: UNSORTED

# For the left half to be unsorted, the rotation break must be somewhere between low and mid.

# For the right half to be unsorted, another rotation break must be somewhere between mid and high.

# That would require two rotation breaks.

# But a single rotation of an ascending-sorted array creates at most one break.

# Therefore, both halves cannot be unsorted.
#Index:   0   1   2   3   4   5   6   7
# Array:  [7] [8] [9] [1] [2] [3] [4] [5]
#          L               M               H
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        #edge case Input = [8, 9, 1, 2, 3, 4, 5]
        #Index:   0   1   2   3   4   5   6
        #Array:  [8] [9] [1] [2] [3] [4] [5]
        #         L           M           H
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # LEFT HALF SORTED
            if nums[low] <= nums[mid]:

                # Target belongs to left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Target does not belong to left half
                else:
                    low = mid + 1

            # LEFT HALF UNSORTED
            elif nums[low] > nums[mid]:
                #Left half is unsorted:
                #[8] [9] [1] [2]
                #└────────────┘
                #    UNSORTED

                # RIGHT HALF SORTED
                # [2] [3] [4] [5]
                if nums[mid] < nums[high]:

                    # Target belongs to right half
                    if nums[mid] < target <= nums[high]:
                        low = mid + 1

                    # Target does not belong to right half
                    else:
                        high = mid - 1

                # RIGHT HALF UNSORTED
                else:
                    return -1

        return -1


#
# [7, 8, 9, 1, 2, 3, 4, 5]
#  7   8   9 | 1   2   3   4   5
#             ^
#        Rotation break
# --------------------
# Index:   0   1   2   3   4   5   6   7
# Array:  [7] [8] [9] [1] [2] [3] [4] [5]
#          L           M               H
# The left half is unsorted.
# The right half is sorted.

# Index:   0   1   2   3   4   5   6   7
# Array:  [4] [5] [7] [8] [1] [2] [3] [9]
#          L           M               H

# The left half is sorted.
# The right half is unsorted.
# --------------------
# LEFT POV : nums[low] <= nums[mid] KEY CONDITION
# # Array:  [4] [5] [7] [8]
# #          L           M
# left is sorted  if mid is greater then low  ==> 4 <= 8 TRUE
# Array:  [7] [8] [9] [1]
#          L           M
# left is unsorted  if mid is smaller then low ==> 7 <= 1 FALSE

# IF LEFT IS SORTED GR8
# IF LEFT IS UNSORTED THEN RIGHT IS SORTED
# --------------------
# left sorted, if we know which section is sorted then we can check if value is in this range?
# nums[low] <= target <= nums[mid]

# if we found
# move high to mid -1
# if we didnt find
# move low to mid + 1
# --------------------
# NOW APPLY SAME LOGIC FOR
# RIGHT POV
# RIGHT POV : nums[mid] <= nums[high] KEY CONDITION
# # Array:  [2] [3] [4] [5]
# #          M           H
# right is sorted  if mid is smaller then high  ==> 2 <= 5 TRUE
# Array:  [2] [3] [4] [1]
#          M           H
# right is unsorted  if mid is greater then high ==> 2 <= 1 FALSE

# IF RIGHT IS SORTED GR8
# IF RIGHT IS UNSORTED THEN LEFT IS SORTED
# --------------------
# if we know which section is sorted then we can check if value is in this range?
# nums[mid] <= target <= nums[high]

# if we found
# move low to mid + 1
# if we didnt find
# move high to mid - 1
# --------------------




    #                 START
    #                  |
    #           Calculate MID
    #                  |
    #       nums[low] <= nums[mid]?
    #              /         \
    #           TRUE         FALSE
    #            |             |
    #      LEFT SORTED    RIGHT SORTED
    #            |             |
    #   nums[low] <=      nums[mid] <=
    #   target <=         target <=
    #   nums[mid]?        nums[high]?
    #       /   \             /   \
    #    TRUE   FALSE       TRUE   FALSE
    #      |      |           |      |
    #    KEEP   KEEP        KEEP   KEEP
    #    LEFT   RIGHT       RIGHT  LEFT
    #      |      |           |      |
    #  high =  low =       low =   high =
    #  mid-1   mid+1       mid+1   mid-1



    #              START
    #                |
    #         mid = (0 + 7) // 2
    #                |
    #             mid = 3
    #                |
    #       nums[0] <= nums[3]?
    #            7 <= 1
    #              FALSE
    #                |
    #          RIGHT SORTED
    #                |
    #    nums[3] <= target <= nums[7]?
    #           1 <= 9 <= 5
    #              FALSE
    #                |
    #        ELIMINATE RIGHT
    #                |
    #          high = mid - 1
    #                |
    #             high = 2
#     Index:   0   1   2   3   4   5   6   7
#     Array:  [7] [8] [9] [1] [2] [3] [4] [5]
#          L   M   H   x   x   x   x   x
#          <--- KEEP ---> <--- ELIMINATED --->


def search(nums, target):
    #We identify a sorted half and ask:
    #Is my target inside this sorted range?

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = (low + high) // 2

        # Target found
        if nums[mid] == target:
            return mid

        # CASE 1: Left half is sorted
        if nums[low] <= nums[mid]:

            # Target could be inside the sorted left half
            if nums[low] <= target <= nums[mid]:
                high = mid - 1

            # Target must be in the right half
            else:
                low = mid + 1

        # CASE 2: Right half is sorted
        else:

            # Target could be inside the sorted right half
            if nums[mid] <= target <= nums[high]:
                low = mid + 1

            # Target must be in the left half
            else:
                high = mid - 1

    return -1

# *****
#                   IDENTIFY SORTED HALF
#                            |
#                   Is LEFT half sorted?
#                      /           \
#                    YES            NO
#                     |              |
#              Check target     RIGHT must be
#              in LEFT range    sorted
#                     |              |
#               +-----+-----+   Check target
#               |           |   in RIGHT range
#             YES           NO
#               |           |
#           Keep LEFT    Keep RIGHT

# Target = 2
# nums = [4, 5, 6, 7, 9, 1, 2, 3]

#                   START
#                     |
#           [4, 5, 6, 7, 9, 1, 2, 3]
#            L           M           H
#                        |
#                     MID = 7
#                        |
#                Is LEFT sorted?
#                   4 <= 7
#                  /       \
#                YES        NO
#                 |          |
#                 |       (not taken)
#                 |
#           LEFT = [4, 5, 6, 7]
#                 |
#          Is target 2 in [4, 7]?
#                 |
#               /   \
#             YES    NO
#              |      |
#              |      |
#         KEEP LEFT  ELIMINATE LEFT
#              |      |
#        Search LEFT  KEEP RIGHT
#              |      |
#         [4, 5, 6, 7] |
#              |      |
#         Target found?|
#           /    \    |
#         YES    NO   |
#          |      |   |
#       RETURN   X    |
#         2      STOP |
#                     |
#               RIGHT = [9, 1, 2, 3]
#                     |
#               Continue search
#                     |
#              [9, 1, 2, 3]
#               L   M   H
#                   |
#                 MID = 1
#                   |
#            Is LEFT sorted?
#               9 <= 1
#              /      \
#            YES       NO
#             |         |
#             |    RIGHT SORTED
#             |     [1, 2, 3]
#             |         |
#             |   Is 2 in [1, 3]?
#             |         |
#             |        YES
#             |         |
#             |    KEEP RIGHT
#             |         |
#             |      [2, 3]
#             |         |
#             |     Continue
#             |         |
#             |      FIND 2
#             |         |
#             |    RETURN INDEX 6
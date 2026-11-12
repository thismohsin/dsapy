
# arr = [1, 3, 5, 6]
# target = 2


# Before insertion:

# Index:  0  1  2  3
# Array:  1  3  5  6

# After insertion:

# Index:  0  1  2  3  4
# Array:  1  2  3  5  6
#           ^
#        Insert at index 1

# Why index 1?

# Because:

#     Everything before index 1 is smaller than 2.

#     Everything from index 1 onward is greater than or equal to 2


# **** GOAL.  Our goal: Find the first* index where arr[index] >= target.
# Our mental model:

#     If arr[mid] < target, target belongs to the right. (mid is smaller then target then move left and answer is in right section)

#     If arr[mid] >= target, mid might be the answer, but an earlier valid position might exist. Move left.

# we dont need variable low hold position of first index found

# before_element < x < after_element
# if arr[mid] > x You move the right boundary (high) to mid - 1. This effectively shifts your search focus to the left half of the remaining array.
# if arr[mid] < x ou move the left boundary (low) to mid + 1. This effectively shifts your search focus to the right half of the remaining array.
# arr[mid] == x falls into the else block, which moves high = mid - 1. This naturally pushes the search leftward to find the first occurrence

#  0  1  2  3
# [1, 3, 5, 6] | 2k
# l=0 h=3 : 3<2k : move high to mid+1 = idx0 : right wall|high
# l=0 h=0 : 1<2k : move low to mid+1 = idx1 : left wall|low
# l=1 h=0 : l>h  : exit


def search_insert(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        #5m <10t = page mid 5 is smaller then target then my ans is in right n i move low to mid
        if arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return low

# ***
#                 [2, 4, 6, 8, 10]

#                   CHECK MID
#                       |
#               Is MID < TARGET?
#                  /         \
#                YES          NO
#                 |            |
#            TOO SMALL      BIG ENOUGH
#                 |            |
#           Search RIGHT   Save candidate
#                              |
#                         Search LEFT



#                          START
#                            |
#                     [2, 4, 6, 8, 10]
#                            |
#                       MID = 6
#                            |
#                         6 < 7? 7 is target and mid < target
#                        /      \
#                     YES        NO
#                      |          |
#                   TOO SMALL  BIG ENOUGH
#                      |          |
#                   MOVE RIGHT  SAVE CANDIDATE
#                      |          |
#                 [8, 10]      SEARCH LEFT
#                    |             |
#                 MID = 8          |
#                    |             |
#                  8 < 7?          |
#                 /     \          |
#               YES      NO        |
#                |        |        |
#                |    SAVE INDEX 3 |
#                |        |        |
#                |    SEARCH LEFT  |
#                |        |        |
#                +--------+--------+
#                         |
#                   low = 3
#                   high = 2
#                         |
#                        STOP
#                         |
#                  ANSWER = INDEX 3

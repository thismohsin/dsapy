# First and Last Occurrence
# ans = mid
# high = mid - 1

# Last occurence
# ans = mid
# low = mid + 1
#https://www.youtube.com/watch?v=Y7LiLNdayF0
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1       
            # Continue searching in left side by moving right to mid - 1,
            # as we have answer on mid recorded -- search LEFT** 1 {2}2[2]2 4

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return ans

def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1        # search RIGHT **
            # Continue searching in right side by moving low to mid + 1,
            # as we have answer on mid recorded -- search RIGHT** 1 2[2]2{2} 4

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return ans


###
# this is different then upperbound and lower bound
# [1 2 2 2 4 ]
#  0 1 2 3 4    

# idx = wrong 1 - 3 = 2 (occurent logic)
# idx = right 1 - 4 = 3 (bound logic)
# fix occurent = right = 1-3+1 = 3 ---> fix + 1

def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    if first == -1:
        return 0

    return last - first + 1


#****
            #   [1, 2, 2, 2, 2, 4]
            #    L        M        H
            #             |
            #          MID = 2
            #             |
            #        MID == TARGET
            #             |
            #            YES
            #             |
            #       SAVE ans = 2
            #             |
            #  Could another 2 exist LEFT?
            #             |
            #            YES
            #             |
            #       SEARCH LEFT
            #             |
            #      [1, 2, 2]
            #       L  H


            #   [1, 2, 2, 2, 2, 4]
            #    L        M        H
            #             |
            #          MID = 2
            #             |
            #        MID == TARGET
            #             |
            #            YES
            #             |
            #       SAVE ans = 2
            #             |
            #  Could another 2 exist RIGHT?
            #             |
            #            YES
            #             |
            #       SEARCH RIGHT
            #             |
            #        [2, 2, 4]
            #         L  H
# nums = [2, 4, 7, 5, 3]

#           7       PEAK
#          / \
#         /   \
#        /     \
#       4       5
#      /         \
#     2           3

#  INCREASING   DECREASING

# one side increasing and other side decreasing and peak is between increasing decreasing

# **
# arr[mid] < arr[mid+1] Uphill -- peak is on right -- retain right by moving low to mid : low=mid+1
# arr[mid] > arr[mid+1] Downhill -- peak is on left -- retain left by moving high to mid : high:mid

# while going uphill low=mid+1
# while going down hill high=mid (not mid-1 as we may loose peak)


#               START
#                 |
#        [2, 4, 7, 5, 3]
#         L     M       H
#               |
#        arr[M] < arr[M+1]?
#               4 < 7
#              /     \
#            YES      NO
#             |    [NOT TAKEN]
#             |
#        UPHILL → RIGHT
#        Eliminate [2, 4]
#        Retain  [7, 5, 3]
#             |
#        low = mid + 1
#        low = 2, high = 4
#             |
#         [7, 5, 3]
#          L  M  H
#             |
#        arr[M] < arr[M+1]?
#               5 < 3
#              /     \
#            YES      NO
#        [NOT TAKEN]   |
#                      |
#                 DOWNHILL
#                 Keep MID and LEFT
#                 Eliminate [3]
#                      |
#                 high = mid
#                 high = 3
#                      |
#                 [7, 5]
#                  L  H
#                      |
#                 low == high?
#                      |
#                     NO

    #          Compare MID and MID+1
    #                    |
    #           +--------+--------+
    #           |                 |
    #        UPHILL            DOWNHILL
    #           |                 |
    #    arr[mid] <          arr[mid] >
    #    arr[mid+1]          arr[mid+1]
    #           |                 |
    #    Peak is RIGHT       Peak is MID
    #      or beyond          or LEFT
    #           |                 |
    #    low = mid + 1       high = mid
    #           |                 |
    #           +--------+--------+
    #                    |
    #              low == high
    #                    |
    #               PEAK INDEX


# arr = [2, 4, 7]
# low = 0 : high = 2 : mid = 1
# arr[mid] < arr[mid + 1]
# 4 < 7 : peak is on right
# low = mid + 1 : low=2 hight=2
# while low < high:
# 2 < 2  FALSE return



def findPeakElement(arr):

    low = 0
    high = len(arr) - 1

    while low < high:

        mid = (low + high) // 2

        # CASE 1: Going uphill
        if arr[mid] < arr[mid + 1]:
            low = mid + 1

        # CASE 2: Going downhill
        elif arr[mid] > arr[mid + 1]:
            high = mid

    return low


arr = [2, 4, 7, 5, 3]

peak_index = findPeakElement(arr)

print("Peak Index:", peak_index)
print("Peak Value:", arr[peak_index])


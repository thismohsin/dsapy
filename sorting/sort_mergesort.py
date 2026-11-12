##### -------
# [9, 12, 18, 25, 27, 31, 38, 43]
# merge_sort([38, 12, 27, 43])
#           |
#           +--> merge_sort([38, 12])
#           |             |
#           |             +--> merge_sort([38])
#           |             +--> merge_sort([12])
#           |             |
#           |             +--> merge([38], [12])
#           |
#           +--> merge_sort([27, 43])
#                         |
#                         +--> merge_sort([27])
#                         +--> merge_sort([43])
#                         |
#                         +--> merge([27], [43])

#           |
#           +--> merge([12, 38], [27, 43])

def merge_sort(arr):

    # BASE CASE:
    # A single element is already sorted.
    if len(arr) <= 1:
        return arr

    # STEP 1: Divide
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # STEP 2: Merge
    return merge(left, right)


def merge(left, right):

    i = 0
    j = 0
    temp = []

    # CASE 1: Both arrays have elements
    while i < len(left) and j < len(right):

        # CASE 1A: Left element is smaller
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1

        # CASE 1B: Right element is smaller
        elif left[i] > right[j]:
            temp.append(right[j])
            j += 1

    # CASE 2: Left array still has elements
    while i < len(left):
        temp.append(left[i])
        i += 1

    # CASE 3: Right array still has elements
    while j < len(right):
        temp.append(right[j])
        j += 1

    return temp


arr = [38, 12, 27, 43, 9, 31, 18, 25]

result = merge_sort(arr)

print(result)
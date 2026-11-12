
# arr = [4, 2, 2, 8, 3, 3, 1]
# [1, 2, 2, 3, 3, 4, 8]

# For example:
# 1 appears once.
# 2 appears twice.
# 3 appears twice.
# 4 appears once.
# 8 appears once.

# max_val = 8
# count = [0] * 9 # create new array fill it with 0 and why 9 and not 8 -- to represent 8 value u will be on 9 idx
# Number:    0  1  2  3  4  5  6  7  8
# Count:    [0][0][0][0][0][0][0][0][0]
# count[arr[i]] += 1

# INPUT:
# Index:      0   1   2   3   4   5   6
# Array:     [4] [2] [2] [8] [3] [3] [1]

# STEP 1: arr[0] = 4
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][0][0][0][1][0][0][0][0]

# STEP 2: arr[1] = 2
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][0][1][0][1][0][0][0][0]


# STEP 3: arr[2] = 2
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][0][2][0][1][0][0][0][0]


# STEP 4: arr[3] = 8
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][0][2][0][1][0][0][0][1]

# STEP 5: arr[4] = 3
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][0][2][1][1][0][0][0][1]

# STEP 6: arr[5] = 3
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][0][2][2][1][0][0][0][1]

# STEP 7: arr[6] = 1
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][1][2][2][1][0][0][0][1]

# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][1][2][2][1][0][0][0][1]

# reconstruct
# Number:     0  1  2  3  4  5  6  7  8
# Count:     [0][1][2][2][1][0][0][0][1]

# Output:
# [1] [2] [2] [3] [3] [4] [8]

def counting_sort(arr):

    if len(arr) == 0:
        return arr

    # Find maximum value
    max_val = max(arr)

    # Create frequency array
    count = [0] * (max_val + 1)

    # STEP 1: Count frequencies
    for num in arr:
        count[num] += 1

    # STEP 2: Reconstruct sorted array
    result = []

    for num in range(len(count)):
        # Write each number according to its frequency
        if count[num] > 0:
            for _ in range(count[num]):
                result.append(num)

    return result


arr = [4, 2, 2, 8, 3, 3, 1]

print(counting_sort(arr))
# [1, 2, 2, 3, 3, 4, 8]



#Fixed window: Shrink when size exceeds k.
#fixed window + sum subset + max
# nums = [2, 1, 5, 1, 3, 2]
# k = 3        sum
# [2, 1, 5]  → 8
# [1, 5, 1]  → 7
# [5, 1, 3]  → 9
# [1, 3, 2]  → 6
#           max = 9
#Variable window: Shrink when the window violates a problem-specific condition.
# Longest subarray with sum ≤ 8
# Longest valid subarray:
# [1, 5, 1]  → sum = 7, length = 3
# [1, 3, 2]  → sum = 6, length = 3
#                     maxLen = 3


# ------------------------
# Longest subarray with sum ≤ 8
# nums = [2, 1, 5, 1, 3, 2]
# limit = 8
# STAGE 1: Expand → Add 2
#          L
#          R
#          |
#        [ 2,  1,  5,  1,  3,  2 ]
#          └───┘
#          sum = 2
#          length = 1
#          maxLen = 1


# STAGE 2: Expand → Add 1
#          L   R
#          |   |
#        [ 2,  1,  5,  1,  3,  2 ]
#          └──────┘
#          sum = 3
#          length = 2
#          maxLen = 2


# STAGE 3: Expand → Add 5
#          L       R
#          |       |
#        [ 2,  1,  5,  1,  3,  2 ]
#          └──────────┘
#          sum = 8
#          length = 3
#          maxLen = 3


# STAGE 4: Expand → Add 1
#          L           R
#          |           |
#        [ 2,  1,  5,  1,  3,  2 ]
#          └──────────────┘
#          sum = 9  ❌ (9 > 8)

#          SHRINK → Remove nums[L] = 2

#              L       R
#              |       |
#        [ 2,  1,  5,  1,  3,  2 ]
#              └───────┘
#          sum = 7
#          length = 3
#          maxLen = 3


# STAGE 5: Expand → Add 3
#              L           R
#              |           |
#        [ 2,  1,  5,  1,  3,  2 ]
#              └──────────────┘
#          sum = 10 ❌ (10 > 8)

#          SHRINK → Remove nums[L] = 1

#                  L       R
#                  |       |
#        [ 2,  1,  5,  1,  3,  2 ]
#                  └───────┘
#          sum = 9 ❌

#          SHRINK → Remove nums[L] = 5

#                      L   R
#                      |   |
#        [ 2,  1,  5,  1,  3,  2 ]
#                      └───────┘
#          sum = 4
#          length = 2
#          maxLen = 3


# STAGE 6: Expand → Add 2

#                      L       R
#                      |       |
#        [ 2,  1,  5,  1,  3,  2 ]
#                      └──────────┘
#          sum = 6
#          length = 3
#          maxLen = 3

def longest_subarray_with_sum():
    nums = [2, 1, 5, 1, 3, 2]
    k = 8

    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(nums)):

        # Expand window
        current_sum += nums[right]

        # Shrink while invalid
        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        # Update maximum length
        max_len = max(max_len, right - left + 1)

    print(max_len)  # 3

# pattern2
nums = [2, 1, 5, 1, 3, 2]
k = 8
def longest_subarray_with_sum(nums, k):

    left = 0  # slow ptr
    right = 0 # fast ptr

    window_sum = 0
    max_len = 0

    while right < len(nums):

        # Expand window
        window_sum += nums[right]

        # Shrink if window sum exceeds k
        while window_sum > k:
            window_sum -= nums[left]
            left += 1

        # Update maximum length
        max_len = max(max_len, right - left + 1)

        # Move fast pointer
        right += 1

    return max_len

def count_num_subarray_product(nums, k):

    left = 0  # slow ptr
    right = 0 # fast ptr

    window_product = 1
    count = 0

    while right < len(nums):

        # Expand window
        window_product *= nums[right]

        # Shrink if product >= k
        while window_product >= k and left <= right:
            window_product //= nums[left]
            left += 1

        # Count valid subarrays ending at right
        count += right - left + 1

        # Move fast pointer
        right += 1

    return count









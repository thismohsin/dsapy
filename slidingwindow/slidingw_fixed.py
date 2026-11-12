# +----+--------------------------+------------------------------------------+
# | #  | Technique                | What we learned                          |
# +----+--------------------------+------------------------------------------+
# | 1  | Print every window       | Move pointers and print subsets          |
# | 2  | Running window sum       | Maintain sum without recalculating       |
# | 3  | Maximum window sum       | Find maximum sum of size K               |
# | 4  | Minimum window sum       | Find minimum sum of size K               |
# | 5  | Average of every window  | Sum divided by K                         |
# | 6  | Count even numbers       | Maintain conditional count               |
# | 7  | Frequency dictionary     | Track character frequencies              |
# | 8  | Maximum vowel count      | Maintain count of qualifying characters |
# | 9  | Find All Anagrams        | Compare frequency dictionaries          |
# +----+--------------------------+------------------------------------------+

# Index:       1       2       3
#              |-------|-------|
#                 1       2
#                 gaps
# right - left + 1 = gap+1


#idx movement + print subset
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# [2, 1, 5]
# [1, 5, 1]
# [5, 1, 3]
# [1, 3, 2]
def fixed_window(nums, k):

    left = 0
    right = k - 1

    while right < len(nums) - 1:

        # Expand window
        right += 1

        # Shrink if window size exceeds k
        if right - left + 1 > k:
            left += 1

        # Process valid window
        if right - left + 1 == k:
            print(nums[left:right + 1])

#fixed window + sum subset
#fixed window + sum subset + max
# nums = [2, 1, 5, 1, 3, 2]
# k = 3        sum
# [2, 1, 5]  → 8
# [1, 5, 1]  → 7
# [5, 1, 3]  → 9
# [1, 3, 2]  → 6
def running_window_sum(nums, k):

    window_sum = sum(nums[:k])

    left = 0
    right = k - 1

    print(window_sum)

    while right < len(nums) - 1:

        # Expand window
        right += 1
        window_sum += nums[right]

        # Shrink window
        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        # Process valid window
        if right - left + 1 == k:
            print(window_sum)


#fixed window + sum subset + max
# nums = [2, 1, 5, 1, 3, 2]
# k = 3        sum
# [2, 1, 5]  → 8
# [1, 5, 1]  → 7
# [5, 1, 3]  → 9
# [1, 3, 2]  → 6
#           max = 9
def max_sum_subarray(nums, k):

    window_sum = sum(nums[:k]) #k=3 then idx[0,1,2]
    max_sum = window_sum

    left = 0 #slow ptr
    right = k - 1 #k=3 then [(k-1) 2, 3 4 5 6 n-1]

    while right < len(nums) - 1: #fast ptr

        # Expand window
        right += 1
        window_sum += nums[right]

        # Shrink if window size exceeds k
        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        # Update maximum
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)

    return max_sum

#fixed window + sum subset + min
#fixed window + sum subset + max
# nums = [2, 1, 5, 1, 3, 2]
# k = 3        sum
# [2, 1, 5]  → 8
# [1, 5, 1]  → 7
# [5, 1, 3]  → 9
# [1, 3, 2]  → 6
#           min = 6
def min_sum_subarray(nums, k):

    window_sum = sum(nums[:k])
    min_sum = window_sum

    left = 0
    right = k - 1

    while right < len(nums) - 1:

        # Expand window
        right += 1
        window_sum += nums[right]

        # Shrink window
        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        # Update minimum
        if right - left + 1 == k:
            min_sum = min(min_sum, window_sum)

    return min_sum

#fixed window + avg(sum subset/k)
# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# [2.6666666666666665, 2.3333333333333335, 3.0, 2.0]
def average_subarray(nums, k):

    window_sum = sum(nums[:k])

    left = 0
    right = k - 1

    averages = []

    # Process initial window
    averages.append(window_sum / k)

    while right < len(nums) - 1:

        # Expand window
        right += 1
        window_sum += nums[right]

        # Shrink window
        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        # Calculate average
        if right - left + 1 == k:
            averages.append(window_sum / k)

    return averages

# Count even numbers in every window of size k.
# nums = [2, 1, 4, 3, 6, 5]
# k = 3
# [2, 1, 4]  → 2 even numbers
# [1, 4, 3]  → 1 even number
# [4, 3, 6]  → 2 even numbers
# [3, 6, 5]  → 1 even number
def count_even(nums, k):

    window_count = 0

    # Calculate initial window count
    for i in range(k):
        if nums[i] % 2 == 0:
            window_count += 1

    left = 0
    right = k - 1

    result = [window_count]

    while right < len(nums) - 1:

        # Expand window
        right += 1

        if nums[right] % 2 == 0:
            window_count += 1

        # Shrink window
        if right - left + 1 > k:

            if nums[left] % 2 == 0:
                window_count -= 1
                left += 1
            else:
                left += 1

        # Process valid window
        if right - left + 1 == k:
            result.append(window_count)

    return result

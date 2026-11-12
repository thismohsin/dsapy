# first
# Why currentPrefixSum-PreviousSum=K and not current+previous=k
# nums = [1, 2, 3]
# k = 3
# ---
# Array:
# Index       0    1    2
#            +----+----+----+
# Numbers    | 1  | 2  | 3  |
#            +----+----+----+
# Prefix sum:  1     3     6

#            REMOVE       KEEP
#            +----+      +----+----+
# Array      | 1  |      | 2  | 3  |
#            +----+      +----+----+
#               1          2    3

# ---
# Current prefix sum = 1 + 2 + 3 = 6
# Previous prefix sum = 1
# Remove the unwanted beginning:
#                  6
#               -  1
#               -----
#                  5

# Remaining subarray = [2, 3]


# #########
#        PREVIOUS ELEMENTS       DESIRED SUBARRAY
#        +----------------+      +----------------+
# Array  |  unwanted      |      |  wanted        |
#        +----------------+      +----------------+
#        <---------------------------------------->
#                   CURRENT PREFIX SUM

#        CURRENT PREFIX SUM
#        - PREVIOUS PREFIX SUM
#        -----------------------------------------
#                   SUBARRAY SUM
# #############

#### IMPORTANT
# # arr = [1, 2, 3]
#         [1 3 6]
#         {0,1,3,6]
# =3
# # k = 3
# # [3] and [1, 2] == size 2
# nums=       [1, 2, 3]
# currentsum= [1 3 6]
# pastsum=    [0 1 3]
# target=k=   3
# key= note we are doing range lookup currentsum vs pastsum substraction give result currentsum-pastsum=k
# from currentsum - target = lookup(pastsum)  i.e pastsum + target = currentsum
#         1-3 = -2
#         3-3 = 0
#         6-3 = 0
 

def subarraySumSet(nums, k):

    seen = {0}
    current_sum = 0
    count = 0

    for num in nums:

        current_sum += num
        needed = current_sum - k

        if needed in seen:
            count += 1

        seen.add(current_sum)

    return count


nums = [1, -1, 0]
k = 0

print(subarraySumSet(nums, k))


# # Idx              0 1 2
# # num              1 2 1
# # prefix           1 3 4  prefixsum/currentsum
# # target sum k     3 3 3  goal
# # need x to be k. -2 0 1 requiredsum   


# HANDLE MULTIPLE and DUPLICATE
#Technique: Remember previous sums and their frequencies
def subarraySum(nums, k):

    current_sum = 0
    count = 0

    seen = {0: 1}

    for i in range(len(nums)):

        # 1. Add current element
        current_sum = current_sum + nums[i]

        # 2. Calculate required previous prefix sum
        needed = current_sum - k

        # 3. Check if needed prefix sum exists
        if needed in seen:

            # 4. Add its frequency to count
            count = count + seen[needed]

        # 5. Store current prefix sum
        if current_sum in seen:

            # If already exists, increase frequency
            seen[current_sum] = seen[current_sum] + 1

        else:

            # If not present, insert with frequency 1
            seen[current_sum] = 1

    return count

## Sliding window does current_sum and remove object from tail
## doesnot work for -ive number well
## prefix sum uses current sum and maintain previous sum and does rangelookup difference to find count
def subarraySumSlidingWindow(nums, k):

    left = 0
    current_sum = 0
    count = 0

    for right in range(len(nums)):

        current_sum = current_sum + nums[right]

        while left <= right and current_sum > k:
            current_sum = current_sum - nums[left]
            left = left + 1

        if current_sum == k:
            count = count + 1

    return count



# Many range sum queries : Prefix Sum
# Count subarrays with sum K: Prefix Sum + Hash Map
# Subarray sum K with negative numbers: Prefix Sum + Hash Map
# Longest subarray with sum K:  Prefix Sum + Hash Map
# Find a subarray with sum K, positive numbers: Sliding Window
# Count subarrays with sum K, positive numbers: Sliding Window


# Find range using a Hash Map
# Instead of finding occurence count we will store index position
def findSubarray(nums, k):

    current_sum = 0
    seen = {0: -1}

    for i in range(len(nums)):

        current_sum = current_sum + nums[i]

        needed = current_sum - k

        if needed in seen:

            left = seen[needed] + 1 # indexing start at 0 so +1
            right = i # current position

            return (left, right)

        if current_sum not in seen:
            seen[current_sum] = i

    return None


nums = [1, 2, 3, 4]
k = 5

print(findSubarray(nums, k))


#sum(L,R)=prefix[R]−prefix[L−1] works without leading zero
#sum(L,R)=prefix[R+1]−prefix[L] works with leading zero
# -- formula R is first and L next ***  

# --- without leading zero
# arr =       [2, 4, 1, 5, 3]
#                 4+1+5=10
#              0  1. 2  3. 4
#                 L.    R

# prefix =    [2, 6, 7, 12, 15]
# Idx:         0  1  2  3   4

# -- we are taking indices of num and value of prefix ***   
# sum(1,3) =  prefix[R*]-prefix[L-1*]
#             prefix[3]-prefix[1-1=0]
#             12 - 2 = 10


# --- with leading zero
# arr =       [2, 4, 1, 5, 3]
#                 4+1+5=10
#              0  1. 2  3. 4
#                 L.    R

# prefix =    [0  2, 6, 7, 12, 15]
# Idx:         0  1  2  3   4

# -- we are taking indices of num and value of prefix ***  
# sum(1,3) =  prefix[R+1*]-prefix[L*]
#             prefix[3+1=4]-prefix[1]
#             12 - 2 = 10

# Example
# arr =       [2, 4, 1, 5, 3]
#                 L     R        sum=10
# prefix = [0, 2, 6, 7, 12, 15]
#             0. 1  2. 3. 4.   5
# sum(L,R)=prefix[R+1]+prefix[L]
# sum(1,3)=prefix[3+1]+prefix[1]
#         = 12 - 2
#         = 10

def range_sum(arr, L, R):
    total = 0

    for i in range(L, R + 1):
        total += arr[i]

    return total


# ------
# Problem 5: Find Pivot Index (LeetCode 724)
# Sum of elements to the left = Sum of elements to the right.
# nums = [1, 7, 3, 6, 5, 6]
          0. 1. 2  3  4. 5
# TOTAL SUM = LEFT SUM + PIVOT + RIGHT SUM
# RIGHT SUM = TOTAL SUM - LEFT SUM - PIVOT
# LEFT SUM = TOTAL SUM - PIVOT - RIGHT SUM
# At index 0, the left sum is 0 because nothing exists to its left.
# At index 5, the right sum is 0 because nothing exists to its right.
# Why do we update left_sum after checking the current index instead of before checking it?
# before adding that value is pivot which we substract not add, look formula


# while scanning u get leftsum 
# u also know totalsum
#next element is pivot
    #          TOTAL SUM
    #              |
    #    ---------------------
    #    |         |         |
    # LEFT SUM   PIVOT   RIGHT SUM
    #    |         |
    #    ---------------------
    #              |
    #    RIGHT = TOTAL - LEFT - PIVOT
    #              |
    #    LEFT == RIGHT ?
    #        /       \
    #      YES        NO
    #       |          |
    #    RETURN      CONTINUE



def pivotIndex(nums: List[int]) -> int:

    total_sum = sum(nums) # total sum for array
    left_sum = 0
    # total sum
    # scan leftsum
    # pivot is next element to eval
    # rightsum =  total_sum - pivot - leftsum
    # *before adding number to leftsum it is pivot first
    for i in range(len(nums)):

        # we need any number added to left_sum is pivot first
        right_sum = total_sum - left_sum - nums[i]

        if left_sum == right_sum:
            return i

        left_sum += nums[i] # keep adding to sum

    return -1

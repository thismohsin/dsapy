# subarray = nums[left:right + 1]
# distinct_count = len(set(subarray))

# nums = [1, 1, 2]
# for left in range(len(nums)):
#     for right in range(left, len(nums)):
#         subarray = nums[left:right + 1]
#         print(subarray)


# Index:  0   1   2
# Value:  1   1   2
# left = 0
# +-------+-------+----------------+
# | Right  | indic | Subarray       |
# +-------+-------+----------------+
# |   0   |   0   | [1]            |
# |   1   |  0 1  | [1, 1]         |
# |   2   | 0 1 2 | [1, 1, 2]      |
# +-------+-------+----------------+
# left = 1
# +-------+-------+----------------+
# | Left  | Right | Subarray       |
# +-------+-------+----------------+
# |   1   |   1   | [1]            |
# |   2   |  1 2  | [1, 2]         |
# +-------+-------+----------------+
# left =2
# +-------+-------+----------------+
# | Left  | Right | Subarray       |
# +-------+-------+----------------+
# |   2   |   2   | [2]            |
# +-------+-------+----------------+

# Index:  0   1   2   3
# Nums:   1   2   1   2
#         L           R

# Index:  0   1   2   3
# Nums:   1   2   1   2
#         L           R

# count += 3 - 0 + 1
# count += 4

# [1, 2, 1, 2]
#     [2, 1, 2]
#         [1, 2]
#            [2] 
# total 4, look at formula


####
# Subarrays with K Different Integers

# nums = [1, 2, 1, 2, 3]
# k = 2
# o/p 7

# [1, 2]
# [1, 2, 1]
# [1, 2, 1, 2]
# [2, 1]
# [2, 1, 2]
# [1, 2]
# [2, 3]


# ###
# nums = [1, 2, 3]
# length 1 = [1], [2], [3]
# length 2 = [1, 2], [2, 3]
# length 3 = [1, 2, 3]

# condition1 is contiguous thereby first element is smaller then second
# condition2 2 unique element not 1 or 3
# we pick length 2 it has 2 contiguous set of type 2 element

# nums = [1, 1, 2]

# [1]
# [1, 1]
# [1, 1, 2] -- YES
# [1]
# [1, 2] -- YES
# [2]
# ===========


### Mono deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
o/p=[3, 3, 5, 5, 6, 7]

[1, 3, -1]  → max = 3
[3, -1, -3] → max = 3
[-1, -3, 5] → max = 5
[-3, 5, 3]  → max = 5
[5, 3, 6]   → max = 6
[3, 6, 7]   → max = 7


# DEQUE
# Think of it as a list where you can efficiently add or remove elements from both the beginning and the end
# from collections import deque
# nums = deque([10, 20, 30])
# nums.append(40) :       10 20 30 40
# nums.appendleft(5):   5 10 20 30 40
# nums.pop() and popleft()


# WHY DEQUE in SLIDING WINDOW

# 1, 3, -1
# maximum = 3
# do we need 1? No 3 is Max
# KEEP DEQUE in DECREASING ORDER KEEP SMALL ELEMENT AT BACK
# Front → 3 → -1 → Rear. : front is MAX

# in sequential flow
# keep max at FRONT
# if new element is smaller then Deque Front 
#     then put them in REAR 
# else (greater then front element)
#     then empty deque AND put max element at front.

# why are we removing  1 3 -1 (we kno 3 is max and we dont care about min then max/current element)

# 

# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k=3

# 1. we compare incoming element with front of deque to decide current element is greater or smaller.
# 2. if incoming element smaller then we append new element in REAR
# 3. if incoming element is greater then we empty deque from REAR and add new incoming element as FRONT (only 1 element in deque)

# first 1 add to deque
# FRONT : 1 :REAR
# next 3  bigger then FRONT 1 so empty deque from rear and put 3
# FRONT : 1 :REAR
# next -1 smaller then FRONT 1 then put it at back rear
# FRONT : 1 -1 :REAR
# next -3 smaller then FRONT 1 then put it at back rear
# FRONT : 1 -1 -3:REAR
# next 5  bigger then FRONT 1 so empty deque from rear and put 5
# FRONT : 5 :REAR
# next 3 smaller then FRONT 5 then put it at back rear
# FRONT : 5 3 :REAR
# next 6 greater then FRONT 5 then empty deque from rear and put 6
# FRONT : 6 :REAR
# next 7 greater then FRONT 6 then empty deque from rear and put 7
# FRONT : 7 :REAR
# RESULT 7

# Index:    0   1   2   3   4   5   6   7
#           ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
# Value:    1   3  -1  -3   5   3   6   7

# nums[0] = 1
# nums[1] = 3
# nums[2] = -1


################################
# Permutation in String — Sliding Window (LeetCode 567)
# Intuition: We need to determine whether s2 contains a substring that has exactly the same character frequencies as s1.
# A permutation means same characters, same counts, different order allowed.

# s1 = "ab"
# s2 = "eidbaooo"

#          e i d b a o o o
#              └─ b a ─┘

#              "ba" = permutation of "ab"

# Output: True

# s1 = "ab"

# need   = {a:1, b:1}
# window = {e:1, i:1}

#         [ e i ] d b a o o o
#               ↓
#         Remove e, add d

#         e [ i d ] b a o o o
#               ↓
#         Remove i, add b

#         e i [ d b ] a o o o
#               ↓
#         Remove d, add a

#         e i d [ b a ] o o o

# need   = {a:1, b:1}
# window = {b:1, a:1}

#         MATCH → True


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:k])

        if window == need:
            return True

        for right in range(k, len(s2)):
            # Add incoming character
            window[s2[right]] += 1

            # Remove outgoing character
            left = right - k
            window[s2[left]] -= 1

            # Remove zero-frequency keys
            if window[s2[left]] == 0:
                del window[s2[left]]

            # Evaluate
            if window == need:
                return True

        return False



# Same question different pattern
#instead of == counter we use == array using ord*

# ord('a')  # 97
# ord('b')  # 98
# ord('c')  # 99
# ord('d')  # 100

# ord('a') - ord('a')
# = 97 - 97
# = 0

# ASCII 128
# 65–90 Capital Alphabet
# 97–122 Lower Alphabet

# Character    ASCII    Minus 97    Array index

#     a          97       97-97          0
#     b          98       98-97          1
#     c          99       99-97          2
#     d         100      100-97          3
#     e         101      101-97          4
#     ...        ...        ...          ...
#     z         122      122-97         25


# freq = [0] * 26

# ARRAY POSITION (INDEX)

# Index:    0   1   2   3   4   5   ... 25
# Letter:   a   b   c   d   e   f   ... z
# Value:    0   0   0   0   0   0   ... 0

# index of b = ord('b') - ord('a')
#       = 98 - 97
#       = 1

# Index:    0   1   2   3   4
# Letter:   a   b   c   d   e
# Value:    0   1   0   0   0
#               ↑
#           We counted b

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # Create frequency arrays (26 letters)
        need = [0] * 26 ### with input create need:array instance
        window = [0] * 26 ### with incoming and outgoing element set and reset array index
        ### at end of each iteration compare need with window

# need:
# Index:  0  1  2  3  4  5  6  7  8  9 ... 25
# Letter: a  b  c  d  e  f  g  h  i  j ... z 
# Value:  1  1  0  0  0  0  0  0  0  0 ... 0
        # Count characters in s1
        for c in s1:
            index = ord(c) - ord('a')
            need[index] += 1

        k = len(s1)

        # Sliding window over s2
        for right in range(len(s2)):

            # Add incoming character
            index = ord(s2[right]) - ord('a')
            window[index] += 1

            # Remove outgoing character
            if right >= k:
                index = ord(s2[right - k]) - ord('a')
                window[index] -= 1

            # Compare frequencies
            if window == need:
                return True

        return False
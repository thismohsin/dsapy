
# LC 1004 — Max Consecutive Ones III
# Problem: Given a binary array nums and an integer k, you can flip at most k zeros to ones. Find the maximum number of consecutive ones.
# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2
# Goal: Find the longest window containing at most 2 zeros.
# No -- [1, 1, 1, 0, 0] - length 5
# Yes --[0, 0, 1, 1, 1, 1] - length 6
# Flip two zeros:
# [1, 1, 1, 1, 1, 1]
# Length = 6

def longest_ones_withreplacementof_k_zero(nums, k):

    left = 0  # slow ptr
    right = 0 # fast ptr

    zero_count = 0
    max_len = 0

    while right < len(nums):

        # Expand window
        if nums[right] == 0:
            zero_count += 1

        # Shrink if zeros exceed k
        while zero_count > k:

            if nums[left] == 0:
                zero_count -= 1

            left += 1

        # Update maximum length
        max_len = max(max_len, right - left + 1)

        # Move fast pointer
        right += 1

    return max_len


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

print(longest_ones_withreplacementof_k_zero(nums, k))  # 6



#  LC 3 — Longest Substring Without Repeating Characters
# s = "abcabcbb"
# a b c
# a = 1 b = 1 c = 1
# Length = 3
# abc = 3
#  bca = 3
#   cab  = 3
#     abc = 3
#      nomorecombination

# max = 3
# for understanding we will collect all combination of value too


# All valid windows:
# ['a', 'ab', 'abc', 'bca', 'cab', 'abc', 'cb', 'b']

# Maximum length: 3

# Longest windows:
# ['abc', 'bca', 'cab', 'abc']

# Final Answer: 3
def longest_substring_without_repeat_char(s):

    left = 0                  # Slow pointer
    right = 0                 # Fast pointer

    char_freq = {}            # Track character frequencies

    max_len = 0               # Previous maximum length
    all_valid = []            # Store all valid windows
    longest_windows = []      # Store longest windows

    while right < len(s):

        # STEP 1: Fast pointer picks a new character
        fast_char = s[right]

        # STEP 2: Add fast character to the window
        char_freq[fast_char] = char_freq.get(fast_char, 0) + 1

        # STEP 3: Shrink if duplicate exists
        while char_freq[fast_char] > 1:

            # Identify character leaving the window
            slow_char = s[left]

            # Remove its frequency
            char_freq[slow_char] -= 1

            # Delete if frequency becomes zero
            if char_freq[slow_char] == 0:
                del char_freq[slow_char]

            # Move slow pointer
            left += 1

        # STEP 4: Current window is valid
        window = s[left:right + 1]

        # STEP 5: Collect all valid windows
        all_valid.append(window)

        # STEP 6: Update maximum length
        # we could do something max_len = max(max_len, right - left + 1)
        # but to reset longestwindow we did traditional if
        if right - left + 1 > max_len:
            max_len = right - left + 1
            longest_windows = [] # clean up old gather data if new length known

        # STEP 7: Collect windows matching maximum length
        if right - left + 1 == max_len:
            longest_windows.append(window) ## add/append new data of maxlen 

        # STEP 8: Move fast pointer
        right += 1

    print("All valid windows:", all_valid)
    print("Maximum length:", max_len)
    print("Longest windows:", longest_windows)

    return max_len


# Input
s = "abcabcbb"

# Execute
result = longest_substring_without_repeat_char(s)

print("Final Answer:", result)

## PATTERN 2 for above question
def longest_substring_without_repeat_chars(s):

    left = 0
    seen = set()
    max_len = 0

    for right in range(len(s)):
        fast_char = s[right]
        #because we found duplicate ABB or ABA 
        #we remove all element until no duplicate of fast_char
        #ABB > B
        #ABA > BA
        while fast_char in seen:
            slow_char =s[left]
            seen.remove(slow_char)
            left += 1

        seen.add(fast_char)

        max_len = max(max_len, right - left + 1)

    return max_len

#######

# LC 424 — Longest Repeating Character Replacement
# Problem: Given a string s and an integer k, you can replace at most k characters to make all characters in a substring the same. Find the length of the longest such substring.
# s = "AABABBA"
# k = 1
# "AABA" : Replace B with A:
# "AAAA" Length = 4
# "BABB": Replace A with B:
# "BBBB" Length = 4  is also right

# so if we want any string with len > 2 that need 1 replacement to become same
# ['AAB', 'AABA', 'ABA', 'ABB', 'BAB', 'BABB', 'BBA']
# thereafter we find max from it
# ----------
### INTUITION
# A A B A B

# A A A A A
#     ↑   ↑
#   Replace 2 characters

# Total window length = 5
# Most frequent character = 3
# Replacements required = 5 - 3 = 2

# Replacements=Window Length−Max Frequency
# Window Length−Max Frequency <=k

# A A A B A A C
# A = 5
# B = 1
# C = 1

# window_length = 7 max_freq = 5
# replacements = 7 - 5
#              = 2
# 2 <= k  # VALID

def longest_character_replacement(s, k):

    left = 0
    right = 0

    char_freq = {}
    max_freq = 0
    max_len = 0

    while right < len(s):

        fast_char = s[right]
        # Expand window
        char_freq[fast_char] = char_freq.get(fast_char, 0) + 1

        #we need this MaxFrequencyRepeatingChar as we move forward
        max_freq = max(max_freq, char_freq[fast_char])

        # Shrink if replacements exceed k
        # ReplacementChar = Window Length − MaxFrequencyRepeatingChar
        while (right - left + 1) - max_freq > k:
            slow_char = s[left]
            char_freq[slow_char] -= 1 
            #it is ok not to remove B  'A': 2,'B': 0,'C': 1
            # we done use len(char_freq) to determine condition
            # previous question was on char_freq not this one
            # if char_freq[s[left]] == 0:
            #     del char_freq[s[left]]
            left += 1

        # Update maximum
        max_len = max(max_len, right - left + 1)

        right += 1

    return max_len
s = "AAABAAC"
k = 2

print(longest_character_replacement(s, k))  # 7

####
# You are given an array where each number represents a type of fruit.
# You have two baskets:
# Each basket can hold only one type of fruit.
# You can collect unlimited fruits of that type.
# Find the maximum number of consecutive fruits you can collect.

# fruits = [1, 2, 1, 2, 3]
# collect 1 2 1 2 == 2 type and length of 4 - yes
# 1 2 3 - not allowed
# 2 3 - small count 

# *** distinct <= 2 ***
# freq = {1: 2, 2: 2}
# freq_count = distinct = 2 and 2+2=4 = max 
# freq = {1: 2, 2: 2, 3: 1}
# freq_count = distinct = 3 not acceptable

def fruit_type_count(fruits):

    left = 0
    right = 0

    fruit_type = 2
    max_count_fruits = 0

    freq = {}

    while right < len(fruits):

        # STEP 1: Expand window
        fast_char = fruits[right]

        # STEP 2: Add incoming fruit
        freq[fast_char] = freq.get(fast_char, 0) + 1

        # STEP 3: Shrink if distinct fruit types > 2
        while len(freq) > fruit_type:

            slow_char = fruits[left]

            freq[slow_char] -= 1

            if freq[slow_char] == 0:
                del freq[slow_char]

            left += 1

        # STEP 4: Update maximum window length
        max_count_fruits = max(
            max_count_fruits,
            right - left + 1
        )

        # STEP 5: Move right
        right += 1

    return max_count_fruits


fruits = [1, 2, 1, 2, 3]

print(fruit_type_count(fruits))  # 4
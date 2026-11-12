
# s = "abacaba"
# k = 3
# "aba" → {'a': 2, 'b': 1}
# "bac" → {'b': 1, 'a': 1, 'c': 1}
# "aca" → {'a': 2, 'c': 1}
# "cab" → {'c': 1, 'a': 1, 'b': 1}
# "aba" → {'a': 2, 'b': 1} 
# we freq map and clone it in [] and keep appending as we find
def fixed_window_frequency(s, k):

    freq = {}

    # Build initial window
    for i in range(k):
        char = s[i]
        freq[char] = freq.get(char, 0) + 1 

    left = 0
    right = k - 1

    result = [freq.copy()] #{'a': 2, 'b': 1}

 #abac
    while right < len(s) - 1:

        # Expand window
        right += 1 #c

        incoming = s[right]
        freq[incoming] = freq.get(incoming, 0) + 1 #{'a': 2, 'b': 1, 'c': 1}

        # Shrink window
        if right - left + 1 > k: # abac therefore yes 3-0+1=4>3

            outgoing = s[left] # take outgoing element
            freq[outgoing] -= 1 # reduce frequency of outgoing element

            if freq[outgoing] == 0: # if outgoing element frequency is 0 remove element
                del freq[outgoing]

            left += 1 # move left fwd

        # Process valid window
        if right - left + 1 == k: # bac therefore yes 3-1+1=3
            result.append(freq.copy()) ##{'a': 1, 'b': 1, 'c': 1}

    return result

# s = "abciiidef"
# k = 3

# INDEX:       0 1 2 3 4 5 6 7 8
# STRING:      a b c i i i d e f
#              L   R

# INITIAL WINDOW
# ┌───────────────────────────┐
# │ Window: "abc"             │
# │                           │
# │ a = vowel     → +1        │
# │ b = consonant → +0        │
# │ c = consonant → +0        │
# │                           │
# │ window_count = 1          │
# │ max_count    = 1          │
# └───────────────────────────┘
# =================================================

# WINDOW 1: EXPAND RIGHT → 3

# a b c i i i d e f
# L     R
#       ↑
#    Incoming i

# i = vowel → window_count + 1
#            1 + 1 = 2

# WINDOW TOO LARGE: 4 > 3

# REMOVE LEFT ELEMENT: a

# a = vowel → window_count - 1
#            2 - 1 = 1

# Move LEFT: 0 → 1

#   a [b c i] i i d e f
#       L   R

# Current window = "bci"
# ========
# Index:          0   1   2   3   4   5   6   7   8
# String:         a   b   c   i   i   i   d   e   f

# Initial:        [a   b   c]  i   i   i   d   e   f
#                  L       R
#                 count = 1
#                 max   = 1

# Transition 1:    a  [b   c   i]  i   i   d   e   f
#                     L       R
#                 Incoming i: +1
#                 Outgoing a: -1
#                 count = 1
#                 max   = 1

# Transition 2:    a   b  [c   i   i]  i   d   e   f
#                        L       R
#                 Incoming i: +1
#                 Outgoing b:  0
#                 count = 2
#                 max   = 2

# Transition 3:    a   b   c  [i   i   i]  d   e   f
#                            L       R
#                 Incoming i: +1
#                 Outgoing c:  0
#                 count = 3
#                 max   = 3

# Transition 4:    a   b   c   i  [i   i   d]  e   f
#                                L       R
#                 Incoming d:  0
#                 Outgoing i: -1
#                 count = 2
#                 max   = 3

# Transition 5:    a   b   c   i   i  [i   d   e]  f
#                                    L       R
#                 Incoming e: +1
#                 Outgoing i: -1
#                 count = 2
#                 max   = 3

# Transition 6:    a   b   c   i   i   i  [d   e   f]
#                                        L       R
#                 Incoming f:  0
#                 Outgoing i: -1
#                 count = 1
#                 max   = 3


def max_vowels(s, k):

    vowels = "aeiou"

    window_count = 0

    # Calculate initial window
    for i in range(k):
        if s[i] in vowels:
            window_count += 1

    max_count = window_count

    left = 0
    right = k - 1

    while right < len(s) - 1:

        # Expand window
        right += 1

        if s[right] in vowels:
            window_count += 1

        # Shrink window
        if right - left + 1 > k:

            if s[left] in vowels:
                window_count -= 1

            left += 1

        # Update maximum
        if right - left + 1 == k:
            max_count = max(max_count, window_count)

    return max_count

# s = "cbaebabacd"
#      0     6
# p = "abc"
# [0, 6]
# from collections import Counter
# p = "abc"
# pattern_count = Counter(p)
# print(pattern_count)
# Counter({'a': 1, 'b': 1, 'c': 1})
# INITIALIZE
#     ↓
# EXPAND RIGHT
#     ↓
# ADD INCOMING CHARACTER
#     ↓
# SHRINK LEFT
#     ↓
# REMOVE OUTGOING CHARACTER
#     ↓
# COMPARE COUNTERS
#     ↓
# STORE LEFT INDEX IF EQUAL


from collections import Counter

def find_anagrams(s, p):

    # STEP 1: Initialize pattern frequency
    k = len(p)
    pattern_count = Counter(p)

    # STEP 2: Build initial window frequency
    freq = Counter(s[:k])

    left = 0
    right = k - 1

    result = []

    # STEP 3: Check initial window
    if freq == pattern_count:
        result.append(left)

    while right < len(s) - 1:

        # STEP 4: Expand window
        right += 1

        incoming = s[right]
        freq[incoming] += 1

        # STEP 5: Shrink window
        if right - left + 1 > k:

            outgoing = s[left]
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            left += 1

        # STEP 6: Check anagram
        if right - left + 1 == k:
            if freq == pattern_count:
                result.append(left)

    return result


s = "cbaebabacd"
p = "abc"

print(find_anagrams(s, p))
# Answer:     1   2   3   4   5   6   7   8   9
# Feasible:   Y   Y   Y   Y   Y   N   N   N   N
#                         ^
#                   Maximum feasible answer


# while left <= right:

#     mid = (left + right) // 2

#     if is_feasible(mid):

#         left = mid + 1

#     else:

#         right = mid - 1

# return right

# stalls = [1, 2, 4, 8, 9]
# cows = 3
# we want to maximize the minimum distance between cows.



position = [1, 2, 3, 4, 7]
m = 3
min_distance = 3
def is_feasible(min_distance):

    balls_placed = 1
    last_position = position[0]

    for current_position in position[1:]:

        distance = current_position - last_position

        if distance >= min_distance:

            # Place a ball here
            balls_placed += 1

            # Remember where we placed it
            last_position = current_position

        if balls_placed == m:
            return True

    return False


###
# candies = [5, 8]
# k = 3
# Box 1 contains 5 candies.
# Box 2 contains 8 candies.
# You have 3 children.
# Every child must receive the same number of candies, and candies must come from only one box per child.

# 4 from box1 goes to kid1 with leftover 1
# 4 from box2 goes to kid2
# 4 from box2 goes to kid3
# here we maximize distribution
# equal distribution -- no split across boxes - valid leftover - allocation came from same box

# 5 from box1 goes to kid1
# 5 from box2 goes to kid2
# nothing for kid3? FAILED equal split

# totol 13 candies

# Candies = [5, 8]
# k = 3

# RULES:
# - Every child receives exactly the same number of candies (MID).
# - A child cannot combine candies from different boxes.
# - One box can be split among multiple children.
# - Leftover candies are discarded.

# +-------+---------+---------+----------------+----------------+------------------+
# | Share | Box 1   | Box 2   | Complete       | Children       | children >= 3    |
# |       | (5)     | (8)     | groups         | served         |                  |
# +-------+---------+---------+----------------+----------------+------------------+
# |   1   |    5    |    8    |       13       |       13       | TRUE             |
# |   2   |    2    |    4    |        6       |        6       | TRUE             |
# |   3   |    1    |    2    |        3       |        3       | TRUE             |
# |   4   |    1    |    2    |        3       |        3       | TRUE=3 <--ANSWER |
# |   5   |    1    |    1    |        2       |        2       | FALSE            |
# |   6   |    0    |    1    |        1       |        1       | FALSE             |
# |   7   |.   0.   |.   1.   |.       1.      |        1       | FALSE             |
# |   8   |.   0.   |.   1.   |.       1.      |        1       | FALSE             |
# |   9   |.   0.   |.   0.   |.       0.      |        0       | FALSE GOT WHYMAX AND NOT SUM
# +-------+---------+---------+----------------+----------------+------------------+

# COMPLETE GROUPS = Box 1 groups + Box 2 groups

# CHILDREN SERVED = COMPLETE GROUPS

# FEASIBILITY CONDITION:
# children >= k
# children >= 3

# TRUE  --> Feasible --> Search RIGHT (larger share)
# FALSE --> Infeasible --> Search LEFT (smaller share)

# PATTERN:
#          T     T     T     T     F     F
#                            ^
#                     MAXIMUM FEASIBLE
#                          ANSWER = 4


def can_distribute(candies, try_with_candies, min_children):

    total_groups = 0

    for box in candies:
        groups = box // try_with_candies
        total_groups += groups

    return total_groups >= min_children


def maximumCandies(candies, k):

    left = 1
    #A child cannot combine candies from different boxes.
    # with 8 candies of equal distribution only 1 kid will get 
    # with 9 candies of equal distribution only 0 kid will get
    right = max(candies) # eventually we have distribute candy and max 8

    answer = 0

    while left <= right:

        mid = left + (right - left) // 2

        if can_distribute(candies, mid, k):

            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    return answer
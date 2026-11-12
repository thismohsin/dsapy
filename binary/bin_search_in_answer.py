# -- Milestone 0
# Imagine you have 10 workers who need to complete 100 tasks.

# You want to find the minimum number of days required if every worker can complete a certain number of tasks per day.

# monotonic
# Days:       1   2   3   4   5   6   7   8
# Possible:   N   N   N   Y   Y   Y   Y   Y
#                          ^
#                     First YES
                    
# Every worker does 4 task per day
# we have 10 worker an 4 task per day = 40task per day
# 40task/day * xDays = 100 task = 3+days

# ############
# -- Milestone 1
# piles = [3, 6, 7, 11]
# We need to find the minimum eating speed k such that all bananas can be eaten within 8 hours.
# number of bananas [1...11] u can use binary search and find out what value meets our requirement speed

# assuming we have to eat at speed 3 bananas per hour
# total banana = 3+6+7+11 = 27
# 3banana/hour * total 8hour = 24 banana -- we want to finish 27 banana not meeting requirement NO
# 4banan/hour * total 8hour = 32 banana -- we finish 27 and have capacity -- meet requirement YES
# 5banan/hour * total 8hour = 40 banana -- we finish 27 and have capacity -- meet requirement YES

# Answer is 4 because it is minimum banana/day

# max_hour_finish_banana = 8 #constraint hour finish eating banana
# total_bananas=27 # sum of all bananas in piles
# for (banana_per_hour = 1 to piles[len(piles)-1])
# 		banana_per_hour * 8 > total_bananas
# 		return banan_per_hour #decimal, split in piles - not answer


# -- Milestone 2
# why this is NOT right answer
# Constraint -- Each hour, we can eat from only one pile. and pile may or may not have exact 4
# then your assumption avg wont work because now u expecting to eat from other pile which fails constraint

# Example 3bph or 3b/h

# Piles = [3, 6, 7, 11]

# Pile 3  → 1 hour 3b/(3bph)=0R 0 remainder accpetable
# Pile 6  → 2 hours 6b/3bph=0R  0 remiander acceptable
# Pile 7  → 3 hours 7b/3bph=1R  +ive Remainder need 1 more
# Pile 11 → 4 hours 11b/3bph=2R +ive remainder need 1 more
#          ---------
# Total   → 10 hours -- No 

# Example 4b/h


# Piles = [3, 6, 7, 11]

# Pile 3  → 1 hour 3b/4bph= -1R negative remainder acceptable 
# Pile 6  → 2 hours 6b/4bph= 1R positive remaiinder need 1 more
# Pile 7  → 2 hours 7b/4bph= 3R positive remaiinder need 1 more
# Pile 11 → 3 hours 11/4bph= 3R positive remaiinder need 1 more
#          ---------
# Total   → 8 hours = YES

# ####
# max_hour_finish_banana = 8 #constraint hour finish eating banana
# total_bananas=27 # sum of all bananas in piles

# eat_speed = 0
# for (bananas_in_pile_per_hour = 1 to piles[len(piles)-1])
# 		for(pile:piles)
# 			remainder_banana = pile/bananas_in_pile_per_hour
# 			remainder_banana > 0
# 			  remainder_banana + 1
# 			eat_speed = eat_banana + remainder_banana
# 			if eat_speed >= max_hour_finish_banana
# 				return eat_speed
			
###
# -- Milestone 3
# There are two issues:
    # You're using division instead of calculating the integer quotient and remainder.
    # You're adding 1 to the remainder instead of calculating the number of hours.
# speed = dist/time
# bananas_in_pile[3 6 7 11]
# bananas_in_pile_per_hour [1..11]
# time = dist/speed
# banana_eat_speed_hour (?) = bananas_in_pile / bananas_in_pile_per_hour
# Pile = 11 bananas
# Speed = 4 bananas/hour
# Time = 11 / 4 = 2.75 hours # Still remainder > 0 then + 1
# you can avoid remainder logic 
# by 
# banana_eat_speed_hour = bananas_in_pile + bananas_in_pile_per_hour - 1 / bananas_in_pile_per_hour

####
# -- Milestone 4
#Brute

## REMIANDER LOGIC ***
#piles = [3, 6, 7, 11]
# max_hours = 8

# for speed in range(1, max(piles) + 1):

#     total_hours = 0

#     for pile in piles:

#         hours = pile // speed
#         remainder = pile % speed

#         if remainder > 0:
#             hours += 1

#         total_hours += hours

#     if total_hours <= max_hours:
#         print("Minimum speed:", speed)
#         break


## TRICK LOGIC
#piles = [3, 6, 7, 11]
# max_hours = 8

# for speed in range(1, max(piles) + 1):

#     total_hours = 0

#     for pile in piles:
#         hours = (pile + speed - 1) // speed (trick of speed - 1 in Nr)
#         total_hours += hours

#     if total_hours <= max_hours:
#         print("Minimum speed:", speed)
#         break

# -- Milestone 5
#-- Bin Search

# Speed:       1  2  3  4  5  6  7  8  9 10 11
# Possible:    N  N  N  Y  Y  Y  Y  Y  Y  Y  Y
#                      ^
#                  First YES
def banana_eat_speed_per_hour():
    piles = [3, 6, 7, 11]
    max_hours = 8 # kis pile mein max banana
    left = 1
    right = max(piles) # intuition max pile will ensure all banana is eaten from all piles

    if max_hours < len(piles):
            return -1 # min 1h per pile and 4 piles then we need 4h and if max_hour is 3 then incorrect ask 

    if max_hours == len(piles):
         return right # min 1h per pile and 4 piles then we need 4h and if max_hour is 4 then return maxPile right
    
    while left <= right:

        speed = (left + right) // 2

        total_hours = 0

        for pile in piles:

            hours = pile // speed
            remainder = pile % speed

            if remainder > 0:
                hours += 1

            total_hours += hours

        if total_hours <= max_hours:
            right = speed - 1    # YES → search LEFT

        else:
            left = speed + 1     # NO → search RIGHT

    return left

#Piles = [3, 6, 7, 11]
# Maximum allowed time = 8 hours

#        SEARCH FOR SPEED
#        [1 ........... 11]
#                 |
#                 v
#        Candidate speed = K
#                 |
#                 v
#        Calculate time per pile
#                 |
#        +--------+--------+
#        |        |        |
#       3/K      6/K      7/K ... 11/K
#        |        |        |
#        v        v        v
#       ceil     ceil     ceil
#        |        |        |
#        +--------+--------+
#                 |
#                 v
#         Add all required hours
#                 |
#                 v
#          total_hours <= 8?
#              /       \
#            YES        NO
#             |          |
#          Try lower   Try higher
#            speed       speed

# https://www.youtube.com/watch?v=LzZFUTWE55c
import math
def banana_eat_speed_per_hour():
    piles = [3, 6, 7, 11]
    max_hours = 8
    low = 1
    high = max(piles) # intuition max pile value, ensures all banana is eaten from all piles
    best_speed = float("inf") # max integer but start with float and division later convert this val to int or use max pile at init
    
    if max_hours < len(piles):
            return -1 # min 1h per pile and 4 piles then we need 4h and if max_hour is 3 then incorrect ask 

    if max_hours == len(piles):
         return high # min 1h per pile and 4 piles then we need 4h and if max_hour is 4 then return maxPile right

    # pile[defined array with value]
    # speed[1 2 3 4 ... 11] .. we change speed
    while low <= high:
        speed = low + (high-low)//2 #avoid overflow

        if is_possible_to_eat_at_this_speed(piles, speed, max_hours) == True:
          best_speed = speed    #store speed
          high = speed - 1      #reduce speed by going to left side
        else:
          low = speed + 1

    return best_speed

def is_possible_to_eat_at_this_speed(piles, speed, max_hours):
     time = 0
     for pile in piles:
          time = time + math.ceil(piles/speed) # 7pile/3speed=got 2 expected 3 therefore use ciel

     return time <= max_hours
         
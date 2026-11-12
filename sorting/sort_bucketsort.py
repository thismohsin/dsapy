# arr = [29, 11, 35, 14, 42, 18, 31, 12]
# Bucket 0:  [10, 19]
# Bucket 1:  [20, 29]
# Bucket 2:  [30, 39]
# Bucket 3:  [40, 49]

# INPUT:
# [29, 11, 35, 14, 42, 18, 31, 12]

# DISTRIBUTION:

# B0 = [11, 14, 18, 12]
# B1 = [29]
# B2 = [35, 31]
# B3 = [42]

# SORT EACH BUCKET:

# B0 = [11, 12, 14, 18]
# B1 = [29]
# B2 = [31, 35]
# B3 = [42]

# CONCATENATE:

# [11, 12, 14, 18, 29, 31, 35, 42]

# ##########################
# Index:    0    1    2    3    4    5    6    7
# Array:   [29] [11] [35] [14] [42] [18] [31] [12]

# Bucket 0: 10–19
# Bucket 1: 20–29
# Bucket 2: 30–39
# Bucket 3: 40–49
# width of bucket is 10 and 4 bucket
# 10          20          30          40          50
# |-----------|-----------|-----------|-----------|
#  Bucket 0    Bucket 1    Bucket 2    Bucket 3


# buckets = [[], [], [], []] ie., [[B0], [B1], [B2] [B3]]

# distribute = current-number - starting_range / width of bucket
# for 29 =>   29-10/10 = floor(1.9) = bucket 1 
# for 19 =>   19-10/10 = floor(0.9) = bucket 0

# B0 = [11, 14, 18, 12]
# B1 = [29]
# B2 = [35, 31]
# B3 = [42]

# SORT individual bucket
# B0 = [11, 12, 14, 18]
# B1 = [29]
# B2 = [31, 35]
# B3 = [42]
# CONCATENATION:
# [11, 12, 14, 18]
# [29]
# [31, 35]
# [42]

#####
# how do decide width of bucket and number of bucket 

#******************************************
# Bucket index:    0       1       2       3
# Value range:   11-14   15-18   19-22   23-26
# arr = [29, 11, 35, 14, 42, 18, 31, 12]
# minimum = min(arr)  # 11
# maximum = max(arr)    # 42
# size = len(arr)  # 8 element
# width = (maximum-minimum + 1)/size = (42-11+1)/8 = 4
# bucket_idx = (num-minmum)/width = for 14 =  (14-11)/4 = 0.75=bucket0
#******************************************
# 11, 12, 13, 14, ... 40, 41, 42 has 32 integer
# range_size or num of integer = maximum - minimum + 1
#  = 42 - 11 + 1 = 32 
#******************************************
# INPUT:
# [29, 11, 35, 14, 42, 18, 31, 12]

# Minimum = 11
# Maximum = 42
# Width   = 4

# BUCKET RANGES:

# B0: 11 - 14
# B1: 15 - 18
# B2: 19 - 22
# B3: 23 - 26
# B4: 27 - 30
# B5: 31 - 34
# B6: 35 - 38
# B7: 39 - 42


# DISTRIBUTION:

# B0 = [11, 14, 12]
# B1 = [18]
# B2 = []
# B3 = []
# B4 = [29]
# B5 = [31]
# B6 = [35]
# B7 = [42]


import math

arr = [29, 11, 35, 14, 42, 18, 31, 12]


# start element of array 11 
minimum = min(arr)
# end element of array 42     
maximum = max(arr)
# lengthof array 8 
size = len(arr)
# 4 width of bucket 
width = math.ceil((maximum - minimum + 1) / size)

# 3. Create empty buckets
buckets = [[] for _ in range(size)]

# 4. Distribute elements
for num in arr:
    # width for each element find bucket index
    b_idx = (num - minimum)
    # add element to array of found bucketidx
    buckets[b_idx].append(num)

# 5. Sort each bucket
for bucket in buckets:
    bucket.sort()

# 6. Combine buckets
result = []

for bucket in buckets:
    result.extend(bucket)

print(result)
# [11, 12, 14, 18, 29, 31, 35, 42]
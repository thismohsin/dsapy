lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

[1, 1, 2, 3, 4, 4, 5, 6]

# look it like matrix of row and column

# 1 4 5
# 1 3 4
# 2 6

# 1. note each array is sorted
# 2. top element is lowest in array
# 3. first column is sorted*

# now push() 1 1 2 on heap first element from column not row.
# these column element decide which row we will target
# pop() n get 1 -- because there is conflict amongst two datapoint, better store row index along with it

# now push again with 1(0idx) 1(1idx) 2(2idx) with column idx -- note heap element are alreaedy sorted with lowest on top
# now we process element of row0 because pop gave value 1 with columnIdx 0 // 1 1 2
# now we pop 1 and push 4 // 1 2 4
# now we pop 1 and push 5 // 2 4 5
# now we pop 2 with rowIdx2 and push // 4 5 6
# what are pop element 1 1 2 4 5 6

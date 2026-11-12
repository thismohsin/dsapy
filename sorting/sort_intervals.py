

# Problem Type	Core Question Being Asked	The Operational Action
# 1. Merge Intervals	"What parts of the day are busy?"	Stretch your boundaries to glue overlapping blocks together.
# 2. Max Activities	"How many things can one single person attend?"	Filter & Reject overlapping activities to keep your schedule open.
# 3. Max Overlapping (Rooms)	"What is the busiest moment of the day?"	Count how many meetings are active at the exact same second.

# cant we use actual set of meeting size - merge interval size?
# No, you cannot simply subtract the size of the merged intervals from the total number of activities to find the maximum number of activities.
# While it feels like a clever shortcut, this math breaks down because merging intervals creates an illusion of how many individual tasks you can actually complete.
# Here is the exact reason why this logic fails, proven by a simple example.

# The Breakdown Example

# Imagine you have 3 activities in your list:
# 1. [1, 10] (A long 9-hour meeting)
# 2. [2, 3]  (A short 1-hour meeting)
# 3. [4, 5]  (Another short 1-hour meeting)

# 1. What happens if you run "Merge Intervals"?

# If you sort by start time and run the merge algorithm:
# • [1, 10] and [2, 3] overlap → Merged into [1, 10]
# • [1, 10] and [4, 5] overlap → Merged into [1, 10]
# The final merged list has exactly 1 interval: [[1, 10]].
# If you try your formula:
# \(\text{Total\ Activities}-\text{Merge\ Interval\ Size}=3-1=2\)
# In this specific scenario, the math happens to give you 2, which matches the maximum number of non-overlapping activities you could do ([2, 3] and [4, 5]).

# 2. Why the math breaks (The Counter-Example)

# Now, let's look at a slightly different set of 3 activities:
# 1. [1, 10] (The same long meeting)
# 2. [2, 5]  (A meeting that overlaps with the long one)
# 3. [3, 6]  (Another meeting that overlaps with the second one)
# Let's run the Merge Intervals logic again:
# • [1, 10] and [2, 5] overlap → Merged into [1, 10]
# • [1, 10] and [3, 6] overlap → Merged into [1, 10]
# The final merged list still has exactly 1 interval: [[1, 10]].
# If you apply your formula here:
# \(3\text{\ (Total)}-1\text{\ (Merged\ Size)}=2\)
# But look closely at the data! Can you actually pick 2 non-overlapping activities?
# • If you pick [1, 10], you can't pick anything else (Total = 1).
# • If you pick [2, 5], it overlaps with [3, 6] and [1, 10] (Total = 1).
# • If you pick [3, 6], it overlaps with [2, 5] and [1, 10] (Total = 1).
# Every single activity in this list clashes with every other activity. The maximum number of activities you can actually attend is 1.
# Your formula calculated 2, which is incorrect.

# Why does the math lie?

# The Merge Intervals algorithm uses a "chain reaction" (transitive property).
# • Event A overlaps Event B.
# • Event B overlaps Event C.
# • Therefore, A, B, and C all merge into one massive block.
# However, just because A overlaps B, and B overlaps C, it does not mean A overlaps C! In Max Activities, you are allowed to completely delete "Event B" out of existence. If you delete B, Event A and Event C might be perfectly compatible. The merge algorithm completely loses sight of these individual compatibilities because it glues everything together into a giant wall.

# Summary

# • Merge Intervals answers: "What total blocks of time are busy?"
# • Max Activities answers: "What is the absolute highest count of individual items I can string together?"


students = [
    ("John", 85),
    ("Sam", 95),
    ("Alex", 75)
]

result = sorted(
    students,
    key=lambda x: x[1],
    reverse=True
)

# #---------------
# intervals = [[5, 8], [1, 3], [2, 6], [9, 10]]

# #after sort
# intervals = [
#     #[start end]
#     [1, 3],
#     [2, 6],
#     [5, 8],
#     [9, 10]
# ]

# merged = [[1, 3]] #first

# for current_start, current_end in intervals[1:]:
#     #[1 3]
#     #[2, 6] [5, 8] [9, 10]
#     #[2 6] start end = 6
#     last_end = merged[-1][1] # from [1 3], 3
#     if last_end >= current_start: 
#         merged[-1][1] = max(last_end, current_end) 
#         # [1 3][2 6]= 3>2 = merge =  max(3,6)=> [1,6]
#         # [1------3]
#         #     [2---------6]


# 2. In Merge Intervals: last_end is a "Stretching Rubber Band" 🪵

# Because you sorted by Start Time, you are moving strictly from left to right across the timeline.
# • What last_end means: It is the furthest point to the right that your current giant merged block has reached so far.
# • The Logic: When a new interval overlaps, it means this new interval starts inside your current block, but it might stick out further to the right.
# • Why it changes on an overlap: You must grow your block to cover the new ground. You update last_end = max(last_end, current_end).


intervals = [[5, 8], [1, 3], [2, 6], [9, 10]]

# STEP 1: Sort by starting position
# sorting by start time is key
intervals.sort(key=lambda x: x[0])

# STEP 2: Start with the first interval
merged = [intervals[0]]

# STEP 3: Examine remaining intervals
for start, end in intervals[1:]:

    # Last interval currently in merged
    last_end = merged[-1][1]

    # CASE 1: Overlap
    # if new meeting is subset or extended subset of prev meeting then we merge
    # imply - new meet start coincide with end of prev meet end current.start<=pev.end
    if start <= last_end:
        merged[-1][1] = max(last_end, end)

    # CASE 2: No overlap
    elif start > last_end:
        merged.append([start, end])

print(merged)
# [[1, 8], [9, 10]]





# #---- Sorting + Greedy
#Sorting decides the order in which we examine elements.
#Greedy decides whether to select or reject the current element.
# # Maximum non-overlapping activities
# activities = [
#     (1, 4),
#     (3, 5),
#     (0, 6),
#     (5, 7),
#     (8, 9),
#     (5, 9)
# ]


#  Always choose the activity that finishes earliest among the available activities.
# activities.sort(key=lambda x: x[1]) #sort by end

# Index:       0       1       2       3       4       5
# Activity:  (1,4)   (3,5)   (0,6)   (5,7)   (5,9)   (8,9)
# End time:     4       5       6       7       9       9

# Index:       0       1       2       3       4       5
# Activity:  (1,4)   (3,5)   (0,6)   (5,7)   (5,9)   (8,9)
#              ✓

# Selected: (1,4)
# Last end = 4
# Count = 1
# ..
#  activity = (3,5)
#  3 < 4 → OVERLAP ignore
# ..
#  activity = (5,7)
#  5 >= 4 → NO OVERLAP consider
# ....
# Current activity = (5,9)

# 5 < 7 → OVERLAP ignore
# ..
# Index:       0       1       2       3       4       5
# Activity:  (1,4)   (3,5)   (0,6)   (5,7)   (5,9)   (8,9)
#              ✓       ✗       ✗       ✓       ✗

# Selected: (1,4), (5,7)
# Last end = 7
# Count = 2



# In Max Activities: last_end is a "Fixed Shield" 🛡️

# Because you sorted by End Time, the very first activity you pick is guaranteed to end as early as humanly possible.
# • What last_end means: It is the end of the best possible activity you could have picked.
# • The Logic: You use last_end as a shield. Any future activity that tries to start before this shield is rejected.
# • Why it never changes on an overlap: If a subsequent activity overlaps, you ignore it. You do not touch last_end. It stays exactly where it is because you want to keep that early finish time locked in.
def max_activities(activities):

    # STEP 1: Sort by ending time
    # sorted by End Time is key
    activities.sort(key=lambda x: x[1])

    selected = []

    last_end = float('-inf')

    for start, end in activities:

        # CASE 1: Activity does not overlap
        # new activity time is after end of last activity end time then it is valid else pass
        if start >= last_end:

            selected.append((start, end))

            # Update the end boundary
            last_end = end

        # CASE 2: Activity overlaps
        elif start < last_end:

            # Skip this activity
            pass

    return selected

# it does answer question: if first meeting window is 5h and second one is 2h with overlap of 1h and can finish early too -- then second one is better it will allow more meeting?
# Excellent question. You're identifying an important distinction: Why do we choose the earliest finishing meeting rather than simply the shortest meeting?
# Meeting A: (1, 6)   Duration = 5 hours
# Meeting B: (4, 6)   Duration = 2 hours
# Meeting C: (6, 8)   Duration = 2 hours
# Time:    1   2   3   4   5   6   7   8
#          |--- A -----------|
#                      |--- B ---|
#                                  |--- C ---|
# activities.sort(key=lambda x: x[1] - x[0]) -- will order meeting by hours spent





######

#---- Maximum number of overlapping meetings
# meetings = A = [(1, 5) (3, 7)]
# Time:  1   2   3   4   5   6   7

# A:     [---------------]
# B:         [---------------]
# C:                 [---------------]

# A starts at 1  → +1
# A ends at 5    → -1

# B starts at 3  → +1
# B ends at 7    → -1

# (1, +1)
# (3, +1)
# (5, -1)
# (7, -1)
# ---
# TIME  EVENT       ACTIVE     MEANING
# -------------------------------------------
# 1     +1            1        A starts
# 3     -1            0        A ends <-- A ends first before B start
# 5     +1            1        B starts
# 7     -1            0        B ends

# sort (time,value)
# maxActive is 1

# Meeting A [1, 5):
#     (1, +1)
#     (5, -1)

# Meeting B [2, 6):
#     (2, +1)
#     (6, -1)

# Meeting C [4, 7):
#     (4, +1)
#     (7, -1)


# events = [
#     (1, +1),
#     (5, -1),
#     (2, +1),
#     (6, -1),
#     (4, +1),
#     (7, -1)
# ]

# right events.sort() or events.sort(key=lambda x: (x[0], x[1]))
# wrong meetings.sort(key=lambda x: x[0])
# [
#     (1, +1),
#     (2, +1),
#     (4, +1),
#     (5, -1),
#     (6, -1),
#     (7, -1)
# ]

# max_active = 3
def max_overlapping_meetings(meetings):

    events = []

    # STEP 1: Convert meetings into events
    for start, end in meetings:
        events.append((start, +1))
        events.append((end, -1))

    # STEP 2: Sort chronologically
    # At equal times, -1 comes before +1
    events.sort()

    active = 0
    max_active = 0

    # STEP 3: Process every event
    for time, value in events:

        # CASE 1: Meeting starts
        if value == +1:
            active += 1

        # CASE 2: Meeting ends
        elif value == -1:
            active -= 1

        # STEP 4: Update maximum
        if active > max_active:
            max_active = active

    return max_active


meetings = [
    (1, 5),
    (2, 6),
    (4, 7)
]

print(max_overlapping_meetings(meetings))
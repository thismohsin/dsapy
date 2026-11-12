# # Possible answers:

# # 1   2   3   4   5   6   7   8   9
# # N   N   N   Y   Y   Y   Y   Y   Y
# #             ^
# #        Minimum feasible answer

# # Brute
# # for answer in range(min_answer, max_answer + 1):

# #     if is_possible(answer):
# #         return answer

# # BinSearch
# # while left <= right:

# #     mid = (left + right) // 2

# #     if is_feasible(mid):
# #         right = mid - 1
# #     else:
# #         left = mid + 1

# # return left


# ###
# books = [10, 20, 30, 40]
# students = 2
# Every student must receive books.

# Books must be allocated in contiguous order.
# A book cannot be split.
# We want to minimize the maximum pages assigned to any student.
# each student should recieve book

# ## Find the minimum possible maximum pages assigned to one student.
# The largest individual book has 40 pages.
# One student could receive all the books: 10 + 20 + 30 + 40 = 100 pages

### compare cocobanan with this
# books = [10, 20, 30, 40]
# students = 2
# We are searching for the minimum possible value of the maximum pages assigned to a student.
# Can our answer be 30?
# Why Because one book itself has 40 pages. We cannot split a book between students.
# BookPages constraint
# Minimum(Largest book cannot be divided)...Maximum(One student gets everything)
# CocoBanana constraint
# Minimum(positive eating speed) ...Maximum(Finish largest pile in one hour)

# Determine search space -- it is after 40
# 1. Why can't the answer be less than 40?
# if u choose any less then max(books) will result in splitting book which is not allowed.and
# So 100 is a guaranteed upper bound (assuming at least one student).
# Possible maximum pages:

#   1 ........ 39 | 40 ................. 100
#   IMPOSSIBLE    | VALID SEARCH SPACE
#                 |
#               START

# def allocate_books(books, students):

#     left = max(books)
#     right = sum(books)

#     for max_pages in range(left, right + 1):

#         if is_feasible(books, students, max_pages):
#             return max_pages

# Suppose we choose a candidate answer:
# max_pages = 70
# Can we allocate all books to 2 students, such that neither student gets more than 70 pages?
# Books = [10, 20, 30, 40]
# S1 = 10 + 20 + 30 (stop adding next element will exceed threshold)= 60 
# S2 = 40
# 60+40 = 100 max pages done amongst 2 students

# Try different candidate
# Candidate = 40
# Student 1: [10, 20] = 30
# Student 2: [30]     = 30
# Student 3: [40]     = 40
# Students needed = 3 not acceptable


# Maximum pages:  40  50  60  70  80  90  100 //we taking round number for easy understanding
# Feasible:        N   N   Y   Y   Y   Y    Y
#                            ^
#                       First YES


# ---- LOGIC
# Books: [10, 20, 30, 40]

# Student 1:
#           10 → 30 → 60
#           +10 +20 +30
# Next book = 40
# 60 + 40 = 100 > 60
# Move to Student 2:
# Student 2:       40
# Final:
# Student 1 = 60
# Student 2 = 40
# Total students = 2
# ----------

# fail case 
# books = [10, 20, 30, 40]
# students = 2
# max_pages = 50

# s1 = 10,20 why s2 came in because of max 50 constraint check
# s2 = 30
# s3 = 40

# def is_feasible(books, students, max_pages):

#     students_needed = 1
#     current_pages = 0

#     for book in books:

#         pages_if_added = current_pages + book

#         if pages_if_added <= max_pages:

#             current_pages = pages_if_added

#         else:

#             students_needed = students_needed + 1

#             current_pages = book

#     is_possible = students_needed <= students

#     return is_possible


# putting everything together CRUDE
# def allocate_books(books, students):

#     left = max(books)
#     right = sum(books)

#     for max_pages in range(left, right + 1):

#         if is_possible(books, students, max_pages):
#             return max_pages


def is_possible(books, max_students, try_pages):

    students_needed = 1
    current_pages = 0

    for book in books:

        pages_if_added = current_pages + book

        if pages_if_added <= try_pages:

            current_pages = pages_if_added

        else:

            students_needed = students_needed + 1

            current_pages = book

    is_possible = students_needed <= max_students

    return is_possible


def allocate_books_binary(books, students):

    left = max(books)
    right = sum(books)

    while left <= right:

        mid = (left + right) // 2

        if is_possible(books, students, mid):

            right = mid - 1

        else:

            left = mid + 1

    return left


###################################
# Capacity To Ship Packages Within D Days

# weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# days = 5

# limit_days=5
# capacity[1...10...55] #55 sum of weight
#         [N....Y...Y]
# sum_weight=55

# test_capacity=15
# valid case move right to mid to find best Y 10...15
# you can say 10 may work may result in split so try

def is_feasible_ship(weights, maxDays, test_capacity):
    days = 1
    current_load = 0
    for weight in range(weights):
        weight_if_added_to_capacity = current_load + weight
        if weight_if_added_to_capacity > test_capacity:
            current_load += weight
        else:
            days = days + 1
            current_load = weight

    is_feasible = days <= maxDays

    return is_feasible



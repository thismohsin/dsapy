# # nums = [2, 5, 1, 3, 7, 6, 4, 8] 
# k = 4 4th element
# n = 8  total element
# 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7
#     ->S L<-
# # ? SMALLEST : k-1 = 3 -----> 4 smallest is 4 at idx 3 
# # ? LARGEST  : n-k = 4 ------> 4 largest is 5 at idx 4

        #       Partition array
        #             |
        #             v
        #       pivot_idx
        #             |
        #   Compare with target_index
        #             |
        #    +--------+--------+
        #    |        |        |
        # pivot <   pivot >   pivot ==
        # target    target    target
        #    |        |        |
        # Search    Search    RETURN --- search range is subject where desired index is compared with pivot idx
        # RIGHT      LEFT     pivot


# pivot_idx < desired_index	RHS (right side)	low = pivot_idx + 1 -- changing lookup range
# pivot_idx > desired_index	LHS (left side)	    high = pivot_idx - 1 -- changing lookup range
# pivot_idx == desired_index	Found	        Return pivot



class Solution:

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    
    def partition(self, nums, low, high):

        # Select the last element as pivot
        pivot = nums[high]
        pivot_idx = high

        # small trace pointer boundary of small 
        small = low

        # Scan every element except the pivot between low..high
        for scan in range(low, high):

            # CASE 1: Current element belongs to the smaller partition
            # if scan-th element is SMALLER then PIVOT then we swap with scan
            if nums[scan] <= pivot:

                # Move the smaller element to the small boundary
                self.swap(nums, small, scan)

                # Expand the smaller partition
                small += 1

            # CASE 2: Current element belongs to the larger partition
            # if scan-th element is GREATER then PIVOT then we pass
            else:

                # Do nothing.
                # Element stays in place for now.
                # small does not move.
                # scan automatically moves to the next element.
                pass

        # Place pivot between smaller and larger partitions
        self.swap(nums, small, pivot_idx)

        # Return pivot's final sorted position
        return small

# Index:    0   1   2   3   4   5   6
# nums:    [2,  5,  1,  3,  7,  6,  4]
#           S                     P
#           SC

#        scan=0 
#        small=0
#        nums[scan] <= pivot : 2 <= 4  → TRUE
#        swap(nums, small, scan) : swap(0, 0)
#        nums = [2, 5, 1, 3, 7, 6, 4]
#        small++ =1
#        scan++ =1
#        [2,  5,  1,  3,  7,  6,  4] inplace

#        scan=1
#        small=1
#        nums[scan] <= pivot : 5 <= 4  → FALSE ::::: if scan element is greater then pivot then we noswap
#        noswaps
#        scan++ =2

#         [2,  5,  1,  3,  7,  6,  4] no change
#         scan=2
#         small=1
#         nums[scan] <= pivot : 1 <= 4  → TRUE ::::: if scan element is smaller then pivot then we swap
#         swap(nums, small, scan) : swap(1, 2)
#         scan++ =3
#         small++ =2
#         [2, 1, 5, 3, 7, 6, 4] transition 1 and 5 swapped after comparing with pivot
       
##########
# [2, 5, 1, 3, 7, 6, 4]
#  S/SC                 P

# 2 <= 4  TRUE → swap(0,0)
# [2, 5, 1, 3, 7, 6, 4]
#     S/SC              P

# 5 <= 4  FALSE → no swap
# [2, 5, 1, 3, 7, 6, 4]
#     S     SC         P

# 1 <= 4  TRUE → swap(1,2)
# [2, 1, 5, 3, 7, 6, 4]
#        S     SC      P

# 3 <= 4  TRUE → swap(2,3)
# [2, 1, 3, 5, 7, 6, 4]
#           S     SC   P

# 7 <= 4  FALSE → no swap
# [2, 1, 3, 5, 7, 6, 4]
#           S        SC P

# 6 <= 4  FALSE → no swap
# [2, 1, 3, 5, 7, 6, 4]
#           S           P

# Final pivot swap (small, high):
# [2, 1, 3, 4, 7, 6, 5]
#           P


    def findKthLargest(self, nums: list[int], k: int) -> int:

        desired_index = len(nums) - k

        low = 0
        high = len(nums) - 1

        while low <= high:

            pivot_idx = self.partition(nums, low, high)

            # Pivot reached desired position
            if pivot_idx == desired_index:
                return nums[pivot_idx]

            # Answer is on RHS
            elif pivot_idx < desired_index:
                low = pivot_idx + 1

            # Answer is on LHS
            else:
                high = pivot_idx - 1


    def quickSort(self, nums, low, high):

        if low < high:

            # Partition and get pivot's final position
            pivot_idx = self.partition(nums, low, high)

            # Sort LHS of pivot
            self.quickSort(nums, low, pivot_idx - 1)

            # Sort RHS of pivot
            self.quickSort(nums, pivot_idx + 1, high)

        return nums

            #             [2, 5, 1, 3, 7, 6, 4]
            #                     |
            #              PARTITION (4)
            #                     |
            #        [2, 1, 3]  4  [7, 6, 5]
            #            |              |
            #       QUICK SORT      QUICK SORT
            #            |              |
            #      PARTITION (3)   PARTITION (5)
            #            |              |
            #        [2, 1] 3       5 [6, 7]
            #          |              |
            #     QUICK SORT      QUICK SORT
            #          |              |
            #        [1] 2         [6] 7
            #          |              |
            #       SORTED         SORTED

            #   FINAL: [1, 2, 3, 4, 5, 6, 7]


#             QUICK SORT                       QUICKSELECT
# ----------                       ------------
#       PARTITION                       PARTITION
#           |                               |
#      +----+----+                          |
#      |         |                    Compare pivot_idx
#     LHS       RHS                   with desired_index
#      |         |                          |
#   SORT LHS  SORT RHS                 +----+----+
#      |         |                     |         |
#  PARTITION PARTITION               LHS       RHS
#      |         |                     |         |
#  Continue  Continue                Search    Search
#  both      both                    only one  only one
#      |         |                     |         |
#      +----+----+                     +----+----+
#           |                               |
#     SORTED ARRAY                     ANSWER FOUND
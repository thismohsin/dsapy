# ============================================================
# P5 — BINARY SEARCH TREE (BST)
# ============================================================
#
#  31. BST Properties
#  32. Build BST
#  33. Search in BST                               LC #700
#  34. Insert into BST                             LC #701
#  35. Validate BST                                LC #98
#  36. Kth Smallest Element                        LC #230
#  37. Minimum Absolute Difference                 LC #530
#  38. LCA in BST                                  LC #235
#  39. Delete Node in BST                          LC #450
#  40. Range Sum of BST                            LC #938
#  41. Convert Sorted Array to BST                 LC #108
#
# ============================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 31. BST PROPERTIES
    # ========================================================
    #
    # TREE:
    #
    #               5
    #              / \
    #             3   7
    #            / \ / \
    #           2  4 6  8
    #
    # RULE:
    # For every node:
    #   All values in LEFT subtree  < node.val
    #   All values in RIGHT subtree > node.val
    #
    # INORDER of a BST = SORTED sequence:
    # 2, 3, 4, 5, 6, 7, 8
    #
    # SEARCH: O(log n) when balanced — halve search space each step.
    #
    # ========================================================


    # ========================================================
    # 32. BUILD BST
    # ========================================================
    #
    # INPUT: [5, 3, 7, 2, 4, 6, 8]
    #
    # OUTPUT:
    #
    #               5
    #              / \
    #             3   7
    #            / \ / \
    #           2  4 6  8
    #
    # ========================================================

    def buildBST(self, values):

        root = None

        for val in values:
            root = self.insert(root, val)

        return root

    # (insert defined below as LC #701)


    # ========================================================
    # 33. LC #700 — SEARCH IN BST
    # ========================================================
    #
    # INPUT:
    #
    #               5
    #              / \
    #             3   7
    #            / \
    #           2   4
    #
    # SEARCH TARGET: 3
    #
    # OUTPUT: node with value 3
    #
    # INTUITION:
    # At each node, target tells you which direction to go.
    # Less than → go left. Greater than → go right.
    #
    # STAGING:
    #
    # STEP 1: node = 5. target 3 < 5 → go left
    # STEP 2: node = 3. target 3 == 3 → return node
    #
    # ========================================================

    def searchBST(self, root, val):

        # BASE CASE: not found.
        if root is None:
            return None

        # STEP 1: Found.
        if root.val == val:
            return root

        # STEP 2: Target is smaller — go left.
        if val < root.val:
            return self.searchBST(root.left, val)

        # STEP 3: Target is larger — go right.
        return self.searchBST(root.right, val)


    # ========================================================
    # 34. LC #701 — INSERT INTO BST
    # ========================================================
    #
    # INPUT:
    #
    #               5
    #              / \
    #             3   7
    #
    # INSERT: 4
    #
    # OUTPUT:
    #
    #               5
    #              / \
    #             3   7
    #              \
    #               4
    #
    # INTUITION:
    # Follow BST ordering until you hit a None slot.
    # Insert there.
    #
    # STAGING:
    #
    # STEP 1: node = 5. 4 < 5 → go left
    # STEP 2: node = 3. 4 > 3 → go right
    # STEP 3: node = None → insert new node here
    #
    # ========================================================

    def insert(self, root, val):

        # BASE CASE: empty slot found — insert here.
        if root is None:
            return TreeNode(val)

        # STEP 1: Value is smaller — go left.
        if val < root.val:
            root.left = self.insert(root.left, val)

        # STEP 2: Value is larger — go right.
        elif val > root.val:
            root.right = self.insert(root.right, val)

        # Equal values: no duplicates inserted.

        return root


    # ========================================================
    # 35. LC #98 — VALIDATE BST
    # ========================================================
    #
    # INPUT:
    #
    #               5
    #              / \
    #             3   7
    #            / \
    #           2   4
    #
    # OUTPUT:
    # True
    #
    # INVALID TREE:
    #
    #               5
    #              / \
    #             3   7
    #              \
    #               6    ← 6 > 5 but is in left subtree of 5
    #
    # OUTPUT:
    # False
    #
    # INTUITION:
    # Checking only left < parent < right is NOT enough.
    # Every node must stay within a valid min/max range.
    #
    # LOGIC:
    # Pass min and max boundaries down the tree.
    # Left child: max shrinks to parent value.
    # Right child: min grows to parent value.
    #
    # STAGING:
    #
    # STEP 1: validate(5, min=-inf, max=+inf) → 5 in range
    # STEP 2: validate(3, min=-inf, max=5)    → 3 in range
    # STEP 3: validate(6, min=3, max=5)       → 6 > 5 → False
    #
    # ========================================================

    def isValidBST(self, root):

        def validate(node, min_val, max_val):

            # BASE CASE:
            if node is None:
                return True

            # STEP 1: Check current node is within range.
            if node.val <= min_val or node.val >= max_val:
                return False

            # STEP 2: Left subtree — upper bound shrinks.
            left_valid = validate(node.left, min_val, node.val)

            # STEP 3: Right subtree — lower bound grows.
            right_valid = validate(node.right, node.val, max_val)

            return left_valid and right_valid

        return validate(root, float("-inf"), float("inf"))


    # ========================================================
    # 36. LC #230 — KTH SMALLEST ELEMENT IN BST
    # ========================================================
    #
    # INPUT:
    #
    #               3
    #              / \
    #             1   4
    #              \
    #               2
    #
    # K = 2
    #
    # OUTPUT:
    # 2
    #
    # INTUITION:
    # Inorder traversal of BST gives sorted values.
    # The kth value in inorder = kth smallest.
    #
    # STAGING (inorder of tree above):
    # 1 → 2 → 3 → 4
    # k=2 → return 2
    #
    # TRANSITION:
    # Use a counter. When count reaches k, save the answer.
    #
    # ========================================================

    def kthSmallest(self, root, k):

        self.count = 0
        self.result = 0

        def inorder(node):

            if node is None:
                return

            # STEP 1: Traverse left.
            inorder(node.left)

            # STEP 2: Count current node.
            self.count += 1

            if self.count == k:
                self.result = node.val
                return

            # STEP 3: Traverse right.
            inorder(node.right)

        inorder(root)

        return self.result


    # ========================================================
    # 37. LC #530 — MINIMUM ABSOLUTE DIFFERENCE IN BST
    # ========================================================
    #
    # INPUT:
    #
    #               4
    #              / \
    #             2   6
    #            / \
    #           1   3
    #
    # OUTPUT:
    # 1
    #
    # INTUITION:
    # Inorder gives sorted values.
    # Minimum difference is always between adjacent values.
    #
    # STAGING (inorder):
    # 1 → 2 → 3 → 4 → 6
    # Differences: 1, 1, 1, 2
    # Minimum = 1
    #
    # TRANSITION:
    # Track previous node in inorder.
    # At each node: diff = current - previous.
    #
    # ========================================================

    def getMinimumDifference(self, root):

        self.prev = None
        self.min_diff = float("inf")

        def inorder(node):

            if node is None:
                return

            # STEP 1: Go left.
            inorder(node.left)

            # STEP 2: Compare with previous.
            if self.prev is not None:
                diff = node.val - self.prev
                self.min_diff = min(self.min_diff, diff)

            # STEP 3: Update previous.
            self.prev = node.val

            # STEP 4: Go right.
            inorder(node.right)

        inorder(root)

        return self.min_diff


    # ========================================================
    # 38. LC #235 — LCA IN BST
    # ========================================================
    #
    # INPUT:
    #
    #               6
    #              / \
    #             2   8
    #            / \ / \
    #           0  4 7  9
    #
    # p = 2, q = 8
    #
    # OUTPUT:
    # Node 6 (LCA)
    #
    # INTUITION:
    # LCA is the first node where p and q split directions.
    # If both are smaller, go left.
    # If both are larger, go right.
    # Otherwise, current node is the LCA.
    #
    # STAGING:
    #
    # STEP 1: node = 6. p=2 < 6, q=8 > 6 → split here → return 6
    #
    # STAGING (p=2, q=4):
    #
    # STEP 1: node = 6. both < 6 → go left
    # STEP 2: node = 2. p=2 == 2 → 2 is ancestor of 4 → return 2
    #
    # ========================================================

    def lowestCommonAncestorBST(self, root, p, q):

        # BASE CASE:
        if root is None:
            return None

        # STEP 1: Both smaller — LCA is in left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorBST(root.left, p, q)

        # STEP 2: Both larger — LCA is in right subtree.
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorBST(root.right, p, q)

        # STEP 3: They split here — current node is the LCA.
        return root


    # ========================================================
    # 39. LC #450 — DELETE NODE IN BST
    # ========================================================
    #
    # INPUT:
    #
    #               5
    #              / \
    #             3   6
    #            / \   \
    #           2   4   7
    #
    # DELETE: 3
    #
    # OUTPUT (one valid answer):
    #
    #               5
    #              / \
    #             4   6
    #            /     \
    #           2       7
    #
    # INTUITION:
    # Find the node. Then handle three cases.
    #
    # CASES:
    # 1. No left child  → replace with right child
    # 2. No right child → replace with left child
    # 3. Two children   → replace value with inorder successor
    #                     (smallest value in right subtree),
    #                     then delete that successor
    #
    # STAGING (delete 3):
    #
    # STEP 1: Find 3.
    # STEP 2: 3 has two children.
    # STEP 3: Inorder successor = smallest in right subtree = 4.
    # STEP 4: Replace 3's value with 4.
    # STEP 5: Delete 4 from right subtree.
    #
    # ========================================================

    def deleteNode(self, root, key):

        # BASE CASE: key not found.
        if root is None:
            return None

        # STEP 1: Navigate to the node to delete.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:

            # CASE 1: No left child.
            if root.left is None:
                return root.right

            # CASE 2: No right child.
            if root.right is None:
                return root.left

            # CASE 3: Two children.
            # Find inorder successor (smallest in right subtree).
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            # Replace value with successor's value.
            root.val = successor.val

            # Delete successor from right subtree.
            root.right = self.deleteNode(root.right, successor.val)

        return root


    # ========================================================
    # 40. LC #938 — RANGE SUM OF BST
    # ========================================================
    #
    # INPUT:
    #
    #               10
    #              /  \
    #             5   15
    #            / \    \
    #           3   7   18
    #
    # RANGE: [7, 15]
    #
    # OUTPUT:
    # 32  (7 + 10 + 15)
    #
    # INTUITION:
    # Use BST ordering to skip entire subtrees outside the range.
    #
    # LOGIC:
    # If node.val < low  → skip left subtree entirely
    # If node.val > high → skip right subtree entirely
    # Otherwise          → add current value, check both sides
    #
    # STAGING:
    #
    # STEP 1: node=10. 7 <= 10 <= 15 → add 10. Check both.
    # STEP 2: node=5.  5 < 7         → skip left, check right
    # STEP 3: node=7.  7 <= 7 <= 15  → add 7. No children.
    # STEP 4: node=15. 7<=15<=15     → add 15. Check right.
    # STEP 5: node=18. 18 > 15       → skip right, check left (None)
    # Total = 10 + 7 + 15 = 32
    #
    # ========================================================

    def rangeSumBST(self, root, low, high):

        # BASE CASE:
        if root is None:
            return 0

        # STEP 1: Node is below range — go right only.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # STEP 2: Node is above range — go left only.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # STEP 3: Node is in range — include it, check both sides.
        left_sum = self.rangeSumBST(root.left, low, high)
        right_sum = self.rangeSumBST(root.right, low, high)

        return root.val + left_sum + right_sum


    # ========================================================
    # 41. LC #108 — CONVERT SORTED ARRAY TO BST
    # ========================================================
    #
    # INPUT:
    # [-10, -3, 0, 5, 9]
    #
    # OUTPUT (one valid answer):
    #
    #               0
    #              / \
    #           -10   5
    #              \   \
    #              -3   9
    #
    # INTUITION:
    # Pick the middle element as root to keep it balanced.
    # Left half becomes left subtree.
    # Right half becomes right subtree.
    #
    # STAGING:
    #
    # STEP 1: array = [-10, -3, 0, 5, 9], mid = 2 (val=0) → root = 0
    # STEP 2: left  = [-10, -3], mid = 0 (val=-10) → root = -10
    # STEP 3: right = [5, 9],    mid = 1 (val=9) → root = 9
    #         left subarray [5] → root = 5
    #
    # ========================================================

    def sortedArrayToBST(self, nums):

        def build(left, right):

            # BASE CASE: no elements.
            if left > right:
                return None

            # STEP 1: Pick middle element as root.
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # STEP 2: Build left subtree from left half.
            node.left = build(left, mid - 1)

            # STEP 3: Build right subtree from right half.
            node.right = build(mid + 1, right)

            return node

        return build(0, len(nums) - 1)


# ============================================================
# FAQ
# ============================================================
#
# Q: Why is inorder traversal sorted for BST?
#
# BST rule: left < node < right.
# Inorder visits left → node → right.
# This naturally produces ascending order.
#
# ---
#
# Q: Why validate using min/max boundaries?
#
# Local comparison (just left/right child) misses cases
# where a deep node violates an ancestor's constraint.
# Passing boundaries tracks the full allowed range.
#
# ---
#
# Q: Why is BST search O(log n) when balanced?
#
# Each step eliminates half the remaining nodes.
# Balanced tree height = log2(n), so at most log2(n) steps.
#
# ---
#
# Q: What happens when duplicate values exist?
#
# Standard BST does not allow duplicates.
# In insert, equal values are ignored (no action).
#
# ---
#
# Q: How to find kth smallest?
#
# Use inorder (sorted order). Count nodes visited.
# When count == k, that is the answer.
#
# ---
#
# Q: How does BST deletion work?
#
# Case 1: No children    → remove node
# Case 2: One child      → replace with that child
# Case 3: Two children   → replace with inorder successor,
#                           delete the successor recursively
#
# ---
#
# Q: BST vs Binary Tree?
#
#  BINARY TREE           BST
#  ===========           ===
#  No ordering rule      left < node < right
#  General structure     Enables O(log n) search
#  Any layout            Always ordered
#
# ============================================================


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    solution = Solution()

    # Build BST from values
    bst = solution.buildBST([5, 3, 7, 2, 4, 6, 8])

    #               5
    #              / \
    #             3   7
    #            / \ / \
    #           2  4 6  8

    found = solution.searchBST(bst, 4)
    print("Search 4:", found.val if found else None)
    # Expected: 4

    print("Valid BST:", solution.isValidBST(bst))
    # Expected: True

    print("Kth Smallest (k=3):", solution.kthSmallest(bst, 3))
    # Expected: 4

    print("Min Diff:", solution.getMinimumDifference(bst))
    # Expected: 1

    p = solution.searchBST(bst, 2)
    q = solution.searchBST(bst, 4)
    lca = solution.lowestCommonAncestorBST(bst, p, q)
    print("LCA(2,4):", lca.val if lca else None)
    # Expected: 3

    bst2 = solution.buildBST([5, 3, 6, 2, 4, 7])
    bst2 = solution.deleteNode(bst2, 3)
    print("Delete 3, inorder root:", bst2.val)
    # Root stays 5

    print("Range Sum [2,5]:", solution.rangeSumBST(bst, 2, 5))
    # Expected: 2 + 3 + 4 + 5 = 14

    sorted_bst = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print("Sorted Array to BST root:", sorted_bst.val)
    # Expected: 0

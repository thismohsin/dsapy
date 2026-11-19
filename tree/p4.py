# ============================================================
# P4 — BASIC TREE RECURSION
# ============================================================
#
#  24. Maximum Depth using DFS                     LC #104
#  25. Minimum Depth using DFS                     LC #111
#  26. Same Tree                                   LC #100
#  27. Symmetric Tree                              LC #101
#  28. Invert Binary Tree                          LC #226
#  29. Count Nodes (basic recursive pattern)
#  30. Leaf Node Detection
#
# ============================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 24. LC #104 — MAXIMUM DEPTH USING DFS
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \
    #           4   5
    #
    # OUTPUT:
    # 3
    #
    # INTUITION:
    # The depth at any node is 1 plus the deeper of its subtrees.
    #
    # LOGIC:
    # DEPTH = 1 + MAX(left depth, right depth)
    # EMPTY NODE = 0
    #
    # STAGING:
    #
    # STEP 1: maxDepth(4) → 1 + max(0, 0) = 1
    # STEP 2: maxDepth(5) → 1 + max(0, 0) = 1
    # STEP 3: maxDepth(2) → 1 + max(1, 1) = 2
    # STEP 4: maxDepth(3) → 1 + max(0, 0) = 1
    # STEP 5: maxDepth(1) → 1 + max(2, 1) = 3
    #
    # TRANSITION:
    # Each call returns its own depth.
    # Parent picks the larger child depth and adds 1.
    #
#         1
#         /
#        2
#       /
#      3

# maxDepth(3) = 1
# maxDepth(2) = 1 + max(1, 0) = 2
# maxDepth(1) = 1 + max(2, 0) = 3
    # ========================================================

#               TREE + RECURSION RETURN VALUES
#               ==============================

#                        1
#                       / \
#                      /   \
#                     /     \
#                    2       3
#                   / \       \
#                  4   5      None
#                  |   |        |
#                  |   |        |
#                  |   |        +-- 0
#                  |   |
#                  |   +-- 1 + max(0, 0) = 1
#                  |
#                  +------ 1 + max(0, 0) = 1


#           NOW NODE 2 CAN CALCULATE:

#                        2
#                       / \
#                      4   5

#              1 + max(1, 1) = 2


#           NOW NODE 3 CALCULATES:

#                        3
#                         \
#                          None

#              1 + max(0, 0) = 1


#           FINALLY ROOT NODE 1 CALCULATES:

#                        1
#                       / \
#                      2   3
#                     (2) (1)

#              1 + max(2, 1) = 3

#               1
#              / \
#             2   3
#            / \
#           4   5

# CALL ORDER (going DOWN):

# 1 → 2 → 4

# RETURN ORDER (coming UP):

# 4 returns 1
# 5 returns 1
# 2 returns 2
# 3 returns 1
# 1 returns 3

    def maxDepth(self, root):

        # BASE CASE:
        if root is None:
            return 0

        # STEP 1: Get depth of left subtree.
        left_depth = self.maxDepth(root.left)

        # STEP 2: Get depth of right subtree.
        right_depth = self.maxDepth(root.right)

        # STEP 3: Return current node + deeper side.
        return 1 + max(left_depth, right_depth) 
        ## maxDepth(3) = 1 -- Note max doesnt get affected by some lhs or rhs missing
        # maxDepth(2) = 1 + max(1, 0) = 2
        # maxDepth(1) = 1 + max(2, 0) = 3


    # ========================================================
    # 25. LC #111 — MINIMUM DEPTH USING DFS
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            /
    #           4
    #
    # PATHS:
    # 1 → 3     = depth 2
    # 1 → 2 → 4 = depth 3
    #
    # OUTPUT:
    # 2
    #
    # INTUITION:
    # A missing child is NOT a leaf.
    # Must reach a node that has NO children on either side.
    #
    # LOGIC:
    # If only one child exists, we must go that direction.
    # We cannot count a missing child as a valid path.
    #
    # STAGING:
    #
    # STEP 1: minDepth(4) → leaf → return 1
    # STEP 2: minDepth(2):
    #   left = 1, right = 0
    #   right is None → go left only → return 1 + 1 = 2
    # STEP 3: minDepth(3) → leaf → return 1
    # STEP 4: minDepth(1):
    #   left = 2, right = 1
    #   both exist → return 1 + min(2, 1) = 2
    #
    # ========================================================
#          1
#         /
#        2
#       /
#      3
# wrong approach
# # minDepth(3) = 1
# # minDepth(2) = 1 + min(1, 0) = 1
# # minDepth(1) = 1 + min(1, 0) = 1
# right approach -- if one node lhs or rhs is missing then dont include in min check they will take the answer down
# # minDepth(3) = 1
# # minDepth(2) = 1 + min(1) = 2
# # minDepth(1) = 1 + min(1) = 3

    def minDepth(self, root):

        # BASE CASE:
        if root is None:
            return 0

        # STEP 1: Leaf node — no children.
        if root.left is None and root.right is None:
            return 1

        # STEP 2: Left child missing — must go right.
        if root.left is None:
            return 1 + self.minDepth(root.right)
        # if lhs is none ignore rhs for min else it will dilute answer

        # STEP 3: Right child missing — must go left.
        if root.right is None:
            return 1 + self.minDepth(root.left) 
        #if rhs is none ignore rhs for min else it will dilute answer

        #if lhs and rhs are present then consider min of both
        # STEP 4: Both children exist — take the shorter path.
        left_depth = self.minDepth(root.left) 
        right_depth = self.minDepth(root.right)
        return 1 + min(left_depth, right_depth)
        ## # minDepth(3) = 1 --- unlike max min get impacted if lhs and rhs miss
        # # minDepth(2) = 1 + min(1) = 2
        # # minDepth(1) = 1 + min(1) = 3


    # ========================================================
    # 26. LC #100 — SAME TREE
    # ========================================================
    #
    # INPUT:
    #
    # TREE P:          TREE Q:
    #
    #     1                1
    #    / \              / \
    #   2   3            2   3
    #
    # OUTPUT:
    # True
    #
    # INTUITION:
    # Two trees are the same if every node matches in value
    # and position simultaneously.
    #
    # LOGIC:
    # Check four conditions at each pair of nodes:
    # 1. Both None      → same
    # 2. One None       → different
    # 3. Values differ  → different
    # 4. Check children recursively
    #
    # STAGING:
    #
    # STEP 1: Compare (1, 1) → equal, check children
    # STEP 2: Compare (2, 2) → equal, check children
    # STEP 3: Compare (None, None) → True
    # STEP 4: Compare (None, None) → True
    # STEP 5: Compare (3, 3) → equal, check children
    # STEP 6: Compare (None, None) → True
    # STEP 7: Compare (None, None) → True
    # Final: True
    #
    # ========================================================

    def isSameTree(self, p, q):

        # CONDITION AND 1: Both nodes are empty.
        if p is None and q is None:
            return True

        # CONDITION OR 2: Only one node is empty.
        if p is None or q is None:
            return False

        # CONDITION 3: Values differ.
        if p.val != q.val:
            return False

        # CONDITION 4: Check left and right subtrees.
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same


    # ========================================================
    # 27. LC #101 — SYMMETRIC TREE
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   2
    #            / \ / \
    #           3  4 4  3
    #
    # OUTPUT:
    # True
    #
    # INTUITION:
    # A mirror — left side is a reflection of right side.
    # Compare left's outer child with right's outer child,
    # and left's inner child with right's inner child.
    #
    # LOGIC:
    #
    # MIRROR PAIRS:
    # left.left  ↔  right.right   (outer) ***
    # left.right ↔  right.left    (inner) ***
    #
    # STAGING:
    #
    # STEP 1: is_mirror(2, 2) → values match
    # STEP 2: is_mirror(3, 3) → outer pair → True
    # STEP 3: is_mirror(4, 4) → inner pair → True
    # Final: True
    #
    # ========================================================

    def isSymmetric(self, root):

        def is_mirror(left_node, right_node):

            # CONDITION 1: Both empty.
            if left_node is None and right_node is None:
                return True

            # CONDITION 2: One empty.
            if left_node is None or right_node is None:
                return False

            # CONDITION 3: Values differ.
            if left_node.val != right_node.val:
                return False

            # CONDITION 4: Outer pair check.
            outer = is_mirror(left_node.left, right_node.right)

            # CONDITION 5: Inner pair check.
            inner = is_mirror(left_node.right, right_node.left)

            return outer and inner

        # BASE CASE:
        if root is None:
            return True

        return is_mirror(root.left, root.right)


    # ========================================================
    # 28. LC #226 — INVERT BINARY TREE
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \ / \
    #           4  5 6  7
    #
    # OUTPUT:
    #
    #               1
    #              / \
    #             3   2
    #            / \ / \
    #           7  6 5  4
    #
    # INTUITION:
    # Swap every node's left and right children,
    # from bottom to top.
    #
    # LOGIC:
    # 1. Invert left subtree.
    # 2. Invert right subtree.
    # 3. Swap the two inverted subtrees.
    #
    # STAGING:
    #
    # STEP 1: invertTree(4) → no children → return node 4
    # STEP 2: invertTree(5) → return node 5
    # STEP 3: invertTree(2):
    #   left = inverted(4) = 4
    #   right = inverted(5) = 5
    #   swap → root.left = 5, root.right = 4
    # STEP 4: invertTree(6), invertTree(7) → return as-is
    # STEP 5: invertTree(3): swap → left=7, right=6
    # STEP 6: invertTree(1): swap → left=3, right=2
    #
    # TRANSITION:
    # Inverted subtrees are returned, then assigned back.
    # Parent receives already-inverted subtrees and swaps them.
    #
    # ========================================================

#        2
#       / \
#    None  None
# left_subtree = self.invertTree(None)
# right_subtree = self.invertTree(None)
# left_subtree = None
# right_subtree = None
# root.left = right_subtree
# root.right = left_subtree
# return root
    
    def invertTree(self, root): 
    # we return none or root out of this function so u can attach node or swap node

        # BASE CASE:
        if root is None:
            return None

        # STEP 1: Invert left subtree.
        left_subtree = self.invertTree(root.left)

        # STEP 2: Invert right subtree.
        right_subtree = self.invertTree(root.right)

        # STEP 3: Swap.
        #taking root changing left right and return root
        root.left = right_subtree
        root.right = left_subtree
        return root


    # ========================================================
    # 29. COUNT NODES — BASIC RECURSIVE PATTERN
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \
    #           4   5
    #
    # OUTPUT:
    # 5
    #
    # INTUITION:
    # Every node contributes 1 to the count.
    # Total = 1 + left count + right count.
    #
    # STAGING:
    #
    # STEP 1: count(4) = 1
    # STEP 2: count(5) = 1
    # STEP 3: count(2) = 1 + 1 + 1 = 3
    # STEP 4: count(3) = 1
    # STEP 5: count(1) = 1 + 3 + 1 = 5
    #
    # ========================================================

    def countNodes(self, root):

        # BASE CASE:
        if root is None:
            return 0

        # STEP 1: Count left.
        left_count = self.countNodes(root.left)

        # STEP 2: Count right.
        right_count = self.countNodes(root.right)

        # STEP 3: Add current node.
        return 1 + left_count + right_count


    # ========================================================
    # 30. LEAF NODE DETECTION
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \
    #           4   5
    #
    # OUTPUT (leaf values):
    # [4, 5, 3]
    #
    # INTUITION:
    # A leaf has no children on either side.
    #
    # LOGIC:
    # left is None AND right is None → it is a leaf.
    #
    # STAGING:
    #
    # STEP 1: Visit 4 → leaf → collect
    # STEP 2: Visit 5 → leaf → collect
    # STEP 3: Visit 2 → has children → skip
    # STEP 4: Visit 3 → leaf → collect
    # STEP 5: Visit 1 → has children → skip
    #
    # ========================================================

    def collectLeaves(self, root):

        leaves = []

        def dfs(node):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Check if leaf.
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return

            # STEP 2: Recurse into children.
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return leaves


# ============================================================
# FAQ
# ============================================================
#
# Q: What should DFS return?
#
# It depends on the problem.
# Height → return an int
# Same tree → return a bool
# Invert → return the modified node
# Path sums → return int (gain or sum)
#
# ---
#
# Q: What happens when node is None?
#
# It is the BASE CASE. Every tree DFS must handle None first.
# Return a neutral value: 0 for counts/heights, True for
# comparisons, None for structural problems.
#
# ---
#
# Q: Why return max(left, right) + 1?
#
# We want the LONGEST path downward.
# We take the larger subtree depth and add 1 for the current node.
#
# ---
#
# Q: How do we compare two trees?
#
# Recursively compare node by node.
# Structurally identical + value identical at every position.
#
# ---
#
# Q: Why do we need two recursive calls?
#
# One tree can branch left and right.
# We must explore both to confirm or deny a property.
#
# ---
#
# Q: What is the difference between return and print?
#
# print  → shows to screen, no value passed back
# return → passes a value back to the caller
# In recursion, return is essential — callers need the result.
#
# ============================================================


# ============================================================
# TEST
# ============================================================

def build_tree():

    #               1
    #              / \
    #             2   3
    #            / \ / \
    #           4  5 6  7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":

    solution = Solution()
    root = build_tree()

    print("Max Depth:", solution.maxDepth(root))
    # Expected: 3

    min_root = TreeNode(1)
    min_root.left = TreeNode(2)
    min_root.right = TreeNode(3)
    min_root.left.left = TreeNode(4)

    print("Min Depth:", solution.minDepth(min_root))
    # Expected: 2

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    print("Same Tree:", solution.isSameTree(p, q))
    # Expected: True

    sym = TreeNode(1)
    sym.left = TreeNode(2)
    sym.right = TreeNode(2)
    sym.left.left = TreeNode(3)
    sym.left.right = TreeNode(4)
    sym.right.left = TreeNode(4)
    sym.right.right = TreeNode(3)

    print("Symmetric:", solution.isSymmetric(sym))
    # Expected: True

    from collections import deque

    invert_root = build_tree()
    solution.invertTree(invert_root)

    def level_order(r):
        if r is None:
            return []
        result = []
        q = deque([r])
        while q:
            size = len(q)
            lvl = []
            for _ in range(size):
                n = q.popleft()
                lvl.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            result.append(lvl)
        return result

    print("Inverted:", level_order(invert_root))
    # Expected: [[1], [3, 2], [7, 6, 5, 4]]

    print("Count Nodes:", solution.countNodes(root))
    # Expected: 7

    print("Leaves:", solution.collectLeaves(root))
    # Expected: [4, 5, 6, 7]

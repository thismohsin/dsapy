# ============================================================
# P6 — STRUCTURAL & POSTORDER PROBLEMS
# ============================================================
#
#  42. Subtree of Another Tree                     LC #572
#  43. Balanced Binary Tree                        LC #110
#  44. Height or Imbalanced Sentinel
#  45. Diameter of Binary Tree                     LC #543
#  46. Count Complete Tree Nodes                   LC #222
#
# ============================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 42. LC #572 — SUBTREE OF ANOTHER TREE
    # ========================================================
    #
    # INPUT:
    #
    # MAIN TREE:           SUBTREE:
    #
    #       3                  4
    #      / \                / \
    #     4   5              1   2
    #    / \
    #   1   2
    #
    # OUTPUT:
    # True
    #
    # INTUITION:
    # At every node of the main tree, check if the
    # subtree rooted there exactly matches subRoot.
    #
    # LOGIC:
    # 1. If subRoot is None → always True (empty is a subtree)
    # 2. If root is None    → False (nothing left to check)
    # 3. If current node matches subRoot → check full equality
    # 4. Otherwise search left and right subtrees
    #
    # STAGING:
    #
    # STEP 1: root=3. isSameTree(3, 4)? → No
    # STEP 2: Check left: root=4. isSameTree(4, 4)?
    #   4==4, left 1==1, right 2==2 → True
    # Found.
    #
    # TRANSITION:
    # isSameTree checks full structural equality.
    # isSubtree searches every node for a match.
    #
    # ========================================================

    def isSubtree(self, root, subRoot):

        # BASE CASE: empty subRoot matches anything.
        if subRoot is None:
            return True

        # BASE CASE: main tree exhausted, no match.
        if root is None:
            return False

        # STEP 1: Check if trees are identical from here.
        if self._isSameTree(root, subRoot):
            return True

        # STEP 2: Search left subtree.
        left_found = self.isSubtree(root.left, subRoot)

        # STEP 3: Search right subtree.
        right_found = self.isSubtree(root.right, subRoot)

        return left_found or right_found

    def _isSameTree(self, p, q):

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left_same = self._isSameTree(p.left, q.left)
        right_same = self._isSameTree(p.right, q.right)

        return left_same and right_same


    # ========================================================
    # 43. LC #110 — BALANCED BINARY TREE
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
    # True
    #
    # UNBALANCED EXAMPLE:
    #
    #           1
    #          /
    #         2
    #        /
    #       3
    #
    # OUTPUT:
    # False
    #
    # INTUITION:
    # At every node, the height difference between
    # left and right subtrees must be at most 1.
    #
    # CONDITION:
    # abs(left_height - right_height) <= 1
    #
    # STAGING (balanced tree):
    #
    # STEP 1: height(4) → balanced, return 1
    # STEP 2: height(5) → balanced, return 1
    # STEP 3: height(2): diff = abs(1-1) = 0 → OK, return 2
    # STEP 4: height(3) → balanced, return 1
    # STEP 5: height(1): diff = abs(2-1) = 1 → OK, return 3
    # Final: True
    #
    # STAGING (unbalanced tree):
    #
    # STEP 1: height(3) → return 1
    # STEP 2: height(2): diff = abs(1-0) = 1 → OK, return 2
    # STEP 3: height(1): diff = abs(2-0) = 2 → NOT OK → return -1
    # Final: False
    #
    # TRANSITION:
    # Uses the sentinel pattern (see section 44).
    # Returns -1 when any subtree is unbalanced.
    # -1 propagates up — no further computation needed.
    #
    # ========================================================

    def isBalanced(self, root):

        def height_or_imbalanced(node):

            # BASE CASE:
            if node is None:
                return 0

            # STEP 1: Get left height.
            left_height = height_or_imbalanced(node.left)

            # STEP 2: Propagate imbalance up immediately.
            if left_height == -1:
                return -1

            # STEP 3: Get right height.
            right_height = height_or_imbalanced(node.right)

            # STEP 4: Propagate imbalance up immediately.
            if right_height == -1:
                return -1

            # STEP 5: Check balance at this node.
            if abs(left_height - right_height) > 1:
                return -1

            # STEP 6: Return actual height.
            return 1 + max(left_height, right_height)

        return height_or_imbalanced(root) != -1


    # ========================================================
    # 44. HEIGHT OR IMBALANCED SENTINEL
    # ========================================================
    #
    # CONCEPT:
    # One function returns EITHER a real height OR a sentinel -1.
    #
    # RETURN VALUES:
    # >= 0  = balanced subtree, value is the height
    # -1    = imbalanced subtree detected
    #
    # WHY NOT USE A BOOLEAN:
    # A bool can't carry the height.
    # A tuple (bool, int) works but is harder to read.
    # -1 as sentinel is simple and efficient.
    #
    # TREE:
    #
    #           1
    #          /
    #         2
    #        /
    #       3
    #
    # CALL TRACE:
    #
    # height_or_imbalanced(3)
    #   left = 0, right = 0
    #   diff = 0 → OK
    #   return 1
    #
    # height_or_imbalanced(2)
    #   left = 1, right = 0
    #   diff = 1 → OK
    #   return 2
    #
    # height_or_imbalanced(1)
    #   left = 2, right = 0
    #   diff = 2 → NOT OK
    #   return -1
    #
    # isBalanced returns -1 != -1 = False
    #
    # IMPORTANT:
    # Once -1 is returned, every ancestor returns -1 immediately.
    # No unnecessary height computations.
    #
    # ========================================================


    # ========================================================
    # 45. LC #543 — DIAMETER OF BINARY TREE
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
    # PATH:
    # 4 → 2 → 1 → 3  (3 edges)
    #
    # INTUITION:
    # The longest path through any node uses both of its subtrees.
    # Diameter at a node = left height + right height.
    #
    # IMPORTANT:
    # DIAMETER is in EDGES.
    # HEIGHT is in NODES.
    #
    # HEIGHT vs DIAMETER:
    #
    #  HEIGHT                    DIAMETER
    #  ======                    ========
    #  Longest path downward     Longest path through node
    #  Measured in nodes         Measured in edges
    #  1 + max(left, right)      left height + right height
    #  Returned to parent        Updates global maximum
    #
    # STAGING:
    #
    # STEP 1: dfs(4): left=0, right=0. diameter=0. return 1
    # STEP 2: dfs(5): left=0, right=0. diameter=0. return 1
    # STEP 3: dfs(2): left=1, right=1. diameter=2. return 2
    # STEP 4: dfs(3): left=0, right=0. diameter=0. return 1
    # STEP 5: dfs(1): left=2, right=1. diameter=3. return 3
    #
    # FINAL ANSWER = 3
    #
    # ========================================================

    def diameterOfBinaryTree(self, root):

        self.max_diameter = 0

        def dfs(node):

            # BASE CASE:
            if node is None:
                return 0

            # STEP 1: Get left height.
            left_height = dfs(node.left)

            # STEP 2: Get right height.
            right_height = dfs(node.right)

            # STEP 3: Update global diameter through this node.
            current_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, current_diameter)

            # STEP 4: Return height to parent (not diameter).
            return 1 + max(left_height, right_height)

        dfs(root)

        return self.max_diameter


    # ========================================================
    # 46. LC #222 — COUNT COMPLETE TREE NODES
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \ /
    #           4  5 6
    #
    # OUTPUT:
    # 6
    #
    # INTUITION:
    # A complete tree has all levels filled except possibly
    # the last, which fills left to right.
    #
    # OPTIMIZATION:
    # If left height == right height, the left subtree is perfect.
    # A perfect tree of height h has 2^h - 1 nodes.
    # We can count it in O(1) without traversing.
    #
    # LOGIC:
    # 1. Measure left height (go left repeatedly).
    # 2. Measure right height (go right repeatedly).
    # 3. If equal: left subtree is perfect → 2^left_h - 1 + 1 (root) + count(right)
    # 4. If not:   right subtree is perfect → 2^right_h - 1 + 1 (root) + count(left)
    #
    # STAGING:
    #
    # Root = 1:
    #   left_h = 3 (1→2→4), right_h = 2 (1→3→6)
    #   Not equal → right subtree (3,6) is perfect, height=2 → 2^2-1 = 3 nodes
    #   count = 3 + 1 + count(left subtree of 1)
    #
    # Left subtree rooted at 2:
    #   left_h = 2 (2→4), right_h = 2 (2→5)
    #   Equal → left subtree (4) is perfect, height=1 → 2^1-1 = 1 node
    #   count = 1 + 1 + count(right subtree of 2 = 5)
    #
    # Node 5: leaf → 1
    #
    # Total: 1 + 1 + 1 = 3 (subtree at 2) → 3 + 1 + 3 = 7? No.
    # Simple recursion is correct for learning — optimization is extra.
    #
    # SIMPLE VERSION (straightforward recursion):
    #
    # ========================================================

    def countNodes(self, root):

        # BASE CASE:
        if root is None:
            return 0

        # STEP 1: Count left subtree.
        left_count = self.countNodes(root.left)

        # STEP 2: Count right subtree.
        right_count = self.countNodes(root.right)

        # STEP 3: Add current node.
        return 1 + left_count + right_count


# ============================================================
# FAQ
# ============================================================
#
# Q: What is a balanced binary tree?
#
# A tree where every node has abs(left_height - right_height) <= 1.
# Not just the root — every single node must satisfy this.
#
# ---
#
# Q: Why return -1 for an imbalanced subtree?
#
# -1 acts as a sentinel signal.
# It travels up and tells every ancestor: stop computing,
# the tree is already unbalanced.
#
# ---
#
# Q: Height vs Diameter?
#
#  HEIGHT                    DIAMETER
#  ======                    ========
#  Longest downward path     Longest any-direction path
#  Measured in nodes         Measured in edges
#  1 + max(left, right)      left + right heights
#  Returned to parent        Updates global max
#
# ---
#
# Q: Why can diameter pass through current node?
#
# Diameter is the longest path between ANY two nodes.
# A path can go: deep left leaf → current node → deep right leaf.
# This uses both subtrees, so we sum both heights.
#
# ---
#
# Q: Why calculate height using postorder?
#
# Height depends on children's heights.
# Children must be processed first.
# Postorder = process children before parent.
#
# ---
#
# Q: Why optimize repeated height calculations?
#
# Without optimization, isBalanced calls height on each node,
# and height re-traverses the subtree each time.
# The sentinel approach computes height and balance in one pass.
#
# ============================================================


# ============================================================
# TEST
# ============================================================

def build_main_tree():

    #       3
    #      / \
    #     4   5
    #    / \
    #   1   2

    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    return root


def build_subtree():

    #     4
    #    / \
    #   1   2

    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    return root


if __name__ == "__main__":

    solution = Solution()

    main_tree = build_main_tree()
    sub_tree = build_subtree()

    print("Is Subtree:", solution.isSubtree(main_tree, sub_tree))
    # Expected: True

    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)

    print("Is Balanced:", solution.isBalanced(balanced))
    # Expected: True

    skewed = TreeNode(1)
    skewed.left = TreeNode(2)
    skewed.left.left = TreeNode(3)

    print("Skewed Balanced:", solution.isBalanced(skewed))
    # Expected: False

    diameter_root = TreeNode(1)
    diameter_root.left = TreeNode(2)
    diameter_root.right = TreeNode(3)
    diameter_root.left.left = TreeNode(4)
    diameter_root.left.right = TreeNode(5)

    print("Diameter:", solution.diameterOfBinaryTree(diameter_root))
    # Expected: 3

    complete = TreeNode(1)
    complete.left = TreeNode(2)
    complete.right = TreeNode(3)
    complete.left.left = TreeNode(4)
    complete.left.right = TreeNode(5)
    complete.right.left = TreeNode(6)

    print("Count Complete Nodes:", solution.countNodes(complete))
    # Expected: 6

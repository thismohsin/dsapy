# ============================================================
# P8 — TREE PATH & SUM PATTERNS
# ============================================================
#
#  53. Path Sum                                    LC #112
#  54. Path Sum II                                 LC #113
#  55. Binary Tree Paths                           LC #257
#  56. Sum Root to Leaf Numbers                    LC #129
#  57. Path Sum III                                LC #437
#  58. Maximum Path Sum                            LC #124
#  59. House Robber III                            LC #337
#
# ============================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 53. LC #112 — PATH SUM
    # ========================================================
    #
    # INPUT:
    #
    #               5
    #              / \
    #             4   8
    #            /   / \
    #           11  13   4
    #          /  \       \
    #         7    2       1
    #
    # TARGET: 22
    #
    # PATH: 5 → 4 → 11 → 2 = 22
    #
    # OUTPUT:
    # True
    #
    # INTUITION:
    # Subtract current node value from target as we go down.
    # At a leaf, check if the remaining target equals 0.
    #
    # LOGIC:
    # remaining = target - node.val
    # At leaf: return remaining == 0
    #
    # STAGING:
    #
    # STEP 1: node=5, remaining = 22-5 = 17
    # STEP 2: node=4, remaining = 17-4 = 13
    # STEP 3: node=11, remaining = 13-11 = 2
    # STEP 4: node=2, remaining = 2-2 = 0, leaf → True
    #
    # ========================================================

    def hasPathSum(self, root, targetSum):

        # BASE CASE: empty node.
        if root is None:
            return False

        # STEP 1: Subtract current node value.
        remaining = targetSum - root.val

        # STEP 2: At a leaf — check if target is met.
        if root.left is None and root.right is None:
            return remaining == 0

        # STEP 3: Check left and right subtrees.
        left_found = self.hasPathSum(root.left, remaining)
        right_found = self.hasPathSum(root.right, remaining)

        return left_found or right_found


    # ========================================================
    # 54. LC #113 — PATH SUM II
    # ========================================================
    #
    # INPUT:
    #
    #               5
    #              / \
    #             4   8
    #            /   / \
    #           11  13   4
    #          /  \     / \
    #         7    2   5   1
    #
    # TARGET: 22
    #
    # OUTPUT:
    # [[5, 4, 11, 2], [5, 8, 4, 5]]
    #
    # INTUITION:
    # Same as Path Sum, but collect the full path.
    # Use backtracking — add node before recursing, remove after.
    #
    # LOGIC:
    # At leaf: if remaining == 0 → save a copy of current path.
    # Backtrack: remove current node before returning to parent.
    #
    # STAGING:
    #
    # path = []
    #
    # STEP 1: visit 5 → path=[5], remaining=17
    # STEP 2: visit 4 → path=[5,4], remaining=13
    # STEP 3: visit 11 → path=[5,4,11], remaining=2
    # STEP 4: visit 7 → path=[5,4,11,7], leaf, remaining=-5 → skip
    #         remove 7 → path=[5,4,11]
    # STEP 5: visit 2 → path=[5,4,11,2], leaf, remaining=0 → save
    #         remove 2 → path=[5,4,11]
    # (backtrack continues up to find second path 5→8→4→5)
    #
    # ========================================================

    def pathSum(self, root, targetSum):

        result = []

        def dfs(node, remaining, path):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Add current node to path.
            path.append(node.val)
            remaining -= node.val

            # STEP 2: At leaf — check if path is valid.
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(list(path))

            else:

                # STEP 3: Recurse into children.
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            # STEP 4: Backtrack — remove current node.
            path.pop()

        dfs(root, targetSum, [])

        return result


    # ========================================================
    # 55. LC #257 — BINARY TREE PATHS
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #              \
    #               5
    #
    # OUTPUT:
    # ["1->2->5", "1->3"]
    #
    # INTUITION:
    # Collect every root-to-leaf path as a string.
    # Build the path string as we go down.
    #
    # STAGING:
    #
    # STEP 1: visit 1 → path = "1"
    # STEP 2: visit 2 → path = "1->2"
    # STEP 3: visit 5 → path = "1->2->5", leaf → save
    # STEP 4: visit 3 → path = "1->3", leaf → save
    #
    # ========================================================

    def binaryTreePaths(self, root):

        result = []

        def dfs(node, path):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Extend path with current node.
            if path == "":
                current_path = str(node.val)
            else:
                current_path = path + "->" + str(node.val)

            # STEP 2: At leaf — save path.
            if node.left is None and node.right is None:
                result.append(current_path)
                return

            # STEP 3: Recurse.
            dfs(node.left, current_path)
            dfs(node.right, current_path)

        dfs(root, "")

        return result


    # ========================================================
    # 56. LC #129 — SUM ROOT TO LEAF NUMBERS
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #
    # PATHS:
    # 1 → 2 = number 12
    # 1 → 3 = number 13
    #
    # OUTPUT:
    # 12 + 13 = 25
    #
    # INTUITION:
    # At each level, shift the current number left (multiply by 10)
    # and add the current node's digit.
    #
    # LOGIC:
    # current_number = parent_number * 10 + node.val
    #
    # STAGING:
    #
    # STEP 1: node=1, number = 0*10+1 = 1
    # STEP 2: node=2, number = 1*10+2 = 12, leaf → return 12
    # STEP 3: node=3, number = 1*10+3 = 13, leaf → return 13
    # Total = 12 + 13 = 25
    #
    # ========================================================

    def sumNumbers(self, root):

        def dfs(node, current_number):

            # BASE CASE:
            if node is None:
                return 0

            # STEP 1: Build current number.
            current_number = current_number * 10 + node.val

            # STEP 2: At leaf — return the formed number.
            if node.left is None and node.right is None:
                return current_number

            # STEP 3: Sum from both subtrees.
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            return left_sum + right_sum

        return dfs(root, 0)


    # ========================================================
    # 57. LC #437 — PATH SUM III
    # ========================================================
    #
    # INPUT:
    #
    #               10
    #              /  \
    #             5   -3
    #            / \    \
    #           3   2   11
    #          / \   \
    #         3  -2   1
    #
    # TARGET: 8
    #
    # OUTPUT:
    # 3
    #
    # VALID PATHS:
    # 5 → 3               = 8
    # 5 → 2 → 1           = 8
    # -3 → 11             = 8
    #
    # IMPORTANT:
    # Paths do NOT need to start at root or end at leaf.
    # They must go downward (parent to child).
    #
    # INTUITION:
    # Use prefix sums.
    # prefix_sum = sum from root to current node.
    # A valid path ends at current node when:
    # prefix_sum - target exists in earlier prefix sums.
    #
    # LOGIC:
    # count[prefix_sum - target] = number of valid paths ending here
    #
    # STAGING:
    #
    # count = {0: 1}  ← empty prefix (sum 0 seen once)
    #
    # STEP 1: node=10, prefix=10
    #         look for 10-8=2 in count → 0 paths
    #         count = {0:1, 10:1}
    #
    # STEP 2: node=5, prefix=15
    #         look for 15-8=7 → 0
    #         count = {0:1, 10:1, 15:1}
    #
    # STEP 3: node=3, prefix=18
    #         look for 18-8=10 → count[10]=1 → 1 path found (5→3)
    #         count = {0:1, 10:1, 15:1, 18:1}
    #
    # BACKTRACK: remove prefix 18 before going up.
    #
    # ========================================================

    def pathSumIII(self, root, targetSum):

        count = {0: 1}
        self.result = 0

        def dfs(node, prefix_sum):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Update running prefix sum.
            prefix_sum += node.val

            # STEP 2: Count paths ending at this node.
            needed = prefix_sum - targetSum

            if needed in count:
                self.result += count[needed]

            # STEP 3: Record this prefix sum.
            count[prefix_sum] = count.get(prefix_sum, 0) + 1

            # STEP 4: Recurse into children.
            dfs(node.left, prefix_sum)
            dfs(node.right, prefix_sum)

            # STEP 5: Backtrack — remove this prefix sum.
            count[prefix_sum] -= 1

        dfs(root, 0)

        return self.result


    # ========================================================
    # 58. LC #124 — BINARY TREE MAXIMUM PATH SUM
    # ========================================================
    #
    # INPUT:
    #
    #               8
    #               |
    #               4
    #              / \
    #             2   6
    #
    # OUTPUT:
    # 18
    #
    # PATH: 2 → 4 → 8 = 18
    #
    # INTUITION:
    # At each node:
    # The best path through this node = left gain + node + right gain.
    # Gain = what we return to parent = node + MAX(left, right).
    # We cannot return both arms to the parent — it would create
    # a branch, which is not a valid single path.
    #
    # GAIN vs MAXIMUM:
    #
    #  GAIN                        MAXIMUM
    #  ====                        =======
    #  node + max(left, right)     node + left + right
    #  What parent can extend      Complete path through node
    #  Returned to parent          Updates global answer
    #
    # IMPORTANT EDGE CASE:
    # Negative gain is worse than not using that subtree.
    # So gain = max(0, actual_gain).
    #
    # STAGING:
    #
    # STEP 1: dfs(2): left=0, right=0. max_sum=2. return 2
    # STEP 2: dfs(6): left=0, right=0. max_sum=6. return 6
    # STEP 3: dfs(4): left=2, right=6. path=2+4+6=12. max_sum=12. return 4+6=10
    # STEP 4: dfs(8): left=10, right=0. path=10+8=18. max_sum=18. return 8+10=18
    #
    # ========================================================

    def maxPathSum(self, root):

        self.max_sum = float("-inf")

        def dfs(node):

            # BASE CASE:
            if node is None:
                return 0

            # STEP 1: Get left gain (ignore negative).
            left_gain = max(0, dfs(node.left))

            # STEP 2: Get right gain (ignore negative).
            right_gain = max(0, dfs(node.right))

            # STEP 3: Complete path through this node.
            path_sum = node.val + left_gain + right_gain

            # STEP 4: Update global maximum.
            self.max_sum = max(self.max_sum, path_sum)

            # STEP 5: Return one-sided gain to parent.
            return node.val + max(left_gain, right_gain)

        dfs(root)

        return self.max_sum


    # ========================================================
    # 59. LC #337 — HOUSE ROBBER III
    # ========================================================
    #
    # INPUT:
    #
    #               3
    #              / \
    #             2   3
    #              \   \
    #               3   1
    #
    # OUTPUT:
    # 7
    #
    # PATH: Rob 3 (root's left) + 3 (root's left-right) + 1 (root's right-right)
    # = 3 + 3 + 1 = 7
    #
    # INTUITION:
    # Adjacent nodes cannot both be robbed.
    # At each node we have two choices:
    #   ROB current node  → skip both children
    #   SKIP current node → children can be robbed or skipped (take their max)
    #
    # LOGIC:
    # Return a pair: (rob_current, skip_current)
    #
    # rob_current  = node.val + skip_left + skip_right
    # skip_current = max(rob_left, skip_left) + max(rob_right, skip_right)
    #
    # STAGING:
    #
    # STEP 1: dfs(3) [right-right leaf]:
    #   rob = 1 + 0 + 0 = 1
    #   skip = 0
    #   return (1, 0)
    #
    # STEP 2: dfs(3) [right child of root]:
    #   rob = 3 + 0 + 0 = 3  (can't take child 1 if taking 3)
    #   skip = max(1,0) = 1
    #   return (3, 1)
    #
    # STEP 3: dfs(3) [left-right leaf]:
    #   return (3, 0)
    #
    # STEP 4: dfs(2) [left child of root]:
    #   rob = 2 + 0 + 0 = 2  (no left child, right skip=0)
    #   skip = max(3,0) = 3
    #   return (2, 3)
    #
    # STEP 5: dfs(3) [root]:
    #   rob  = 3 + skip_left + skip_right = 3 + 3 + 1 = 7
    #   skip = max(2,3) + max(3,1) = 3 + 3 = 6
    #   return (7, 6)
    #
    # ANSWER = max(7, 6) = 7
    #
    # ========================================================

    def rob(self, root):

        def dfs(node):

            # BASE CASE: no node contributes nothing.
            if node is None:
                return (0, 0)

            # STEP 1: Get results from children.
            rob_left, skip_left = dfs(node.left)
            rob_right, skip_right = dfs(node.right)

            # STEP 2: Rob this node — skip both children.
            rob_current = node.val + skip_left + skip_right

            # STEP 3: Skip this node — take best from each child.
            skip_current = max(rob_left, skip_left) + max(rob_right, skip_right)

            return (rob_current, skip_current)

        rob_root, skip_root = dfs(root)

        return max(rob_root, skip_root)


# ============================================================
# FAQ
# ============================================================
#
# Q: What is a root-to-leaf path?
#
# A path that starts at the root and ends at a LEAF node.
# Every node along the way is a direct parent-child connection.
#
# ---
#
# Q: How to pass remaining target sum?
#
# Subtract node.val as you go down.
# At the leaf, check if remaining == 0.
#
# ---
#
# Q: Why use backtracking?
#
# When building paths, we add a node before recursing
# and remove it after. This reuses the same list for all paths
# without creating new lists at every step.
#
# ---
#
# Q: Path Sum II vs Path Sum III?
#
#  PATH SUM II              PATH SUM III
#  ===========              ============
#  Root-to-leaf only        Any downward path
#  Exact path collected     Count of paths only
#  Uses backtracking        Uses prefix sums
#
# ---
#
# Q: What is prefix sum in a tree?
#
# Running total from root to current node.
# If (prefix_sum - target) was seen before,
# there is a subpath ending here with that sum.
#
# ---
#
# Q: Maximum Sum vs Maximum Gain?
#
#  MAXIMUM SUM              MAXIMUM GAIN
#  ===========              ============
#  left + node + right      node + max(left, right)
#  Full path through node   One-sided, given to parent
#  Updates global answer    Returned to caller
#
# ---
#
# Q: Why can returned gain use only one child?
#
# A path must be a straight line — no branching.
# If we returned both arms, the parent would receive
# a Y-shaped path, which is invalid.
#
# ---
#
# Q: Why can global maximum use both children?
#
# The global maximum tracks the best COMPLETE path ending here.
# At this node we are the "peak" — both arms connect through us.
# We are not returning this to a parent, so branching is fine.
#
# ---
#
# Q: Why does House Robber return two states?
#
# The choice to rob or skip at a node affects the parent's options.
# By returning both (rob, skip), the parent can make the optimal
# decision without re-computing.
#
# ============================================================


# ============================================================
# TEST
# ============================================================

def build_path_sum_tree():

    #               5
    #              / \
    #             4   8
    #            /   / \
    #           11  13   4
    #          /  \     / \
    #         7    2   5   1

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    return root


if __name__ == "__main__":

    solution = Solution()

    tree = build_path_sum_tree()

    print("Has Path Sum 22:", solution.hasPathSum(tree, 22))
    # Expected: True

    print("Path Sum II (22):", solution.pathSum(tree, 22))
    # Expected: [[5, 4, 11, 2], [5, 8, 4, 5]]

    paths_root = TreeNode(1)
    paths_root.left = TreeNode(2)
    paths_root.right = TreeNode(3)
    paths_root.left.right = TreeNode(5)

    print("Binary Tree Paths:", solution.binaryTreePaths(paths_root))
    # Expected: ["1->2->5", "1->3"]

    sum_root = TreeNode(1)
    sum_root.left = TreeNode(2)
    sum_root.right = TreeNode(3)

    print("Sum Root to Leaf:", solution.sumNumbers(sum_root))
    # Expected: 25

    ps3_root = TreeNode(10)
    ps3_root.left = TreeNode(5)
    ps3_root.right = TreeNode(-3)
    ps3_root.left.left = TreeNode(3)
    ps3_root.left.right = TreeNode(2)
    ps3_root.right.right = TreeNode(11)
    ps3_root.left.left.left = TreeNode(3)
    ps3_root.left.left.right = TreeNode(-2)
    ps3_root.left.right.right = TreeNode(1)

    print("Path Sum III (8):", solution.pathSumIII(ps3_root, 8))
    # Expected: 3

    mps_root = TreeNode(8)
    mps_root.left = TreeNode(4)
    mps_root.left.left = TreeNode(2)
    mps_root.left.right = TreeNode(6)

    print("Max Path Sum:", solution.maxPathSum(mps_root))
    # Expected: 18

    rob_root = TreeNode(3)
    rob_root.left = TreeNode(2)
    rob_root.right = TreeNode(3)
    rob_root.left.right = TreeNode(3)
    rob_root.right.right = TreeNode(1)

    print("House Robber III:", solution.rob(rob_root))
    # Expected: 7

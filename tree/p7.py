# ============================================================
# P7 — TREE RELATIONSHIPS & CONSTRUCTION
# ============================================================
#
#  47. LCA in Binary Tree                          LC #236
#  48. Construct from Preorder + Inorder           LC #105
#  49. Construct from Inorder + Postorder          LC #106
#  50. Construct from Preorder + Postorder         LC #889 [Extra]
#  51. Construct BST from Preorder                 LC #1008
#  52. Flatten Binary Tree to Linked List          LC #114
#
# ============================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 47. LC #236 — LOWEST COMMON ANCESTOR (BINARY TREE)
    # ========================================================
    #
    # INPUT:
    #
    #               3
    #              / \
    #             5   1
    #            / \ / \
    #           6  2 0  8
    #             / \
    #            7   4
    #
    # p = 5, q = 1
    # OUTPUT: Node 3
    #
    # p = 5, q = 4
    # OUTPUT: Node 5
    #
    # INTUITION:
    # Go deep. When you find p or q, return it.
    # The node where both sides return a non-None value is the LCA.
    # If one side is None, the LCA is entirely in the other side.
    #
    # LOGIC:
    # 1. BASE CASE: node is None OR node is p OR node is q → return node
    # 2. Search left and right.
    # 3. Both non-None → current node is LCA.
    # 4. One is None   → LCA is the non-None side.
    #
    # STAGING (p=5, q=1):
    #
    # STEP 1: lca(3): search left and right
    # STEP 2: lca(5): node == p → return node 5
    # STEP 3: lca(1): node == q → return node 1
    # STEP 4: back at 3: left=5, right=1 → both non-None → return 3
    #
    # STAGING (p=5, q=4):
    #
    # STEP 1: lca(3): search left and right
    # STEP 2: lca(5): node == p → return node 5 immediately
    #         (4 is below 5, but 5 is already the ancestor)
    # STEP 3: lca(1): no match → return None
    # STEP 4: back at 3: left=5, right=None → return 5
    #
    # ========================================================

    def lowestCommonAncestor(self, root, p, q):

        # BASE CASE: empty node or found p or q.
        if root is None:
            return None

        if root == p or root == q:
            return root

        # STEP 1: Search left subtree.
        left_result = self.lowestCommonAncestor(root.left, p, q)

        # STEP 2: Search right subtree.
        right_result = self.lowestCommonAncestor(root.right, p, q)

        # STEP 3: Both found — current node is LCA.
        if left_result is not None and right_result is not None:
            return root

        # STEP 4: Only one side found — return that side.
        if left_result is not None:
            return left_result

        return right_result


    # ========================================================
    # 48. LC #105 — CONSTRUCT FROM PREORDER + INORDER
    # ========================================================
    #
    # INPUT:
    # preorder = [3, 9, 20, 15, 7]
    # inorder  = [9, 3, 15, 20, 7]
    #
    # OUTPUT:
    #
    #               3
    #              / \
    #             9  20
    #               / \
    #              15   7
    #
    # INTUITION:
    # Preorder first element = ROOT.
    # Find root in inorder → everything LEFT is left subtree,
    #                         everything RIGHT is right subtree.
    #
    # LOGIC:
    # 1. Root = preorder[0]
    # 2. Find root in inorder → index mid
    # 3. Left subtree size = mid (elements before root in inorder)
    # 4. Recurse: left  = preorder[1 : 1+left_size], inorder[:mid]
    #             right = preorder[1+left_size:],    inorder[mid+1:]
    #
    # STAGING:
    #
    # STEP 1: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
    #         root=3, mid=1 (index of 3 in inorder)
    #         left size = 1
    #         left  preorder=[9], inorder=[9]
    #         right preorder=[20,15,7], inorder=[15,20,7]
    #
    # STEP 2: Build left: root=9, no children → Node(9)
    #
    # STEP 3: Build right:
    #         root=20, mid=1 (index of 20 in [15,20,7])
    #         left  preorder=[15], inorder=[15]  → Node(15)
    #         right preorder=[7],  inorder=[7]   → Node(7)
    #
    # ========================================================

    def buildTree_pre_in(self, preorder, inorder):

        # BASE CASE:
        if not preorder or not inorder:
            return None

        # STEP 1: Root is always first in preorder.
        root_val = preorder[0]
        root = TreeNode(root_val)

        # STEP 2: Find root's position in inorder.
        mid = inorder.index(root_val)

        # STEP 3: Left subtree elements.
        root.left = self.buildTree_pre_in(
            preorder[1 : 1 + mid],
            inorder[:mid]
        )

        # STEP 4: Right subtree elements.
        root.right = self.buildTree_pre_in(
            preorder[1 + mid:],
            inorder[mid + 1:]
        )

        return root


    # ========================================================
    # 49. LC #106 — CONSTRUCT FROM INORDER + POSTORDER
    # ========================================================
    #
    # INPUT:
    # inorder   = [9, 3, 15, 20, 7]
    # postorder = [9, 15, 7, 20, 3]
    #
    # OUTPUT:
    #
    #               3
    #              / \
    #             9  20
    #               / \
    #              15   7
    #
    # INTUITION:
    # Postorder LAST element = ROOT.
    # Find root in inorder → split left and right.
    #
    # STAGING:
    #
    # STEP 1: postorder=[9,15,7,20,3], last=3 → root=3
    #         mid=1 (index of 3 in inorder)
    #         left  inorder=[9], postorder=[9]
    #         right inorder=[15,20,7], postorder=[15,7,20]
    #
    # STEP 2: Build left: root=9 → Node(9)
    #
    # STEP 3: Build right: last=20 → root=20
    #         left=[15], right=[7]
    #
    # ========================================================

    def buildTree_in_post(self, inorder, postorder):

        # BASE CASE:
        if not inorder or not postorder:
            return None

        # STEP 1: Root is always last in postorder.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # STEP 2: Find root in inorder.
        mid = inorder.index(root_val)

        # STEP 3: Left subtree.
        root.left = self.buildTree_in_post(
            inorder[:mid],
            postorder[:mid]
        )

        # STEP 4: Right subtree.
        root.right = self.buildTree_in_post(
            inorder[mid + 1:],
            postorder[mid: -1]
        )

        return root


    # ========================================================
    # 50. LC #889 — CONSTRUCT FROM PREORDER + POSTORDER [Extra]
    # ========================================================
    #
    # INPUT:
    # preorder  = [1, 2, 4, 5, 3, 6, 7]
    # postorder = [4, 5, 2, 6, 7, 3, 1]
    #
    # OUTPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \ / \
    #           4  5 6  7
    #
    # INTUITION:
    # preorder[0]  = root
    # preorder[1]  = left subtree root
    # Find preorder[1] in postorder → index gives left subtree size
    #
    # IMPORTANT:
    # Preorder + postorder can have MULTIPLE valid trees
    # when the tree is not full (some nodes have one child).
    # LeetCode guarantees a full binary tree for this problem.
    #
    # STAGING:
    #
    # STEP 1: pre[0]=1 → root=1
    #         pre[1]=2 → left subtree root
    #         Find 2 in post=[4,5,2,6,7,3,1] → index=2
    #         Left size = 2+1 = 3
    #         Left  pre=[2,4,5], post=[4,5,2]
    #         Right pre=[3,6,7], post=[6,7,3]
    #
    # STEP 2: Build left: root=2, pre[1]=4
    #         Find 4 in [4,5,2] → index=0, left size=1
    #         Left=[4], Right=[5]
    #
    # ========================================================

    def constructFromPrePost(self, preorder, postorder):

        # BASE CASE:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        # STEP 1: Left child is second element in preorder.
        left_root_val = preorder[1]

        # STEP 2: Find it in postorder to get left subtree size.
        left_size = postorder.index(left_root_val) + 1

        # STEP 3: Build left subtree.
        root.left = self.constructFromPrePost(
            preorder[1 : 1 + left_size],
            postorder[:left_size]
        )

        # STEP 4: Build right subtree.
        root.right = self.constructFromPrePost(
            preorder[1 + left_size:],
            postorder[left_size: -1]
        )

        return root


    # ========================================================
    # 51. LC #1008 — CONSTRUCT BST FROM PREORDER
    # ========================================================
    #
    # INPUT:
    # preorder = [8, 5, 1, 7, 10, 12]
    #
    # OUTPUT:
    #
    #               8
    #              / \
    #             5  10
    #            / \   \
    #           1   7   12
    #
    # INTUITION:
    # preorder[0] = root.
    # Find the first value greater than root → right subtree starts.
    # Everything before it (after root) = left subtree.
    # Everything after it = right subtree.
    #
    # STAGING:
    #
    # STEP 1: root=8. Find first > 8 in [5,1,7,10,12] → index 3 (val=10)
    #         left  = [5, 1, 7]
    #         right = [10, 12]
    #
    # STEP 2: Build left: root=5. Find first > 5 in [1,7] → index 1 (val=7)
    #         left=[1], right=[7]
    #
    # STEP 3: Build right: root=10. Find first > 10 in [12] → index 0
    #         left=[], right=[12]
    #
    # ========================================================

    def bstFromPreorder(self, preorder):

        # BASE CASE:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        # STEP 1: Find the split point for right subtree.
        split = len(preorder)

        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                split = i
                break

        # STEP 2: Build left subtree.
        root.left = self.bstFromPreorder(preorder[1:split])

        # STEP 3: Build right subtree.
        root.right = self.bstFromPreorder(preorder[split:])

        return root


    # ========================================================
    # 52. LC #114 — FLATTEN BINARY TREE TO LINKED LIST
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   5
    #            / \   \
    #           3   4   6
    #
    # OUTPUT (in-place, right-only linked list):
    #
    # 1 → 2 → 3 → 4 → 5 → 6
    #
    # This is preorder traversal order.
    #
    # INTUITION:
    # At each node:
    # 1. Flatten left subtree.
    # 2. Flatten right subtree.
    # 3. Attach left subtree to the right.
    # 4. Find tail of left subtree.
    # 5. Attach original right subtree at the tail.
    # 6. Set left to None.
    #
    # STAGING:
    #
    # STEP 1: flatten(3) → no children, done
    # STEP 2: flatten(4) → no children, done
    # STEP 3: flatten(2):
    #   left = 3→4 (already flat)
    #   right = 4 (already flat)
    #   tail of left = 4
    #   4.right = original right (node 4... already same)
    #   Hmm — let's trace clearly:
    #
    # State after flatten(2):
    #   2.right = 3
    #   3.right = 4
    #   4.right = None (original right, already attached)
    #   2.left  = None
    #
    # STEP 4: flatten(6) → done
    # STEP 5: flatten(5):
    #   no left subtree
    #   5.right = 6
    # STEP 6: flatten(1):
    #   left flat = 2→3→4
    #   right flat = 5→6
    #   tail of left = 4
    #   4.right = 5
    #   1.right = 2
    #   1.left  = None
    #
    # RESULT: 1→2→3→4→5→6
    #
    # ========================================================

    def flatten(self, root):

        # BASE CASE:
        if root is None:
            return

        # STEP 1: Flatten left subtree.
        self.flatten(root.left)

        # STEP 2: Flatten right subtree.
        self.flatten(root.right)

        # STEP 3: Save the original right subtree.
        original_right = root.right

        # STEP 4: Move left subtree to right.
        root.right = root.left
        root.left = None

        # STEP 5: Find tail of the new right (was left).
        tail = root

        while tail.right is not None:
            tail = tail.right

        # STEP 6: Attach original right subtree at tail.
        tail.right = original_right


# ============================================================
# FAQ
# ============================================================
#
# Q: How does preorder identify the root?
#
# Preorder visits ROOT first.
# preorder[0] is always the root of the current subtree.
#
# ---
#
# Q: How does inorder divide left and right?
#
# Inorder visits LEFT → ROOT → RIGHT.
# Once we know where root is in inorder, everything before
# it is the left subtree, everything after is the right.
#
# ---
#
# Q: Why use a hashmap?
#
# Finding root in inorder is O(n) with list.index().
# A hashmap maps value → index in O(1).
# For large trees this speeds up construction significantly.
#
# ---
#
# Q: How does recursion build subtrees?
#
# Root is identified, then sub-arrays are sliced.
# Each recursive call builds the subtree for its slice.
# Returns the root of that subtree to its parent.
#
# ---
#
# Q: Can preorder + postorder uniquely build every binary tree?
#
# No. Only when the tree is full (every node has 0 or 2 children).
# If a node has only one child, we cannot tell if it is left or right.
#
# ---
#
# Q: How to find LCA without BST ordering?
#
# Use postorder DFS. Search left and right recursively.
# If both sides return a match, current node is the LCA.
# If only one side returns a match, propagate it upward.
#
# ---
#
# Q: How to rearrange pointers when flattening?
#
# Process bottom-up (postorder).
# At each node: left flat → right, attach original right at tail.
#
# ============================================================


# ============================================================
# TEST
# ============================================================

def level_order(root):

    if root is None:
        return []

    from collections import deque

    result = []
    q = deque([root])

    while q:
        size = len(q)
        level = []
        for _ in range(size):
            n = q.popleft()
            level.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        result.append(level)

    return result


if __name__ == "__main__":

    solution = Solution()

    # LCA test
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left        # node 5
    q = root.right       # node 1

    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA(5,1):", lca.val)
    # Expected: 3

    p2 = root.left          # node 5
    q2 = root.left.right.right  # node 4

    lca2 = solution.lowestCommonAncestor(root, p2, q2)
    print("LCA(5,4):", lca2.val)
    # Expected: 5

    # Build from preorder + inorder
    tree1 = solution.buildTree_pre_in([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print("Pre+In root:", tree1.val, "| level order:", level_order(tree1))
    # Expected root: 3, levels: [[3], [9, 20], [15, 7]]

    # Build from inorder + postorder
    tree2 = solution.buildTree_in_post([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print("In+Post root:", tree2.val)
    # Expected: 3

    # Build BST from preorder
    tree3 = solution.bstFromPreorder([8, 5, 1, 7, 10, 12])
    print("BST from Pre root:", tree3.val, "| levels:", level_order(tree3))
    # Expected root: 8, levels: [[8], [5, 10], [1, 7, 12]]

    # Flatten
    flat = TreeNode(1)
    flat.left = TreeNode(2)
    flat.right = TreeNode(5)
    flat.left.left = TreeNode(3)
    flat.left.right = TreeNode(4)
    flat.right.right = TreeNode(6)

    solution.flatten(flat)

    vals = []
    cur = flat
    while cur:
        vals.append(cur.val)
        cur = cur.right

    print("Flattened:", vals)
    # Expected: [1, 2, 3, 4, 5, 6]

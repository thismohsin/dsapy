# ============================================================
# P2 — DFS TRAVERSALS
# ============================================================
#
#  11. Preorder Traversal                          LC #144
#  12. Inorder Traversal                           LC #94
#  13. Postorder Traversal                         LC #145
#  14. Recursive DFS
#  15. Iterative DFS using Stack
#  16. DFS Execution / Call Stack Visualization
#
# ============================================================


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 11. LC #144 — PREORDER TRAVERSAL
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
    # [1, 2, 4, 5, 3, 6, 7]
    #
    # INTUITION:
    # Visit the current node BEFORE going into its children.
    # "Pre" means first.
    #
    # LOGIC:
    # ORDER: ROOT → LEFT → RIGHT
    #
    # STAGING:
    #
    # STEP 1: Visit 1  → result = [1]
    # STEP 2: Visit 2  → result = [1, 2]
    # STEP 3: Visit 4  → result = [1, 2, 4]
    # STEP 4: Visit 5  → result = [1, 2, 4, 5]
    # STEP 5: Visit 3  → result = [1, 2, 4, 5, 3]
    # STEP 6: Visit 6  → result = [1, 2, 4, 5, 3, 6]
    # STEP 7: Visit 7  → result = [1, 2, 4, 5, 3, 6, 7]
    #
    # TRANSITION:
    # Each call appends current node, then recurses left, then right.
    #
    # ========================================================

    def preorderTraversal(self, root):

        result = []

        def dfs(node):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Visit current node first.
            result.append(node.val)

            # STEP 2: Traverse left subtree.
            dfs(node.left)

            # STEP 3: Traverse right subtree.
            dfs(node.right)

        dfs(root)

        return result


    # ========================================================
    # 12. LC #94 — INORDER TRAVERSAL
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
    # [4, 2, 5, 1, 6, 3, 7]
    #
    # INTUITION:
    # Visit left subtree fully, then current node, then right.
    # For a BST this produces sorted order.
    #
    # LOGIC:
    # ORDER: LEFT → ROOT → RIGHT
    #
    # STAGING:
    #
    # STEP 1: Go left to 4. Visit 4.   → [4]
    # STEP 2: Back to 2. Visit 2.      → [4, 2]
    # STEP 3: Go right to 5. Visit 5.  → [4, 2, 5]
    # STEP 4: Back to 1. Visit 1.      → [4, 2, 5, 1]
    # STEP 5: Go left to 6. Visit 6.   → [4, 2, 5, 1, 6]
    # STEP 6: Back to 3. Visit 3.      → [4, 2, 5, 1, 6, 3]
    # STEP 7: Go right to 7. Visit 7.  → [4, 2, 5, 1, 6, 3, 7]
    #
    # TRANSITION:
    # Recurse left fully → append current → recurse right.
    #
    # ========================================================

    def inorderTraversal(self, root):

        result = []

        def dfs(node):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Traverse left subtree.
            dfs(node.left)

            # STEP 2: Visit current node.
            result.append(node.val)

            # STEP 3: Traverse right subtree.
            dfs(node.right)

        dfs(root)

        return result


    # ========================================================
    # 13. LC #145 — POSTORDER TRAVERSAL
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
    # [4, 5, 2, 6, 7, 3, 1]
    #
    # INTUITION:
    # Visit both children fully before visiting the current node.
    # "Post" means last.
    #
    # LOGIC:
    # ORDER: LEFT → RIGHT → ROOT
    #
    # STAGING:
    #
    # STEP 1: Visit 4  → [4]
    # STEP 2: Visit 5  → [4, 5]
    # STEP 3: Visit 2  → [4, 5, 2]
    # STEP 4: Visit 6  → [4, 5, 2, 6]
    # STEP 5: Visit 7  → [4, 5, 2, 6, 7]
    # STEP 6: Visit 3  → [4, 5, 2, 6, 7, 3]
    # STEP 7: Visit 1  → [4, 5, 2, 6, 7, 3, 1]
    #
    # TRANSITION:
    # Recurse left, recurse right, then append current node.
    #
    # ========================================================

    def postorderTraversal(self, root):

        result = []

        def dfs(node):

            # BASE CASE:
            if node is None:
                return

            # STEP 1: Traverse left subtree.
            dfs(node.left)

            # STEP 2: Traverse right subtree.
            dfs(node.right)

            # STEP 3: Visit current node last.
            result.append(node.val)

        dfs(root)

        return result


    # ========================================================
    # 14. RECURSIVE DFS
    # ========================================================
    #
    # INTUITION:
    # Recursion naturally follows the call stack — each call
    # goes deeper before returning.
    #
    # PATTERN (same structure for all three traversals):
    #
    # def dfs(node):
    #     if node is None: return
    #     # [ preorder position ]
    #     dfs(node.left)
    #     # [ inorder position ]
    #     dfs(node.right)
    #     # [ postorder position ]
    #
    # WHERE you place the work (append/compute) defines the order.
    #
    # ========================================================


    # ========================================================
    # 15. ITERATIVE DFS USING STACK
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
    # OUTPUT (preorder):
    # [1, 2, 4, 5, 3]
    #
    # INTUITION:
    # Replace the call stack with an explicit stack.
    # Push right child before left so left is processed first.
    #
    # LOGIC:
    # 1. Push root onto stack.
    # 2. While stack is not empty:
    #    a. Pop node.
    #    b. Visit node.
    #    c. Push right child (processed later).
    #    d. Push left child (processed next).
    #
    # STAGING (STACK STATE):
    #
    # INIT:      stack = [1]
    # POP 1:     visit 1, push 3 then 2 → stack = [3, 2]
    # POP 2:     visit 2, push 5 then 4 → stack = [3, 5, 4]
    # POP 4:     visit 4, no children   → stack = [3, 5]
    # POP 5:     visit 5, no children   → stack = [3]
    # POP 3:     visit 3, no children   → stack = []
    #
    # TRANSITION:
    # Right is pushed before left so that left is on top and
    # popped first — matching recursive preorder.
    #
    # ========================================================

    def preorderIterative(self, root):

        result = []

        if root is None:
            return result

        stack = [root]

        while len(stack) > 0:

            # STEP 1: Take next node from stack.
            node = stack.pop()

            # STEP 2: Visit it.
            result.append(node.val)

            # STEP 3: Push right first (processed later).
            if node.right is not None:
                stack.append(node.right)

            # STEP 4: Push left second (processed next).
            if node.left is not None:
                stack.append(node.left)

        return result


    # ========================================================
    # 16. DFS EXECUTION / CALL STACK VISUALIZATION
    # ========================================================
    #
    # TREE:
    #
    #               1
    #              / \
    #             2   3
    #
    # RECURSIVE PREORDER CALL STACK:
    #
    # dfs(1)                   ← enters first
    #   dfs(2)                 ← goes left
    #     dfs(None) → return   ← base case
    #     dfs(None) → return   ← base case
    #   ← returns from dfs(2), visits 2
    #   dfs(3)                 ← goes right
    #     dfs(None) → return
    #     dfs(None) → return
    #   ← returns from dfs(3), visits 3
    # ← returns from dfs(1), visits 1
    #
    # ORDER:
    # 1. Call goes DOWN (deeper into tree).
    # 2. Return goes UP (back toward root).
    # 3. BASE CASE (None) is the stopping point.
    #
    # ========================================================


# ============================================================
# FAQ
# ============================================================
#
# Q: Preorder vs Inorder vs Postorder?
#
#  ORDER         VISIT TIME         USE CASE
#  =========     ==========         ========
#  Preorder      Before children    Copy/serialize tree
#  Inorder       Between children   Sorted output (BST)
#  Postorder     After children     Delete/compute tree
#
# ---
#
# Q: When is the root processed?
#
# Preorder  → root first
# Inorder   → root in the middle
# Postorder → root last
#
# ---
#
# Q: Why does postorder process children first?
#
# Children must be processed before the parent can use
# their results. Example: computing height requires knowing
# children's heights first.
#
# ---
#
# Q: How does recursion return to parent?
#
# When a function reaches its base case or its last line,
# it returns. Control passes back to the caller.
# The caller continues from where it left off.
#
# ---
#
# Q: How to implement DFS using a stack?
#
# Use an explicit list as a stack.
# Push right before left so left is processed first.
# Pop → visit → push children.
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

    print("Preorder (recursive):", solution.preorderTraversal(root))
    # Expected: [1, 2, 4, 5, 3, 6, 7]

    print("Inorder:", solution.inorderTraversal(root))
    # Expected: [4, 2, 5, 1, 6, 3, 7]

    print("Postorder:", solution.postorderTraversal(root))
    # Expected: [4, 5, 2, 6, 7, 3, 1]

    print("Preorder (iterative):", solution.preorderIterative(root))
    # Expected: [1, 2, 4, 5, 3, 6, 7]

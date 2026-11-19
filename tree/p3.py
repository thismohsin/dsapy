# ============================================================
# P3 — BFS / LEVEL ORDER TRAVERSALS
# ============================================================
#
#  17. Queue Fundamentals
#  18. Level Order Traversal                       LC #102
#  19. Right Side View                             LC #199
#  20. Zigzag Level Order                          LC #103
#  21. Average of Levels                           LC #637
#  22. Maximum Depth using BFS                     LC #104
#  23. Minimum Depth using BFS                     LC #111
#
# ============================================================


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # ========================================================
    # 17. QUEUE FUNDAMENTALS
    # ========================================================
    #
    # A QUEUE is a First-In First-Out (FIFO) structure.
    #
    # OPERATIONS:
    #
    # enqueue (append) → add to the back
    # dequeue (popleft) → remove from the front
    #
    # EXAMPLE:
    #
    # enqueue 1 → [1]
    # enqueue 2 → [1, 2]
    # enqueue 3 → [1, 2, 3]
    # dequeue   → returns 1, queue = [2, 3]
    # dequeue   → returns 2, queue = [3]
    #
    # WHY QUEUE FOR BFS:
    # We process nodes level by level.
    # The first node we add is the first we process.
    # This guarantees left-to-right, top-to-bottom order.
    #
    # ========================================================


    # ========================================================
    # 18. LC #102 — LEVEL ORDER TRAVERSAL
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
    # [[1], [2, 3], [4, 5, 6, 7]]
    #
    # INTUITION:
    # Process one full level at a time.
    # All nodes at the same depth form one group.
    #
    # LOGIC:
    # 1. Start queue with root.
    # 2. Each iteration: snapshot the current queue size.
    #    That size = number of nodes at this level.
    # 3. Process exactly that many nodes.
    # 4. Their children go into the queue for the next level.
#     #
#      TREE              ACTION          QUEUE (FRONT → BACK)
# ──────────────────────────────────────────────────────────

#        1           START           [1]

#        1           POP 1           []
#       / \
#      2   3          PUSH 2         [2]
#                     PUSH 3         [2, 3]

#  LEVEL 1 = [1]
# ──────────────────────────────────────────────────────────

#        1           POP 2           [3]
#       / \
#      2   3          PUSH 4         [3, 4]
#     / \             PUSH 5         [3, 4, 5]

#        1           POP 3           [4, 5]
#       / \
#      2   3          PUSH 6         [4, 5, 6]
#     / \             PUSH 7         [4, 5, 6, 7]
#    4  5 6 7

#  LEVEL 2 = [2, 3]
# ──────────────────────────────────────────────────────────

#        1           POP 4           [5, 6, 7]
#       / \
#      2   3          POP 5           [6, 7]
#     / \ / \         POP 6           [7]
#    4  5 6  7        POP 7           []

#  LEVEL 3 = [4, 5, 6, 7]
# ──────────────────────────────────────────────────────────

#  OUTPUT = [[1], [2, 3], [4, 5, 6, 7]]
    # ========================================================

    def levelOrder(self, root):

        result = []

        if root is None:
            return result

        queue = deque([root])

        while len(queue) > 0:

            # Snapshot size = number of nodes at this level.
            level_size = len(queue)

            current_level = []

            for i in range(level_size):

                # STEP 1: Take next node at this level.
                node = queue.popleft()

                # STEP 2: Record its value.
                current_level.append(node.val)

                # STEP 3: Enqueue children for next level.
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(current_level)

        return result


    # ========================================================
    # 19. LC #199 — RIGHT SIDE VIEW
    # ========================================================
    #
    # INPUT:
    #
    #               1
    #              / \
    #             2   3
    #            / \   \
    #           4   5   7
    #
    # OUTPUT:
    # [1, 3, 7]
    #
    # INTUITION:
    # From the right side, you see only the last node
    # of each level.
    #
    # LOGIC:
    # Do level order traversal.
    # Take only the last node of each level.
    #
    # STAGING:
    #
    # LEVEL 1: [1]      → last = 1
    # LEVEL 2: [2, 3]   → last = 3
    # LEVEL 3: [4, 5, 7] → last = 7
    #
    # TRANSITION:
    # After processing each level, append current_level[-1].
    #
    # ========================================================

    def rightSideView(self, root):

        result = []

        if root is None:
            return result

        queue = deque([root])

        while len(queue) > 0:

            level_size = len(queue)

            last_val = 0

            for i in range(level_size):

                node = queue.popleft()

                # Track last node seen at this level.
                last_val = node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(last_val)

        return result


    # ========================================================
    # 20. LC #103 — ZIGZAG LEVEL ORDER
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
    # [[1], [3, 2], [4, 5, 6, 7]]
    #
    # INTUITION:
    # Alternate direction each level.
    # Even levels: left to right.
    # Odd levels: right to left.
    #
    # LOGIC:
    # Same as level order.
    # Track level number (even/odd).
    # If odd level, reverse current level before appending.
    #
    # STAGING:
    #
    # LEVEL 0 (even): [1]       → keep as [1]
    # LEVEL 1 (odd):  [2, 3]    → reverse → [3, 2]
    # LEVEL 2 (even): [4,5,6,7] → keep as [4, 5, 6, 7]
    #
    # ========================================================

    def zigzagLevelOrder(self, root):

        result = []

        if root is None:
            return result

        queue = deque([root])
        level_number = 0

        while len(queue) > 0:

            level_size = len(queue)
            current_level = []

            for i in range(level_size):

                node = queue.popleft()
                current_level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            # Odd level: reverse direction.
            if level_number % 2 == 1:
                current_level.reverse()

            result.append(current_level)
            level_number += 1

        return result


    # ========================================================
    # 21. LC #637 — AVERAGE OF LEVELS
    # ========================================================
    #
    # INPUT:
    #
    #               3
    #              / \
    #             9  20
    #               / \
    #              15   7
    #
    # OUTPUT:
    # [3.0, 14.5, 11.0]
    #
    # INTUITION:
    # Average = sum of level / number of nodes in level.
    #
    # STAGING:
    #
    # LEVEL 1: [3]       → avg = 3.0
    # LEVEL 2: [9, 20]   → avg = 29/2 = 14.5
    # LEVEL 3: [15, 7]   → avg = 22/2 = 11.0
    #
    # ========================================================

    def averageOfLevels(self, root):

        result = []

        if root is None:
            return result

        queue = deque([root])

        while len(queue) > 0:

            level_size = len(queue)
            level_sum = 0

            for i in range(level_size):

                node = queue.popleft()
                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result


    # ========================================================
    # 22. LC #104 — MAXIMUM DEPTH USING BFS
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
    # Count how many levels exist.
    # Each level = one more unit of depth.
    #
    # STAGING:
    #
    # LEVEL 1: process [1]    → depth = 1
    # LEVEL 2: process [2, 3] → depth = 2
    # LEVEL 3: process [4, 5] → depth = 3
    # queue empty → return 3
    #
    # ========================================================

    def maxDepth(self, root):

        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while len(queue) > 0:

            level_size = len(queue)
            depth += 1

            for i in range(level_size):

                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return depth


    # ========================================================
    # 23. LC #111 — MINIMUM DEPTH USING BFS
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
    # 1 → 3     = depth 2  (first leaf found)
    # 1 → 2 → 4 = depth 3
    #
    # OUTPUT:
    # 2
    #
    # INTUITION:
    # BFS naturally finds the shortest path first.
    # Stop as soon as the first leaf is reached.
    #
    # LOGIC:
    # A LEAF = node with no left and no right child.
    # First leaf encountered in BFS = minimum depth.
    #
    # STAGING:
    #
    # LEVEL 1: pop 1 → has children → depth = 1
    # LEVEL 2: pop 2 → has left child
    #          pop 3 → NO children → LEAF found → return 2
    #
    # TRANSITION:
    # Check each node when popped.
    # If it is a leaf, return current depth immediately.
    #
    # ========================================================

    def minDepth(self, root):

        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while len(queue) > 0:

            level_size = len(queue)
            depth += 1

            for i in range(level_size):

                node = queue.popleft()

                # STEP 1: Check if this is a leaf.
                if node.left is None and node.right is None:
                    return depth

                # STEP 2: Enqueue existing children.
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return depth


# ============================================================
# FAQ
# ============================================================
#
# Q: DFS vs BFS — when to use which?
#
#  DFS                       BFS
#  ===                       ===
#  Use recursion/stack        Use queue
#  Explores depth first       Explores level by level
#  Good for: path problems    Good for: shortest path,
#  height, subtree checks     level grouping, min depth
#
# ---
#
# Q: Why do we use a queue?
#
# Queue is FIFO. Nodes added earlier are processed earlier.
# This ensures we finish one level before starting the next.
#
# ---
#
# Q: Why capture len(queue) before each level?
#
# During the level loop we add new nodes to the queue.
# If we used len(queue) live it would include next-level nodes.
# Snapshotting the size first isolates exactly one level.
#
# ---
#
# Q: How to identify the last node of a level?
#
# Process i in range(level_size). When i == level_size - 1,
# the current node is the last node of this level.
#
# ---
#
# Q: Why does BFS find minimum depth naturally?
#
# BFS expands outward from root uniformly.
# The first leaf it reaches is guaranteed to be the closest.
# DFS might explore a deep branch before finding a shallower one.
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

    print("Level Order:", solution.levelOrder(root))
    # Expected: [[1], [2, 3], [4, 5, 6, 7]]

    print("Right Side View:", solution.rightSideView(root))
    # Expected: [1, 3, 7]

    print("Zigzag:", solution.zigzagLevelOrder(root))
    # Expected: [[1], [3, 2], [4, 5, 6, 7]]

    avg_root = TreeNode(3)
    avg_root.left = TreeNode(9)
    avg_root.right = TreeNode(20)
    avg_root.right.left = TreeNode(15)
    avg_root.right.right = TreeNode(7)

    print("Average of Levels:", solution.averageOfLevels(avg_root))
    # Expected: [3.0, 14.5, 11.0]

    print("Max Depth (BFS):", solution.maxDepth(root))
    # Expected: 3

    min_root = TreeNode(1)
    min_root.left = TreeNode(2)
    min_root.right = TreeNode(3)
    min_root.left.left = TreeNode(4)

    print("Min Depth (BFS):", solution.minDepth(min_root))
    # Expected: 2

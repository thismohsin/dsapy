# ============================================================
# P1 — TREE FUNDAMENTALS
# ============================================================
#
#  01. Tree Terminology
#  02. TreeNode Structure
#  03. Build a Binary Tree
#  04. Binary Tree vs BST
#  05. Height vs Depth
#  06. Tree Levels vs Edges
#  07. Maximum Nodes / Levels / Height Formulas
#  08. Full vs Complete vs Perfect vs Balanced
#  09. Recursive Thinking (Base / Recursive Case)
#  10. Recursion Call Stack
#
# ============================================================


# ============================================================
# 01. TREE TERMINOLOGY
# ============================================================
#
# INPUT:
#
#               1          <-- ROOT
#              / \
#             2   3        <-- CHILDREN of 1
#            / \
#           4   5          <-- LEAF nodes (no children)
#
# TERMS:
#
# ROOT    — Top node. No parent. Node 1.
# PARENT  — Node directly above. Node 2 is parent of 4 and 5.
# CHILD   — Node directly below. Node 4 is child of 2.
# LEAF    — Node with no children. Nodes 4, 5, 3.
# EDGE    — Connection between two nodes. 1-2 is an edge.
# SUBTREE — Any node and all its descendants. Node 2's subtree = {2, 4, 5}.
#
# ============================================================


# ============================================================
# 02. TREENODE STRUCTURE
# ============================================================
#
# INPUT:
# value = 5, left child = 3, right child = 7
#
# OUTPUT:
#
#     5
#    / \
#   3   7
#
# INTUITION:
# Each node holds a value and pointers to two children.
# A missing child is represented by None.
#
# LOGIC:
# node.val   = the value stored
# node.left  = left child node (or None)
# node.right = right child node (or None)
#
# ============================================================

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 03. BUILD A BINARY TREE
# ============================================================
#
# INPUT:
# Values: 1, 2, 3, 4, 5
#
# OUTPUT:
#
#               1
#              / \
#             2   3
#            / \
#           4   5
#
# INTUITION:
# Create each node manually and wire children by assignment.
#
# LOGIC:
# 1. Create each TreeNode.
# 2. Assign left and right children.
#
# ============================================================

def build_tree():

    root = TreeNode(1)

    root.left       = TreeNode(2)
    root.right      = TreeNode(3)

    root.left.left  = TreeNode(4)
    root.left.right = TreeNode(5)

    return root


# ============================================================
# 04. BINARY TREE vs BST
# ============================================================
#
# BINARY TREE:
#
#               5
#              / \
#             3   8
#            / \
#           9   1
#
# No ordering rule. Any value anywhere.
#
# ---
#
# BST (Binary Search Tree):
#
#               5
#              / \
#             3   8
#            / \   \
#           1   4   9
#
# RULE:
# LEFT child < PARENT < RIGHT child
# This holds for EVERY node in the tree.
#
# DIFFERENCE:
#
#  BINARY TREE          BST
#  ===========          ===
#  No ordering          LEFT < NODE < RIGHT
#  General structure    Enables O(log n) search
#
# ============================================================


# ============================================================
# 05. HEIGHT vs DEPTH
# ============================================================
#
# TREE:
#
#               1        <- DEPTH 0, HEIGHT 2
#              / \
#             2   3      <- DEPTH 1, HEIGHT 1
#            / \
#           4   5        <- DEPTH 2, HEIGHT 0
#
# DEPTH:
# Distance from ROOT to the node.
# Root has depth 0.
# Measured going DOWN from root.
#
# HEIGHT:
# Distance from the node to its DEEPEST LEAF.
# Leaf has height 0.
# Measured going UP from leaf.
#
# DIFFERENCE:
#
#  DEPTH                 HEIGHT
#  =====                 ======
#  Root → Node           Node → Leaf
#  Root = 0              Leaf = 0
#  Increases downward    Increases upward
#
# ============================================================


# ============================================================
# 06. TREE LEVELS vs EDGES
# ============================================================
#
# TREE:
#
#               1        <- LEVEL 1
#              / \
#             2   3      <- LEVEL 2
#            / \
#           4   5        <- LEVEL 3
#
# LEVELS:
# Count of rows in the tree.
# Root is at level 1.
#
# EDGES:
# Connections between nodes.
# A tree with N nodes has exactly N-1 edges.
#
# RELATIONSHIP:
#
# EDGES = LEVELS - 1
#
# 3 levels → 2 edge layers
#
# ============================================================


# ============================================================
# 07. MAXIMUM NODES / LEVELS / HEIGHT FORMULAS
# ============================================================
#
# TREE WITH HEIGHT h (number of levels):
#
# LEVEL 1 (root):  1  node  = 2^1 => 2^l1-1=1n node at level 1
# LEVEL 2:         2  nodes = 2^1 => 2^l2-1=3n node at level 2
# LEVEL 3:         4  nodes = 2^2 => 2^l3-1=7n node at level 3
# LEVEL h:         2^(h-1)  nodes level=l=height=h n=Node
#
# TOTAL NODES in a perfect tree of height h:
#
# TOTAL = 2^h - 1
#
# EXAMPLES:
#
# h = 1 → 1 node
# h = 2 → 3 nodes
# h = 3 → 7 nodes
# h = 4 → 15 nodes
#
# given level u know nodes required.
# for given nodes what will be height is given by formula
# MINIMUM HEIGHT for N nodes:
#
# MIN HEIGHT = floor(log2(N)) + 1
#
# ============================================================


# ============================================================
# 08. FULL vs COMPLETE vs PERFECT vs BALANCED
# ============================================================
#
# FULL BINARY TREE:
# Every node has 0 or 2 children. Never 1.
#
#               1
#              / \
#             2   3
#            / \
#           4   5
#
# Node 2 has 2 children. Node 3 has 0. Valid full tree.
#
# ---
#
# COMPLETE BINARY TREE:
# All levels filled left to right.
# Last level filled from left.
#
#               1
#              / \
#             2   3
#            / \  /
#           4   5 6
#
# ---
#
# PERFECT BINARY TREE:
# All levels completely filled.
# All leaves at same depth.
#
#               1
#              / \
#             2   3
#            / \ / \
#           4  5 6  7
#
# ---
#
# BALANCED BINARY TREE:
# Height difference between left and right subtrees <= 1
# for every node.
#
# COMPARISON:
#
#  TYPE       RULE
#  ====       ====
#  Full       0 or 2 children per node
#  Complete   Fill left to right each level
#  Perfect    All levels full, all leaves same depth
#  Balanced   |left height - right height| <= 1
#
# ============================================================


# ============================================================
# 09. RECURSIVE THINKING
# ============================================================
#
# PROBLEM:
# Count nodes in a tree.
#
# INPUT:
#
#               1
#              / \
#             2   3
#
# OUTPUT:
# 3
#
# INTUITION:
# The count of nodes at any node equals:
# 1 (current) + count(left) + count(right)
#
# LOGIC:
#
# BASE CASE:     node is None → return 0
# RECURSIVE CASE: 1 + count(left) + count(right)
#
# STAGING:
#
# STEP 1: count(None) = 0
# STEP 2: count(2)    = 1 + count(None) + count(None) = 1
# STEP 3: count(3)    = 1
# STEP 4: count(1)    = 1 + 1 + 1 = 3
#
# ============================================================

def count_nodes(root):

    # BASE CASE:
    if root is None:
        return 0

    # STEP 1: Count left subtree.
    left_count = count_nodes(root.left)

    # STEP 2: Count right subtree.
    right_count = count_nodes(root.right)

    # STEP 3: Add current node.
    return 1 + left_count + right_count


# ============================================================
# 10. RECURSION CALL STACK
# ============================================================
#
# PROBLEM:
# Trace the call stack for count_nodes on:
#
#               1
#              / \
#             2   3
#
# CALL STACK (growing downward):
#
# count_nodes(1)
#   count_nodes(2)
#     count_nodes(None) → 0
#     count_nodes(None) → 0
#   returns 1
#   count_nodes(3)
#     count_nodes(None) → 0
#     count_nodes(None) → 0
#   returns 1
# returns 1 + 1 + 1 = 3
#
# KEY POINTS:
#
# 1. Each call waits for its children to return.
# 2. Returns bubble up from leaf to root.
# 3. BASE CASE stops the recursion.
# 4. Stack depth = height of tree.
#
# ============================================================


# ============================================================
# FAQ
# ============================================================
#
# Q: What is root, parent, child and leaf?
#
# ROOT   = top node, no parent
# PARENT = node directly above another
# CHILD  = node directly below another
# LEAF   = node with no children
#
# ---
#
# Q: Height vs depth — what is the difference?
#
# DEPTH  = distance from root DOWN to the node
# HEIGHT = distance from node UP to its deepest leaf
#
# ---
#
# Q: How many nodes can a binary tree have?
#
# Perfect tree of height h → 2^h - 1 nodes
# Minimum: h nodes (skewed tree, one child per node)
#
# ---
#
# Q: What is a full vs complete vs perfect tree?
#
# FULL     = every node has 0 or 2 children
# COMPLETE = filled left-to-right, last level may be partial
# PERFECT  = all levels fully filled
#
# ---
#
# Q: What makes a tree balanced?
#
# abs(left_height - right_height) <= 1 at every node
#
# ---
#
# Q: What is the base case in recursion?
#
# The condition that stops the recursion.
# For trees: node is None → return 0 or None or False
#
# ============================================================


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    root = build_tree()

    print("Node count:", count_nodes(root))
    # Expected: 5

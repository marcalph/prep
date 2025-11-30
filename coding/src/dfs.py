"""
useful if 
    Tree data structure
    Balanced/low branching factor
    Hierarchical structures
    Solution near the leaves
    Traversal along paths
    Explore all possible paths
"""

# examples
# Find products in a price range: convert prices in BST then variation of preorder traversal
# Dependency resolution: In the dependency graph as DFS traverses the graph, it naturally produces a topological ordering of the nodes.
# Syntax tree analysis: In compilers and interpreters, source code is typically represented as syntax trees. dfs can be used to perform tasks code generation, optimization, or static analysis


def binary_tree_diameter(root):
    def dfs(node):
        if not node:
            return 0, 0
        left_height, left_diameter = dfs(node.left)
        right_height, right_diameter = dfs(node.right)
        return 1 + max(left_height, right_height), max(
            left_height + right_height, left_diameter, right_diameter
        )

    return dfs(root)[1]

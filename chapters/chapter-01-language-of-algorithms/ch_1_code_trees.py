from collections import deque
from typing import Any


class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def tree_bfs(root: TreeNode | None) -> list[Any]:
    """Return the tree's values in breadth-first (level) order."""
    if root is None:
        return []

    queue = deque([root])
    traversal_output = []

    while queue:
        current_node = queue.popleft()
        traversal_output.append(current_node.value)

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

    return traversal_output


def tree_dfs(root: TreeNode | None) -> list[Any]:
    """Return the tree's values in preorder depth-first order."""
    if root is None:
        return []

    stack = [root]
    traversal_output = []

    while stack:
        current_node = stack.pop()
        traversal_output.append(current_node.value)

        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)

    return traversal_output


def main() -> None:
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")
    root.right.right = TreeNode("F")

    print("Breadth-first traversal:", tree_bfs(root))
    print("Depth-first traversal:", tree_dfs(root))


if __name__ == "__main__":
    main()

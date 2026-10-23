from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_bfs(root):
    """Return node values in breadth-first (level-order) traversal order."""
    if not root:
        return []

    queue = deque([root])
    traversal_output = []

    while queue:
        current_node = queue.popleft()
        traversal_output.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return traversal_output


def tree_dfs(root):
    """Return node values in iterative preorder depth-first order."""
    if not root:
        return []

    stack = [root]
    traversal_output = []

    while stack:
        current_node = stack.pop()
        traversal_output.append(current_node.value)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return traversal_output


def main():
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")

    print("Breadth-first:", tree_bfs(root))
    print("Depth-first:", tree_dfs(root))


if __name__ == "__main__":
    main()

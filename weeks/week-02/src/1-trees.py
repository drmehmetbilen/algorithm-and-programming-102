from collections import deque


class TreeNode:
    """Node for a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Simple binary tree implementation for traversal practice."""

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        """Return True if tree has no nodes."""
        return self.root is None

    def find(self, target):
        """Return True if target exists in the tree (BFS)."""
        if self.is_empty():
            return False

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.value == target:
                return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return False

    def size(self):
        """Return total number of nodes."""

        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    def height(self):
        """Return tree height using node-count definition (empty tree is 0)."""

        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def preorder(self):
        """Return preorder traversal list: root, left, right."""
        result = []

        def _preorder(node):
            if node is None:
                return
            result.append(node.value)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        return result

    def inorder(self):
        """Return inorder traversal list: left, root, right."""
        result = []

        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            result.append(node.value)
            _inorder(node.right)

        _inorder(self.root)
        return result

    def postorder(self):
        """Return postorder traversal list: left, right, root."""
        result = []

        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.value)

        _postorder(self.root)
        return result

    def level_order(self):
        """Return level-order traversal list using a queue."""
        if self.is_empty():
            return []

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return result


def build_sample_tree():
    """Create a small sample tree for class demo."""
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")
    root.right.right = TreeNode("F")
    return BinaryTree(root)


if __name__ == "__main__":
    tree = build_sample_tree()

    print("Preorder:", tree.preorder())
    print("Inorder:", tree.inorder())
    print("Postorder:", tree.postorder())
    print("Level-order:", tree.level_order())
    print("Size:", tree.size())
    print("Height:", tree.height())
    print("Find 'E':", tree.find("E"))
    print("Find 'Z':", tree.find("Z"))

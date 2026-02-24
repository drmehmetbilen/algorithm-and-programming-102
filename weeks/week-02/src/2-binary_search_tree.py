from collections import deque


class BSTNode:
    """Node for Binary Search Tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with insert, search, and delete."""

    def __init__(self):
        self.root = None

    def is_empty(self):
        """Return True if BST has no nodes."""
        return self.root is None

    def insert(self, key):
        """
        Insert key into BST.
        Returns True if inserted, False if key already exists.
        """
        if self.root is None:
            self.root = BSTNode(key)
            return True

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = BSTNode(key)
                    return True
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = BSTNode(key)
                    return True
                current = current.right
            else:
                return False

    def search(self, key):
        """Return True if key exists, otherwise False."""
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def find_min(self):
        """Return minimum key, or None if BST is empty."""
        node = self._min_node(self.root)
        return None if node is None else node.key

    def find_max(self):
        """Return maximum key, or None if BST is empty."""
        current = self.root
        if current is None:
            return None

        while current.right is not None:
            current = current.right
        return current.key

    def delete(self, key):
        """
        Delete key from BST.
        Returns True if deleted, False if key not found.
        """
        self.root, deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        if node is None:
            return None, False

        if key < node.key:
            node.left, deleted = self._delete(node.left, key)
            return node, deleted

        if key > node.key:
            node.right, deleted = self._delete(node.right, key)
            return node, deleted

        if node.left is None and node.right is None:
            return None, True

        if node.left is None:
            return node.right, True

        if node.right is None:
            return node.left, True

        successor = self._min_node(node.right)
        node.key = successor.key
        node.right, _ = self._delete(node.right, successor.key)
        return node, True

    def _min_node(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Return inorder traversal list (sorted for BST)."""
        result = []

        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            result.append(node.key)
            _inorder(node.right)

        _inorder(self.root)
        return result

    def preorder(self):
        """Return preorder traversal list."""
        result = []

        def _preorder(node):
            if node is None:
                return
            result.append(node.key)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        return result

    def postorder(self):
        """Return postorder traversal list."""
        result = []

        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.key)

        _postorder(self.root)
        return result

    def level_order(self):
        """Return level-order traversal list."""
        if self.root is None:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return result

    def height(self):
        """Return height using node-count definition (empty tree is 0)."""

        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)


if __name__ == "__main__":
    bst = BinarySearchTree()
    sample_values = [50, 30, 70, 20, 40, 60, 80]

    for value in sample_values:
        bst.insert(value)

    print("Inorder (sorted):", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())
    print("Level-order:", bst.level_order())
    print("Height:", bst.height())
    print("Min:", bst.find_min())
    print("Max:", bst.find_max())

    print("Search 60:", bst.search(60))
    print("Search 99:", bst.search(99))

    print("Delete 20 (leaf):", bst.delete(20))
    print("Delete 30 (one child):", bst.delete(30))
    print("Delete 50 (two children):", bst.delete(50))
    print("Inorder after deletes:", bst.inorder())

# Binary Search Tree is a data structure where each node has at most
# two children and follows this rule:
#   - The left child's value must be less than the parent's value.
#   - The right child's value must be greater than the parent's value.
#
# Thanks to this rule, search, insertion and deletion operations are much faster.
#
# Operations:
#   - add_node    : Insert a new node
#   - search_value: Search for a value
#   - size        : Total number of nodes in the tree
#   - height      : Height (depth) of the tree
#   - delete_node : Delete a node
# ============================================================


class Node():
    """
    Class representing each individual node in the BST.

    Attributes:
        text  (str)  : Text data carried by the node.
        value (int)  : Numeric value that determines the node's position in the tree.
        left  (Node) : Left child node (holds a smaller value).
        right (Node) : Right child node (holds a larger value).
    """

    def __init__(self, text: str, value: int):
        """
        Initializes the Node object.

        Arguments:
            text  (str) : Text data to assign to the node.
            value (int) : Numeric value to assign to the node.

        Possible Errors:
            TypeError : Raises an error if text is not str or value is not int.
        """
        if not isinstance(text, str):
            raise TypeError(f"text parametresi(ilk parametre) string olmalıdır.")
        if not isinstance(value, (int, float)):
            raise TypeError(f"'value' parametresi(ikinci parametre) sayısal olmalıdır.")

        self.value = value   # int  — Numeric key that determines position in the tree
        self.text  = text    # str  — Text/name data carried by the node
        self.left  = None    # Node — Left child (empty at start)
        self.right = None    # Node — Right child (empty at start)


class BinaryTree():
    """
    Class representing the Binary Search Tree structure.

    BST rule: All values in the left subtree of any node must be
    smaller than that node, and all values in the right subtree must be larger.

 *                        ┌─────┐
 *                        │  50 │          ← ROOT
 *                        └──┬──┘
 *               ┌───────────┴───────────┐
 *            ┌──┴──┐               ┌────┴──┐
 *            │  30 │               │  70   │
 *            └──┬──┘               └───┬───┘
 *          ┌────┴────┐          ┌──────┴─────┐
 *       ┌──┴──┐   ┌──┴──┐    ┌──┴──┐      ┌──┴──┐
 *       │  20 │   │  40 │    │  60 │      │  80 │
 *       └──┬──┘   └─────┘    └─────┘      └──┬──┘
 *       ┌──┴──┐                           ┌──┴──┐
 *       │  10 │                           │  90 │
 *       └─────┘                           └─────┘


    Attributes:
        root (Node): The root (top) node of the tree.
    """

    def __init__(self, text: str, value: int):
        """
        Initializes the tree with a root node.

        Arguments:
            text  (str) : Text data for the root node.
            value (int) : Numeric value for the root node.

        Possible Errors:
            TypeError: Raises an error if an invalid parameter type is given.

        Example:
            >>> tree = BinaryTree("Root", 50)
        """
        self.root = Node(text, value)   # Node — The starting point of the entire tree

    # ----------------------------------------------------------
    # INSERTION (ADD NODE)
    # ----------------------------------------------------------

    def add_node(self, text: str, value: int) -> None:
        """
        Adds a new node to the tree.

        According to BST rules:
          - If the new value is greater than the current node  → go right
          - If the new value is less than the current node     → go left
          - Once an empty spot is found (no node to go to), place the node there.

        Arguments:
            text  (str) : Text data for the new node.
            value (int) : Numeric value for the new node.

        Possible Errors:
            TypeError : Raises an error if an invalid parameter type is given.
            ValueError: Raises an error if the same value already exists.

        Example:
            >>> tree.add_node("Ankara", 20)
        """
        new_node     = Node(text, value)   # Node — The new node created to be inserted
        current_node = self.root           # Node — Starting point for traversal (root)

        while True:
            if value > current_node.value:
                # New value is larger → look at the right side
                if current_node.right is None:
                    current_node.right = new_node  # Empty spot found - insert
                    break
                else:
                    current_node = current_node.right  # Not empty, keep going
            elif value < current_node.value:
                # New value is smaller → look at the left side
                if current_node.left is None:
                    current_node.left = new_node   # Empty spot found - insert
                    break
                else:
                    current_node = current_node.left   # Not empty, keep going
            else:
                # A BST cannot have two nodes with the same value!
                raise ValueError(f"HATA: {value} değeri zaten mevcut! BST'de tekrar eden değer eklenemez.")

    # ----------------------------------------------------------
    # SEARCH (SEARCH VALUE)
    # ----------------------------------------------------------

    def search_value(self, value: int) -> str:
        """
        Searches for the node with the given numeric value and returns its text data.

        Thanks to the BST structure, the search area is halved at every step.
        This is much faster than a direct linear search.

        Arguments:
            value (int): The numeric value to search for.

        Return Value:
            str: The text data of the found node.

        Possible Errors:
            TypeError : Raises an error if value is not numeric.
            KeyError  : Raises an error if the value is not found in the tree.

        Example:
            >>> tree.search_value(20)
            'Ankara'
        """
        if not isinstance(value, int):
            raise TypeError(f"'value' sayısal değer olmalıdır.")

        current_node = self.root   # Node — The node where the search begins

        while current_node is not None:
            if current_node.value == value:
                return current_node.text           # Found!
            elif value < current_node.value:
                current_node = current_node.left   # Value is smaller than node's value → go left
            else:
                current_node = current_node.right  # Value is larger than node's value → go right

        # Loop ended but value was not found
        raise KeyError(f"HATA: {value} değeri ağaçta bulunamadı.")

    # ----------------------------------------------------------
    # SIZE
    # ----------------------------------------------------------

    def size(self) -> int:
        """
        Returns the total number of nodes in the tree.

        Counts all nodes recursively.

        Return Value:
            int: Total number of nodes.

        Example:
            >>> tree.size()
            7
        """
        return self._size(self.root)

    def _size(self, current_node: 'Node') -> int:
        """
        Recursive helper method — called by size().

        Arguments:
            current_node (Node): The node being processed.

        Return Value:
            int: The count of this node and all nodes below it.
        """
        if current_node is None:
            return 0
        # This node (1) + left subtree size + right subtree size
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    #      A
    #     / \
    #    B   C
    #   / \
    #  D   E

    # Step 1 — _size(A) is called:
    # "How many nodes are under A?"
    # = 1 (itself) + _size(B) + _size(C)

    # Step 2 — _size(B) is called:
    # "How many nodes are under B?"
    # = 1 (itself) + _size(D) + _size(E)

    # Step 3 — _size(D) is called:
    # "How many nodes are under D?"
    # = 1 (itself) + _size(None) + _size(None)
    #                   ↓                ↓
    #                   0                0
    # = 1 + 0 + 0 = 1  ✅

    # Step 4 — _size(E) is called:
    # "How many nodes are under E?"
    # = 1 (itself) + _size(None) + _size(None)
    #                   ↓                ↓
    #                   0                0
    # = 1 + 0 + 0 = 1  ✅

    # Step 5 — Now we can calculate B's result:
    # _size(B) = 1 (itself) + _size(D) + _size(E)
    #         =      1      +     1    +     1
    #         = 3  ✅

    # Step 6 — _size(C) is called:
    # "How many nodes are under C?"
    # = 1 (itself) + _size(None) + _size(None)
    #                   ↓                ↓
    #                   0                0
    # = 1 + 0 + 0 = 1  ✅

    # Step 7 — Now we can calculate A's result:
    # _size(A) = 1 (itself) + _size(B) + _size(C)
    #         =      1      +     3    +     1
    #         = 5  ✅

    # The function first goes all the way down, then adds up on the way back.



    # ----------------------------------------------------------
    # HEIGHT
    # ----------------------------------------------------------

    def height(self) -> int:
        """
        Returns the height (depth) of the tree.

        Height: The number of nodes from the root to the deepest leaf.
        A tree with a single node has a height of 1.
        Core logic:
        "Me (1) + how tall is my left arm, how tall is my right arm → take the taller one"

        Return Value:
            int: The height of the tree.

        Example:
            >>> tree.height()
            5
        """
        return self._height(self.root)

    def _height(self, current_node: 'Node') -> int:
        """
        Recursive helper method — called by height().

        Arguments:
            current_node (Node): The node being processed.

        Return Value:
            int: The length of the longest path below this node.
        """
        if current_node is None:
            return 0
        # The larger of left and right subtree heights + this node
        return 1 + max(self._height(current_node.left), self._height(current_node.right))

    # size and height work similarly but calculate different things.
    # In height calculation, each node counts as 1 and the subtree heights
    # are compared to select the longest one.
    #      A
    #     / \
    #    B   C
    #   / \
    #  D   E
    # For example, _height(A) is called and calculates 1 (me) + max(_height(B), _height(C)).
    # The logic is the same as size — whichever of _height(B) or _height(C) is larger
    # gets selected, 1 is added, and the result is the height of the tree.


    # ----------------------------------------------------------
    # DELETION (DELETE NODE)
    # ----------------------------------------------------------

    def delete_node(self, value: int) -> None:
        """
        Deletes the node with the given value while preserving the nodes below it.

        The deletion is performed in 4 steps:
          1. Find the node to delete and its parent
          2. Collect the children of the node to delete into a list
          3. Cut the parent's connection
          4. Re-insert the collected nodes

        Arguments:
            value (int): The numeric value of the node to delete.

        Possible Errors:
            TypeError : Raises an error if value is not numeric.
            KeyError  : Raises an error if the value is not found in the tree.
            ValueError: Raises an error if attempting to delete the root node.

        Example:
            >>> tree.delete_node(9)   # 9 is deleted, nodes below are preserved
        """
        if not isinstance(value, (int, float)):
            raise TypeError("'value' int veya float olmalıdır.")
        if self.root is None:
            raise KeyError("HATA: Ağaç boş.")
        if self.root.value == value:
            raise ValueError("HATA: Kök düğüm silinemez.")

        # Step 1 — Find the node to delete and its parent
        # We track the parent because there is no upward link inside Node.
        # When the loop ends, we have both current (to delete) and parent (its parent).
        parent  = None      # Node — One level above the node to delete
        current = self.root # Node — As always, we start from the root.

        while current is not None:
            if value == current.value:
                break                      # Found!
            parent = current               # Stay one step behind
            if value < current.value:
                current = current.left     # Smaller → go left
            else:
                current = current.right    # Larger → go right

        if current is None:
            raise KeyError(f"HATA: {value} değeri ağaçta bulunamadı.")

        # Step 2 — Collect the children of the node to delete into a list
        # We collect current's children, not current itself,
        # because current is being deleted and doesn't need to be re-added.
        collected = []                                   # list — will hold (text, value) tuples
        self._collect_nodes(current.left,  collected)   # Collect left subtree
        self._collect_nodes(current.right, collected)   # Collect right subtree

        # Step 3 — Cut the parent's connection
        # We check whether current is the left or right child of parent.
        # Setting the correct side to None detaches the node from the tree.
        # Python automatically cleans up the freed memory.
        if parent.left == current:
            parent.left  = None   # current was left child → cut left connection
        else:
            parent.right = None   # current was right child → cut right connection

        # Step 4 — Re-insert the collected nodes
        # add_node places them according to BST rules.
        # Since we collected top-to-bottom, the parent is always inserted before
        # its children, so the tree structure stays intact.
        for text, val in collected:
            self.add_node(text, val)


    def _collect_nodes(self, node: 'Node', result: list) -> None:
        """
        Collects the entire subtree starting from the given node into a list.

        Collects top-to-bottom (parent first, children after).
        This order matters: when re-inserting with add_node, the parent
        must always be added before its children to preserve BST structure.

        Arguments:
            node   (Node) : The node where collection begins.
            result (list) : The list where (text, value) tuples are appended.

        Example:
            Input tree:
                  15
                 /
                11
            Output: [("Burdur", 15), ("Bilecik", 11)]
        """
        if node is None:
            return
        result.append((node.text, node.value))    # Itself first
        self._collect_nodes(node.left,  result)   # Then left child
        self._collect_nodes(node.right, result)   # Then right child


# ==============================================================
# MAIN PROGRAM — Test and Usage Example
# ==============================================================

if __name__ == "__main__":

    # Tree is created (root node: Mehmet, 32)
    my_tree = BinaryTree("Mehmet", 32)

    # Nodes are added
    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)

    # Search test
    print(f"41 değerindeki düğüm : {my_tree.search_value(41)}")   # Ata
    print(f"9  değerindeki düğüm : {my_tree.search_value(9)}")    # Sabriye

    # Size and height
    print(f"\nAğaç boyutu    : {my_tree.size()}")     # 7
    print(f"Ağaç yüksekliği: {my_tree.height()}")    # 5

    # Deletion test
    print(f"Silmeden önce boyut: {my_tree.size()}")

    my_tree.delete_node(15)   # Leaf node (Burdur)
    print(f"15 (Burdur) silindi → boyut: {my_tree.size()}")

    my_tree.delete_node(9)    # Node with two children (Sabriye)
    print(f"9  (Sabriye) silindi → boyut: {my_tree.size()}")

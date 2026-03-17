# Binary Search Tree: each node has at most two children.
#   - Left child value  < parent value
#   - Right child value > parent value
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
    Represents a single node in the BST.

    Attributes:
        text  (str)  : Text data carried by the node.
        value (int)  : Numeric value that determines the node's position.
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
            TypeError : Raises an error if text is not str or value is not numeric.
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
    Represents the Binary Search Tree structure.

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
        self.root = Node(text, value)

    # ----------------------------------------------------------
    # INSERTION (ADD NODE)
    # ----------------------------------------------------------

    def add_node(self, text: str, value: int) -> None:
        """
        Adds a new node to the tree following BST rules.

        Arguments:
            text  (str) : Text data for the new node.
            value (int) : Numeric value for the new node.

        Possible Errors:
            TypeError : Raises an error if an invalid parameter type is given.
            ValueError: Raises an error if the same value already exists.

        Example:
            >>> tree.add_node("Ankara", 20)
        """
        new_node     = Node(text, value)
        current_node = self.root

        while True:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                raise ValueError(f"HATA: {value} değeri zaten mevcut! BST'de tekrar eden değer eklenemez.")

    # ----------------------------------------------------------
    # SEARCH (SEARCH VALUE)
    # ----------------------------------------------------------

    def search_value(self, value: int) -> str:
        """
        Searches for the node with the given value and returns its text data.

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

        current_node = self.root

        while current_node is not None:
            if current_node.value == value:
                return current_node.text
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        raise KeyError(f"HATA: {value} değeri ağaçta bulunamadı.")

    # ----------------------------------------------------------
    # SIZE
    # ----------------------------------------------------------

    def size(self) -> int:
        """
        Returns the total number of nodes in the tree.

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
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    # ----------------------------------------------------------
    # HEIGHT
    # ----------------------------------------------------------

    def height(self) -> int:
        """
        Returns the height (depth) of the tree.

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
        return 1 + max(self._height(current_node.left), self._height(current_node.right))

    # ----------------------------------------------------------
    # DELETION (DELETE NODE)
    # ----------------------------------------------------------

    def delete_node(self, value: int) -> None:
        """
        Deletes the node with the given value while preserving the nodes below it.

        Arguments:
            value (int): The numeric value of the node to delete.

        Possible Errors:
            TypeError : Raises an error if value is not numeric.
            KeyError  : Raises an error if the value is not found in the tree.
            ValueError: Raises an error if attempting to delete the root node.

        Example:
            >>> tree.delete_node(9)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("'value' int veya float olmalıdır.")
        if self.root is None:
            raise KeyError("HATA: Ağaç boş.")
        if self.root.value == value:
            raise ValueError("HATA: Kök düğüm silinemez.")

        parent  = None
        current = self.root

        while current is not None:
            if value == current.value:
                break
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            raise KeyError(f"HATA: {value} değeri ağaçta bulunamadı.")

        collected = []
        self._collect_nodes(current.left,  collected)
        self._collect_nodes(current.right, collected)

        if parent.left == current:
            parent.left  = None
        else:
            parent.right = None

        for text, val in collected:
            self.add_node(text, val)

    def _collect_nodes(self, node: 'Node', result: list) -> None:
        """
        Collects the entire subtree starting from the given node into a list.
        Collects top-to-bottom so that parents are always re-inserted before children.

        Arguments:
            node   (Node) : The node where collection begins.
            result (list) : The list where (text, value) tuples are appended.
        """
        if node is None:
            return
        result.append((node.text, node.value))
        self._collect_nodes(node.left,  result)
        self._collect_nodes(node.right, result)


# ==============================================================
# MAIN PROGRAM — Test and Usage Example
# ==============================================================

if __name__ == "__main__":

    my_tree = BinaryTree("Mehmet", 32)

    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)

    print(f"41 değerindeki düğüm : {my_tree.search_value(41)}")
    print(f"9  değerindeki düğüm : {my_tree.search_value(9)}")

    print(f"\nAğaç boyutu    : {my_tree.size()}")
    print(f"Ağaç yüksekliği: {my_tree.height()}")

    print(f"Silmeden önce boyut: {my_tree.size()}")

    my_tree.delete_node(15)
    print(f"15 (Burdur) silindi → boyut: {my_tree.size()}")

    my_tree.delete_node(9)
    print(f"9  (Sabriye) silindi → boyut: {my_tree.size()}")

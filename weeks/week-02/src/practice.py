class Node():
    def __init__(self, text: str, value: int):
        self.value: int = value
        self.text: str = text
        self.left: 'Node' = None
        self.right: 'Node' = None

class BinaryTree():
    def __init__(self, text: str, value: int):
        self.root = Node(text, value)
          
    def add_node(self, text: str, value: int):
        new_node = Node(text, value)
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
                print("ERROR : Value already exists!!")
                break

    def search_value(self, value: int) -> str:
        current_node = self.root
        while True:
            if current_node.value == value:
                return current_node.text
            if value < current_node.value:
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    return "ERROR : Not found"
                current_node = current_node.right

    def size(self) -> int:
        return self._size(self.root)
        
    def _size(self, current_node: 'Node') -> int:
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, current_node: 'Node') -> int:
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left), self._height(current_node.right))

    def delete_node(self, value: int):
        self.root = self._delete(self.root, value)

    def _delete(self, current: 'Node', value: int) -> 'Node':
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete(current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            
            temp = self._min_value(current.right)
            current.value = temp.value
            current.text = temp.text
            current.right = self._delete(current.right, temp.value)
        
        return current

    def _min_value(self, node: 'Node') -> 'Node':
        current = node
        while current.left is not None:
            current = current.left
        return current

if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet", 32)
    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)

    print(f"41 araniyor: {my_tree.search_value(41)}")
    print(f"Boyut: {my_tree.size()}")
    print(f"Yukseklik: {my_tree.height()}")
    
    my_tree.delete_node(31)
    print(f"31 silindikten sonra boyut: {my_tree.size()}")

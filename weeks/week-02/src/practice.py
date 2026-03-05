# Binary Search Tree
# Node and Tree Class 
# Add New Node
# Find Value
# Size
# Height
# Delete 

class Node():
    def __init__(self, text, value):
        # text: str, key of node
        self.text = text
        # value: int,  position in tree
        self.value = value
        # left child 
        self.left = None
        # right child 
        self.right = None

class BinaryTree():
    # init tree with root node
    def __init__(self, text: str, value: int):
        # text: str, key of root
        # value: int, value of root
        self.root = Node(text, value)
          
    # add new node to tree
    def add_node(self, text: str, value: int):
        
        new_node = Node(text, value)
        current_node = self.root
        while True:
            if value > current_node.value:
                #  right
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            elif value < current_node.value:
                #  left
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                # value already exists
                print("ERROR: Value is already exist!!")
                break

    # find value
    def search_value(self, value: int):
        
        current_node = self.root
        while True:
            if current_node.value == value:
                return current_node.text
            if value < current_node.value:
                if current_node.left is None:
                    return "ERROR: Not found."
                current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    return "ERROR: Not found"
                current_node = current_node.right

    # size
    def size(self):
        return self._size(self.root)
        
    
    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    # height 
    def height(self):
        return self._height(self.root)

    
    def _height(self, current_node):
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left), self._height(current_node.right))
    



    
# Delete 

def delete(self, value: int):
    # value: int, node to remove
    current_node = self.root  
    parent = None             

    # find the node to delete
    while current_node:
        if value < current_node.value:
            parent = current_node
            current_node = current_node.left
        elif value > current_node.value:
            parent = current_node
            current_node = current_node.right
        else:
            # found
            break

    if current_node is None:
        # value not found
        return

    #  0 children "leaf" 
    if current_node.left is None and current_node.right is None:
        if parent is None:
            # tree has only root
            self.root = None
        elif parent.left == current_node:
            parent.left = None
        else:
            parent.right = None

    #  1 child
    elif current_node.left is None or current_node.right is None:
        # get the child node
        child = current_node.left if current_node.left else current_node.right
        if parent is None:
            # deleting root with 1 child
            self.root = child
        elif parent.left == current_node:
            parent.left = child
        else:
            parent.right = child

    #  2 children
    else:
        # find smallest node in right subtree
        successor_parent = current_node
        successor = current_node.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # copy successor's key and value to current node
        current_node.text = successor.text
        current_node.value = successor.value

        # remove successor node
        if successor.right:
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        else:
            if successor_parent.left == successor:
                successor_parent.left = None
            else:
                successor_parent.right = None


if __name__ == "__main__":
    # create tree and add nodes
    my_tree = BinaryTree("Mehmet", 32)
    my_tree.add_node("Sabriye", 9)
    my_tree.add_node("Emirhan", 31)
    my_tree.add_node("Ata", 41)
    my_tree.add_node("Burdur", 15)
    my_tree.add_node("Konya", 42)
    my_tree.add_node("Bilecik", 11)

    
    print(my_tree.search_value(41))   #  print Ata
    print(my_tree.search_value(82))   # not found
    
    print(my_tree.size())              # total nodes
    print(my_tree.height())            # height of tree

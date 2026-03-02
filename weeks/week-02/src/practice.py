
# Binary Search Tree
# Node and Tree Class Definitations
# Add New Node
# Find Value
# Size
# Height
# Delete ?

class Node():
    """Nodes for Binary Search Tree

    text: This parameter will be used as a key

    value: This parameter will be used as a position of the Node"""
    def __init__(self, text : str, value : int):
        self.value = value 
        self.text = text
        self.left = None
        self.right = None

    #Getter/Setter
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        if type(value) is not int:
            raise TypeError("Error: Value must be intiger")
        else: self.__value = value

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self,text):
        if type(text) is not str:
            raise TypeError("Error: Text must be string")
        else: self.__text = text

class BinaryTree():
    def __init__(self,text:str,value:int):
        """
        Uses text and value to construct binary tree

        text: this parameter will be used as a key

        value: this parameter will be used as a position of the Node
        """
        self.root = Node(text,value)
          
    def add_node(self,text: str,value: int):
        """Insert a Node which used as a BST. 
        If a node can move to the right or left of the main root, it will; otherwise, it will be added there.

        text: this parameter will be used as a key

        value: this parameter will be used as a position of the Node
        """
        new_node = Node(text,value)
        current_node = self.root
        while True:
            if value>current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            elif value<current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                print("ERRROR : Value is already exist!!")
                break

    def search_value(self,value: int):
        """Searches for a node in BST and returns an error if none exists.
        It will return an error if the value is less than or greater than the leaf value.
        If it is equal to the node, it will return the node's text.

        value: This parameter is used to find the text of the Node inside the BST.
        """
        current_node = self.root
        while True:
            if current_node.value == value:
                return current_node.text
            if value<current_node.value:
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            elif value>current_node.value:
                if current_node.right is None:
                    return "ERROR : Not found"
                current_node = current_node.right

    def size(self):
        """Executes the _size() method without taking any parameters."""
        return self._size(self.root)
        
    def _size(self, current_node):
        """Count each node starting from the root.

        current_node: Must be a Node"""
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self):
        """Executes the _height() method without taking any parameters."""
        return self._height(self.root)
    def _height(self, current_node):
        """By examining all the branches, it finds the longest one.
        
        current_node: Must be a Node"""
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left),self._height(current_node.right))

    def delete(self, value: int):
        """The method the user will use

        value: The node values ​​you want to delete"""
        self.root = self._delete(self.root, value)

    def _delete(self , currentNode, value: int):
        """This method deletes the node that is requested to be removed from the BST."""
        if currentNode is None:
            return currentNode
        if value < currentNode.value:
            currentNode.left = self._delete(currentNode.left,value)
        elif value > currentNode.value:
            currentNode.right = self._delete(currentNode.right,value)
        else:
            if currentNode.left is None:
                return currentNode.right
            elif currentNode.right is None:
                return currentNode.left
            
            minNode = self.findMinValue(currentNode.right)
            currentNode.value = minNode.value
            currentNode.text = minNode.text

            currentNode.right = self._delete(currentNode.right, minNode.value)
        return currentNode

    def findMinValue(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode
    
if __name__ == "__main__":
    my_tree = BinaryTree("Mehmet",32)
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Emirhan",31)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Burdur",15)
    my_tree.add_node("Konya",42)
    my_tree.add_node("Bilecik",11)

    # print(my_tree.search_value(41))
    # print(my_tree.search_value(82))
    # print(my_tree.size())
    # print(my_tree.height())

    print(my_tree.size())
    print(my_tree.delete(15))
    print(my_tree.size())
    print(my_tree.search_value(15))
    print(my_tree.delete(61))
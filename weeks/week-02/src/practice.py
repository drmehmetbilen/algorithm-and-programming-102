
# Binary Search Tree
# Node and Tree Class Definitations
# Add New Node
# Find Value
# Size
# Height
# Delete ?

class Node():
    def __init__(self, text, value):
        self.__value= value
        self.__text= text
        self.left = None
        self.right = None


#Encapsulatıon was used to ensure the security of the information
#Getter methods------------

    def get_text(self):
        return self.__text
    
    def get_value(self):
        return self.__value
    
#Setter methods------------

    def update_data(self,text,value):
        if not isinstance(text,str):
            raise IndexError("Text must be string.")
        self.__text = text

        if not isinstance(value,int):
            raise IndexError("Value must be integer.")
        self.value = value




class BinaryTree():
    def __init__(self,text:str,value:int):
        """
        This methods uses text and value to construct binary tree
        text: this parameter will be used as a key
        value: this parameter will be used as a position of the Node
        """
        self.root = Node(text,value)
          
    def add_node(self,text,value):
        """
        Insert a new node to binary search tree.(Nodes are added to the end of the branches)
        text : this parameter will be used as a key
        value : this parameter will be used a position of the Node
        """
        new_node = Node(text,value)
        current_node = self.root
        while True:
            if value>current_node.get_value():
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            elif value<current_node.get_value():
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                print("ERRROR : Value is already exist!!")
                break

    def search_value(self,value):
        """
        Searches for a Node in Binary Search Tree.If no Nodes are founds,It returns an error.
        value : this parameter will be used a position of the Node 
        """
        current_node = self.root
        while True:
            if current_node.get_value() == value:
                return current_node.get_text()
            
            if value<current_node.get_value():
                if current_node.left is None:
                    return "ERROR : Not found."
                current_node = current_node.left
            elif value>current_node.get_value():
                if current_node.right is None:
                    return "ERROR : Not found"
                current_node = current_node.right

    def size(self):
        """
        Excecutes the _size() method without any parameter.
        """
        
        return self._size(self.root)
        
    def _size(self, current_node):
        """
        Calculates the size of the binary search tree.
        current_node : must be a node
        """
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def height(self):
        """
        Excecutes the _height() method without any parameters.
        """
        return self._height(self.root)
    def _height(self, current_node):
        """
        Calculate the number of parents for any given child.
        current_node : must be a node
        """
        if current_node is None:
            return 0
        return 1 + max(self._height(current_node.left),self._height(current_node.right))
    


    def delete_node(self,value):
        "Excecutes the _delete() method without any parameters."
        self.root = self._delete(self.root,value)

    def _delete(self,current_node,value):
        """
        This metod deletes any node that need to be deleted.
        
        
        """
        
        if current_node is None:
            return None
        
        if value < current_node.get_value():
            current_node.left = self._delete(current_node.left,value)

        elif value > current_node.get_value():
            current_node.right = self._delete(current_node.right,value)

        else:

            if current_node.left is None and current_node.right is None:
                return None
            
            elif current_node.left is None:
                return current_node.right
            
            elif current_node.right is None:
                return current_node.left
            

            else:
                successor = self.min_value_node(current_node.right)
                current_node.update_data(successor.get_text(),successor.get_value())
                current_node.right = self._delete(current_node.right,successor.getvalue())

        return current_node
    
    def _min_value_node(self,node):
        current = node 
        while current.left is not None:
            current = current.left 
        return current
    


if __name__ == "__main__":
    
      


    my_tree = BinaryTree("Mehmet",32)
 
    my_tree.add_node("Sabriye",9)
    my_tree.add_node("Emirhan",31)
    my_tree.add_node("Ata",41)
    my_tree.add_node("Burdur",15)
    my_tree.add_node("Konya",42)
    my_tree.add_node("Bilecik",11)

    print(my_tree.search_value(41))
    print(my_tree.search_value(82))
    print(my_tree.size())
    print(my_tree.height())





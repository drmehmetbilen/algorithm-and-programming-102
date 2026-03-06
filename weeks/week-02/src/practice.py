
#
#   This branch is cloned from https://github.com/drmehmetbilen/algorithm-and-programming-102
#   Please checkout the main repository for updates!
#   
#   Repo owner : drmehmetbilen
#   Pull request made by : weaponm249entity aka. Onur Yüksel
#

# Binary Search Tree 
# Node and Tree Class Definitations.    Complete!
# Add New Node.                         Complete and Tweaked!
# Find Value.                           Complete and Tweaked!
# Size.                                 Completed!
# Height.                               Completed!
# Delete.                               Completed!

class Node():                               #   Create the data struct.
    def __init__(self,text,value):          #   The "__init__" method is the first thing to run when the Class is initialized (One of the first things to happen in the runtime that has user code.). 
        self.value = value                  
        self.text = text                    
        self.left = None                    #   These allow compositioning to happen. In this case allowing "Nodes" to have other child nodes in them.
        self.right = None                   #   Refer to the upper comment.

class BinaryTree():                         #   Create a class to manipulate and recieve results from a complex Node data structure.
    def __init__(self,text:str,value:int):
        self.root = Node(text.upper(),value)    #   The text.upper() sub-function makes the given text all uppercase getting rid of case sensitiveness in the structure. Reducing the chance of error and simplifying the logic.

    def add_node(self,text:str,value:int):  #   Add a Node to the tree considering the trees inhabitants.
        currentNode = self.root                     #   Retrieves the root node the moment this function runs.
        newNode = Node(text.upper(),value)          #   Convert given data into a pliable Node form and Convert the given string into a uppercase form. ex, hello! -> HELLO! This makes other methods in this class have less fail cases and gives more reliable output.
        while currentNode:                      
            if value > currentNode.value:           #
                if currentNode.right is None:       #
                    currentNode.right = newNode     #
                    break                           #   This is the basic BST (Binary Search Tree) algorithm. The basic logic can be explained as if you were starting the root Node (The First Node)
                currentNode = currentNode.right     #   and comparing the wanted texts or in this case values to the child nodes of the root node. You may always not find the wanted value the first
            elif value < currentNode.value:         #   search so we use a comparison to get closer and closer to the value wanted. Going right if we have a value higher than the children or left
                if currentNode.left is None:        #   if the value is lower. We keep searching until we find the desired value or until the text matches.
                    currentNode.left = newNode      #
                    break                           #   In this instance we use the BST Algorith to add a node to the correct place.
                currentNode = currentNode.left      #
            else:
                print("This value already exists!")
                break
    
    def getValue(self,target):              #   The main method to acquire values in this Class.
        foundNode = self.searchintermediate(self.root, target.upper())  #    We use a intermediary method to avoid messy code and make the recursive method which is needed in searching possible. 
        if foundNode:                                                   
            return foundNode.value                                      #    The search sub-function returns the whole node itself so we will only extract the value out of it.

    def searchintermediate(self, currentNode, target):  #   The Searching Algorithm
        if currentNode is None:                                             #   This stops the recursion if the searching algorithm hit a empty Node spot.      
            return None
        if currentNode.text == target:                                      #   We found the Node!
            return currentNode
        left_result = self.searchintermediate(currentNode.left, target)     #
        if left_result:                                                     #   We search the tree going left everytime until we either hit the wanted node or we hit a empty node
            return left_result                                              #   if we do hit a empty node we go right of the parent node and start searching that node. Since we want to search everything
        return  self.searchintermediate(currentNode.right, target)          #   we continue searching left of that node too until we hit something we want or nothing.
                                                                            # 
                                                                            #   A Example search could go like this : Root -> Left -> Left -> Empty -> Go back and go Right -> Left -> Left -> Node Found!
                                                                            #

    def size(self):                         #   Gives the number of tree's inhabitants.
        return self.sizeintermediate(self.root)
    
    def sizeintermediate(self, current_node):
        if current_node is None:
            return 0                                                                #   Return 0 if the node is empty
        return 1 + self.sizeintermediate(current_node.left) + self.sizeintermediate(current_node.right)   #   Add 1 and add 1 more for every recall this function until every branch hits a empty Node

    def height(self):                       #   Gives the tree's most longest branch
        return self.heightintermediate(self.root)

    def heightintermediate(self, currentNode):
        if currentNode is None:
            return 0                                                                                        #   Return 0 if the Node is empty
        return 1 + max(self.heightintermediate(currentNode.left), self.heightintermediate(currentNode.right)) #   This functions like a size calculation but when the left and right branches converge take the highest of the branches size.
                                                                                                            #   Ensuring we get a continous line across the tree that gives us the deepest branch.

    def deleteDPO(self,target):             #   Deleting a Node but not keeping any orphaned nodes (Very Destructive). DPO standing for Dont Preserve Orphaned Nodes.
        if self.root.value == target or self.root.text == str(target).upper():                                  #   This is the algorithm to check if the given target is equal to the Root's value or text. Non-Case Sensitive.
            self.root = None                                                                                    #   This is the line that actually deletes the Node.
            return print("Tree Root Deleted...")
        parent = self.obliterateParent(self.root, target)                                                       #   The target is not the root node so we need to look deeper in the tree.

        if parent:                                                                                              
            if parent.left and (parent.left.value == target or parent.left.text == str(target).upper()):        #   This deletes left child of the parent node we get from the sub-function in line 76. We also make a failsafe incase the user gives either a value or key this function will always compare the relevant variables and not opposite varibles resulting in a ValueError.
                parent.left = None
            elif parent.right and (parent.right.value == target or parent.right.text == str(target).upper()):   #   This deletes right child of the parent node we get from the sub-function in line 76. We also make a failsafe incase the user gives either a value or key this function will always compare the relevant variables and not opposite varibles resulting in a ValueError.
                parent.right = None
            else:
                print("Target Not Found")

    def obliterateParent(self, currentNode, target):    
        if currentNode is None:                                         #   Checks if the Parent node is empty.
            return None             
        targetStr = str(target).upper()                                 #   The parent is not empty so lets get rid of case sensitivity.

        for child in [currentNode.left, currentNode.right]:             #   We put the potential two children of the parent node in a list to compare them seperately.
            if child:                                                   #   This is a failsafe to make sure the children actually exist otherwise the program could crash.  
                if child.value == target or child.text == targetStr:    #   Compare the children to the target
                    return currentNode                                  #   If we find the target in the children pool we return the childrens parent.
        
        left = self.obliterateParent(currentNode.left, target)          
        if left:                                                        #   We couldnt find the target in the search so we start a recursive algorithm here almost same as the searchintermediate sub-function's
            return left                                                 #   logic. We go from the most left and go right one leaf and go left from there until we find the target or we find nothing.
        return self.obliterateParent(currentNode.right, target)

    def delete(self,target):                #   Deleting a Node but keeping the rest of the sub-tree (Least Destructive).
        targetValue = None                                                  #   This is a placeholder variable which will get filled with the target's value.

        if isinstance(target, str):                                         #
            foundNode = self.searchintermediate(self.root, target.upper())  #   We have another check here to make sure if the user gives either a value or a text input we will always find the target node.
            if foundNode:                                                   #   the isinstance here is a method to check if the first variable's type is the same type of the second variable which is a string in this instance.
                targetValue = foundNode.value                               #   We will return the target's value to the placeholder variable above.
            else:                                                           #   
                print(f"Text {target} not found.")                          #   The target doesnt exist so we return nothing.
                return                                                      #
        else:                                                               #
            targetValue = target                                            #   The user gave a integer value so  we dont need to anything else lets proceed with the deletion procedure.
        
        self.root = self.deleteintermediate(self.root, targetValue)         #   Here we treat the deleted parent nodes new successor as a non-permanent root for now so we can later "sew" it back in to the main tree. Also we start the recursive algorithm for deletion here.

    def deleteintermediate(self, node, value):                                      
        if node is None:                                                            #    This is the base case in this recursive algorithm incase either the target value doesnt exist or one of the branches dont exist. A parent could have a very deep right branch but could have empty left branch too. This avoids a crash.                  
            return None
        
        if value < node.value:                                                      #
            node.left = self.deleteintermediate(node.left, value)                   #   This is a modified BST Algorith where it is almost like a search but we keep adding the children we find in the main tree into a seperate tree
        elif value > node.value:                                                    #   so later on we can "sew" it back together considering we find a successor to the now deleted parent node.
            node.right = self.deleteintermediate(node.right, value)                 #

        else:
            if node.left is None:                                                   #
                return node.right                                                   #   In this case the children of the main parent node either had one children tree or had no children at all
            elif node.right is None:                                                #   this is the most simple case to solve so we either just delete the node entirely(No Children Present) or
                return node.left                                                    #   Assign the Sole Child as the new Parent and move on.
            
            successorChild = self.getMin(node.right)                                #
                                                                                    #   In this case we have two seperate children so now we have to make a decision who gets to be the successor parent.
            node.value = successorChild.value                                       #   In order to make this decision we need to find the right value which is larger than the left child but also the smallest in the right sub-tree.
                                                                                    #   Why? if we were to write any other value we would end up with a parent that would have three children which doesnt fit the nature of our BST. This is Binary so Only 2 answers not 3.
                                                                                    #   So we find the smallest value in the right sub-tree with the getMin() method and appoint that node as the successor.
            node.text = successorChild.text                                         #   We overwrite the old parents data with the new successor child
                                                                                    #
            node.right = self.deleteintermediate(node.right, successorChild.value)  #   Since we overwrote the data now we have 2 duplicate children we remove the original child and leave the duped child as the parent.

        return node                                                                 #   Finally we return the entire tree.

    def getMin(self, node):                 #   Get the minimum value of a tree.
        current = node
        while current.left:
            current = current.left
        return current


if __name__ == "__main__":

    MyTree = BinaryTree("Root",65536)                                               #   Declaring the Root

    MyTree.add_node("Torvalds",1969)                                                #
    MyTree.add_node("Helsinki",128)                                                 #
    MyTree.add_node("Helk",32)                                                      #
    MyTree.add_node("Bilen",15)                                                     #
    MyTree.add_node("Stockholm",1142)                                               #   Adding Some Nodes.
    MyTree.add_node("Apple", 80000)                                                 #   
    MyTree.add_node("Kobenhavn",1842)                                               #
    MyTree.add_node("Istanbul",1453)                                                #
    MyTree.add_node("Linux", 70000)                                                 #
    MyTree.add_node("Python", 90000)                                                #



    print(f"Tree Size: {MyTree.size()}")                                            #   Expected: 11
    print(f"Tree Height: {MyTree.height()}")                                        #   Expected: 4

    # Testing getValue

    result = MyTree.getValue("HELSINKI")
    if result:
        print(result)                                                               #   Expected: 128

    # Testing deleteDPO (Destructive)
    # Lets obliterate the "Apple" branch (80000). 
    # This should also take out Linux (70000) and Python (90000).

    MyTree.deleteDPO("APPLE")
    print(f"Size after Obliterating Apple branch: {MyTree.size()}")                 #   Expected: 8

    # Testing delete (Sewing)
    # Let's delete "Torvalds" (1969) but "sew" its child (Helsinki) back in.

    MyTree.delete("TORVALDS")
    print(f"Size after Sewing Torvalds away: {MyTree.size()}")                      #   Expected: 7

    # Final Check

    final_search = MyTree.getValue("HELSINKI")
    print(f"Is Helsinki still here? {'Yes' if final_search else 'No'}")

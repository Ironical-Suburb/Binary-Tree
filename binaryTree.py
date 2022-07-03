class BinaryTree:
    def __init__(self, rootElement):
        self.key = rootElement
        self.left = None
        self.right = None
        
    '''getters'''
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getKey(self):
        return self.key
    
    '''setters'''
    def setKey(self,key):
        self.key=key
        
    def setLeft(self,left):
        self.left=left        
  
    def setRight(self,right):
        self.right=right
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
  
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t 
            
    def _strHelper(self):
        """Returns list of strings,  total width of the tree, position of the middle node and the height"""
        # Base case, no child.
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.key
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.key
        keyStrLength = len(keyStr)
        # Case 1: only have left child
        if self.getLeft() != None and self.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength,leftWidth + keyStrLength // 2, leftHeight + 2

        # Case 2: only have right child
        elif self.getLeft() == None and self.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength,keyStrLength // 2, rightHeight + 2, 

        # Two children.
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper() 
          
    
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            #append a few rows to fill in the blanks in the bottom, so that left and right lists are of the length
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength,  leftWidth + keyStrLength // 2,max(leftHeight, rightHeight) + 2
    
    
    def __str__(self):
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result
    
    
def preorder(tree):
    '''
    print the value of a tree in a Preorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''  
    #TODO delete pass and write your code
    # Got from Class Notes 
    if tree != None:
        print(tree.getKey())
        preorder(tree.getLeft())
        preorder(tree.getRight())
        
def inorder(tree):
    '''
    print the value of a tree in an Inorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''  
    #TODO delete pass and write your code
    # Got from Class Notes 
    if tree != None:
        inorder(tree.getLeft())
        print(tree.getKey())
        inorder(tree.getRight())

def postorder(tree):
    '''
    print the value of a tree in a postorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''       
    #TODO delete pass and write your code
    # Got from Class Notes 
    if tree != None:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print(tree.getKey())
        

def findMinKey(tree):
    '''
    find the minimum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''       
    #TODO delete pass and write your code
    if tree == None:
        return None 
    
    test_list = []
    check_root = tree.getKey()
    if check_root != None:
        test_list.append(check_root)
    check_left = findMinKey(tree.getLeft())
    if check_left != None:
        test_list.append(check_left)
    check_right = findMinKey(tree.getRight())
    if check_right != None:
        test_list.append(check_right)
        
    return min(test_list)

def findMaxKey(tree):
    '''
    find the maximum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''       
    #TODO delete pass and write your code
    if tree == None:
        return None 
    
    test_list = []
    check_root = tree.getKey()
    if check_root != None:
        test_list.append(check_root)
    check_left = findMaxKey(tree.getLeft())
    if check_left != None:
        test_list.append(check_left)
    check_right = findMaxKey(tree.getRight())
    if check_right != None:
        test_list.append(check_right)
        
    return max(test_list) 


def buildTree(inOrder, preOrder): 
    '''
    Build a binary tree based on given Inorder and PreOrder traversals
    
    Parameters:
        - inOrder,preOrder (list of numbers)
    
    Returns: a BinaryTree object
    '''  
    
    #TODO delete pass and write your code
    
    #base case:
    if 0 > len(inOrder)-1:
        return 0 #return 0 if start is bigger than end 
    
    #get the root value
    root_value = BinaryTree(preOrder[0]) # Creating the root node 
    
    if 0 == (len(inOrder)-1):
        return root_value
    get_index = inOrder.index(root_value.getKey()) #find the index of root value in Inorder traversal
    len_get_index = len(inOrder[:get_index]) # How many traversals required
    root_value.left = buildTree(inOrder[:get_index],preOrder[1:len_get_index+2])  #creating the left side of the tree 
    root_value.right = buildTree(inOrder[(get_index)+1:],preOrder[(get_index)+1:]) #creating the right side of the tree 
    
    #build the tree recursively
    return root_value

def main():
    tree = BinaryTree(1)
    tree.insertLeft(2)
    tree.insertRight(7) 
    tree.getLeft().insertLeft(3)
    tree.getLeft().insertRight(6)
    tree.getLeft().getLeft().insertLeft(4)
    tree.getLeft().getLeft().insertRight(5)
    tree.getRight().insertLeft(8)
    tree.getRight().insertRight(9)

    print("the tree:\n")
    print(tree)
    
    print("preorder traversal:")
    preorder(tree)
    print()
    print("inorder traversal:")
    inorder(tree)
    print()
    print("postorder traversal:")
    postorder(tree)
    print()

    print('Max value in tree:', findMaxKey(tree))
    print('Min value in tree:', findMinKey(tree))

    inor = [4,3,5,2,6,1,8,7,9]
    preor = [1,2,3,4,5,6,7,8,9]

    theTree = buildTree(inor,preor)
    
    print(theTree)
    inor2 = [3,2,4,1,5]
    preor2 = [1,2,3,4,5]

    theTree2 = buildTree(inor2,preor2)
    
    print(theTree2)  
    
    
if __name__ == "__main__":
    main()        
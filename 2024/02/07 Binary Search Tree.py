class Node:
    def __init__(self,item):
        self.left = None
        self.item = item
        self.right = None
        
    def insert(self, item):
        if self.item != None:
            if self.item > item:
                if self.left == None:
                    self.left = Node(item)     
                else:
                    self.left.insert(item)
            elif self.item < item:
                if self.right == None:
                    self.right = Node(item)     
                else:
                    self.right.insert(item)       
        else:
            self.item = item

    def inOrder(self):
        if self.left != None:
            self.left.inOrder()
        print(self.item)
        if self.right != None:
            self.right.inOrder()

    def preOrder(self):
        print(self.item)
        if self.left != None:
            self.left.preOrder()        
        if self.right != None:
            self.right.preOrder()

    def postOrder(self):
        if self.left != None:
            self.left.postOrder()        
        if self.right != None:
            self.right.postOrder()
        print(self.item)


tree = Node(27)
tree.insert(20)
tree.insert(29)
tree.insert(30)
tree.insert(12)
tree.insert(25)

tree.inOrder()
print()
tree.preOrder()
print()
tree.postOrder()
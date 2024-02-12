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
        print(self.item)



tree = Node(27)
tree = Node.insert(20)
tree = Node.insert(29)
tree = Node.insert(30)
tree = Node.insert(12)
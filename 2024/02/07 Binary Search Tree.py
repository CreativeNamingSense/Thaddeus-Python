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


tree = Node(27)
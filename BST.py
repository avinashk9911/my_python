class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key==None:
            self.key=BST(data)
        else:
            if self.key>data:
                if self.lchild:
                    self.lchild.insert(data)
                else:
                    self.lchild=BST(data)
            else:
                if self.rchild:
                    self.rchild.insert(data)
                else:
                    self.rchild=BST(data)
    
    def search(self,data):
        #if self.key==None:
            #return False
        #else:
        if data==self.key:
            print("the node is present in the tree")
            return True
        if data>self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("the node is not present in the right tree")
                return False
        #elif data<self.key:
        else:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("the node is not present in the left tree")
                return False
                
    def printBST(self):
        if self.key==None:
            return False,"no tree"
        if self.lchild:
            self.lchild.printBST()
        print(self.key)
        if self.rchild:
            self.rchild.printBST()

    def delete(self,data):
        if self.key==None:
            return "no binart tree"
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("the node is not present in lchild")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("data is not present in the rchild")
        else:
            if self.lchild == None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild==None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)

        return self
        
tree=BST(7)
a=[1,2,3,4,5,6,8,9,10,11]
for _ in a:
    tree.insert(_)
tree.printBST()
print()
tree.search(11)
tree.delete(1)
print()
tree.printBST()

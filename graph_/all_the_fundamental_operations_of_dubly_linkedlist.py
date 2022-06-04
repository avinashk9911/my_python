# all_the_fundamental_operations_of_dubly_linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
    
class llist:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            new.prev=n
            n.next=new
            self.tail=new

    def add_head(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    
    def add_tail(self,data):
        new=Node(data)
        # n=self.head
        # while n.ref!=None:
        #     n=n.ref
        # n.ref=new
        new.next=self.tail
        self.tail=new 

    def insertbefore(self,data):
        if self.head==None:
            

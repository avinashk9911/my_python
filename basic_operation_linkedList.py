from tkinter import N


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dllist:
    def __init__(self):
        self.head=None
    
    def add_node(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new

        else:
            n=self.head
            while n.next!=None:
                n=n.next
            new.prev=n
            n.next=new

    def printdll(self):
        if self.head==None:
            return 'the linked lsit is empty!'
        else:
            n=self.head
            while n != None:
                print(n.data,end='->')
                n=n.next

    def add_front(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head.prev=self.head
            self.head=new         
    
    

dll=dllist()

a=[1,2,3,4,5,6,7,8]
for _ in a:
    dll.add_node(_)
dll.printdll()
print()

dll.add_front(100)
dll.printdll()
print()




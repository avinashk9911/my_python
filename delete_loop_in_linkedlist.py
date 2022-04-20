from itsdangerous import NoneAlgorithm


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class llist:
    def __init__(self):
        self.head=None
    
    def printll(self):
        n=self.head
        if self.head==None:
            return 'the linked list is empty!'
        else:
            while n!=None:
                print(n.data, end='->')
                n=n.ref

    def add_end(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=new

    def createloop(self):
        if self.head==None:
            return 'the linked list is empty!'
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=self.head
    
    def deleteloop(self):
        if self.head==None:
            return 'the linked list is empty!'
        else:
            s=set()
            n=self.head
            while n != None:
                if n in s:
                    n.ref=None
                else:
                    s.add(n)
                    n=n.ref

ll=llist()
print('adding elements to the end of the list')
a=[3,4,5,6,234,56,45]
for _ in a:
    ll.add_end(_)
ll.printll()
print()

ll.createloop()

ll.deleteloop()
ll.printll()
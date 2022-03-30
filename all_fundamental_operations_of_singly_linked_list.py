from selectors import EpollSelector


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

    def add_starting(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            new.ref=self.head
            self.head=new
    
    def add_between(self,x,data): #thsi will add the new node in front of x
        if self.head==None:
            self.head=Node(data)
            return f'the linked list was empty, so thre is no node {x}'
        elif self.head.data==x:
            new=Node(data)
            new.ref=self.head
            self.head=new
        else:
            new=Node(data)
            n=self.head
            while n.ref.data!=x:
                n=n.ref
            new.ref=n.ref
            n.ref=new

    def reversell(self):
        prev=None
        n=self.head
        while n!=None:
            temp=n.ref
            n.ref=prev
            prev=n
            n=temp
        self.head=prev
   
    # def delete_end(self):
    #     if self.head==None:
    #        return 'the linked list is empty'
    #     else:
    #         n=self.head
    #         while n.ref!=None:
    #             n=n.ref
            

ll=llist()
print('adding elements to the end of the list')
a=[3,4,5,6,234,56,45]
for _ in a:
    ll.add_end(_)
ll.printll()
print()
print('adding elements to the start of the list')
a=[4,35,6,767,34,546,67,45]
for _ in a:
    ll.add_starting(_)
ll.printll()
print()

print('add a new element infront of the given node x')
ll.add_between(35,100)
ll.printll()
print()

print('Reverse the linked list')
ll.reversell()
ll.printll()
print()

# reverse a linked list in a given group
# LinkedList: 1->2->2->4->5->6->7->8
# K = 4
# Output: 4 2 2 1 8 7 6 5 
# Explanation: 
# The first 4 elements 1,2,2,4 are reversed first 
# and then the next 4 elements 5,6,7,8. Hence, the 
# resultant linked list is 4->2->2->1->8->7->6->5.

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

    def reversegroup(self,k):
        count=0
        prev=None
        current=self.head
        while current!=None and count<k:
            temp=current.ref
            current.ref=prev
            prev=current
            current=temp
            count+=1
        self.head.ref=temp
        self.head=prev

ll=llist()
print('adding elements to the end of the list')
a=[3,4,5,6,234,56,45]
for _ in a:
    ll.add_end(_)
ll.printll()
print()

print('reverse a linked list in a given group!')
ll.reversegroup(3)
ll.printll()
print()
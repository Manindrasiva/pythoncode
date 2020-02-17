from Node import Node
class Linkedlist:
    def __init__(self):
        self.head=None

    def add(self,data):
        newnode=Node(data)
        if(self.head is None):
            self.head=newnode
        else:
            current=self.head
            while(current.nextnode is not None):
                current=current.nextnode
            current.nextnode=newnode

    def addatFirst(self,data):
        newnode=Node(data)
        if(self.head is None):
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode


    def print(self):
         n=self.head
         while(n is not None):
             print(n.data," ")
             n=n.nextnode

    def reverse(self):
        current =self.head
        prev=None
        while(current is not None):
            next =current.nextnode
            current.nextnode=prev
            prev=current
            current=next
        self.head=prev

    def  inserAtpos(self,pos,data):

        if(self.head is None and  pos==0 ):
            self.addatFirst(data)
        else:
            current=self.head
            n = Node(data)
            prev=None
            count=1
            while(current is not None):
                count=count+1
                prev=current
                if(pos == count):
                    break
                current=current.nextnode
            n.nextnode=current.nextnode
            prev.nextnode=n
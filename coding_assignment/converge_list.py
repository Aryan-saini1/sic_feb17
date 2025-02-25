class Node:
    def __init__(self,data=0,link=None):
        self.data=data
        self.link=link
    def insert_node(self):
        new_node=Node()
        new_node.data=int(input("Enter data to be inserted:"))
        pos=int(input("Enter position where to insert:"))
        if pos<=0:  
            print("Invalid position")
            return
        prev = self
        for _ in range(pos - 1):
            if prev.link is None:
                print("Invalid Position")
                return
            prev = prev.link
        new_node.link = prev.link
        prev.link = new_node
def check_converge(n1,n2):
    temp1=n1
    temp2=n2
    i=0
    while temp1 !=None and temp2 !=None:
        if temp1==temp2:
            print("The List Converge at",i)
            return
    else:
        print("List do not converge")

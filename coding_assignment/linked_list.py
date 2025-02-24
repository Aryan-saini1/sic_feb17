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
    def delete_node(self):
        pos=int(input("Enter position to delete:"))
        prev = self
        for _ in range(pos - 1):
            if prev.link is None:
                print("Invalid Position")
                return
            prev=prev.link
        if prev.link is None:
            print("Invalid Position")
            return
        prev.link=prev.link.link
    def display(self):
        cur=self.link
        if cur==None:
            print(None)
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.link
        print("None")

    def rev_display(self):
        rev = []
        cur = self.link  
        while cur is not None:
            rev.append(cur.data)
            cur = cur.link
        if not rev:
            print("None")
            return
        print(" -> ".join(map(str, reversed(rev))),end=" -> ")
        print(None)
class Menu:
    def __init__(self):
        pass
    def run_menu(self,first):
        while True:
            ch=int(input("1.Insert Node\n2.Display\n3.Delete\n4.Reverse display\n5.Exit\nEnter choice:"))     
            match ch:
                case 1:first.insert_node()
                case 2:first.display()
                case 3:first.delete_node()
                case 4:first.rev_display()
                case 5:exit(0)  
menu=Menu()
first=Node()
menu.run_menu(first)
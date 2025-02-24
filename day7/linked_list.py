class Node:
    def __init__(self,data=0,link=None,cnt=0):
        self.data=data
        self.link=link
        self.cnt=cnt
    def insert_node(self):
        new_node=Node()
        new_node.data=int(input("Enter data to be inserted:"))
        pos=int(input("Enter position where to insert:"))
        if pos == 0:  
            new_node.link = self.link
            self.link = new_node
        else:
            prev = self
            for _ in range(pos - 1):
                if prev.link is None:
                    print("Invalid Position")
                    return
                prev = prev.link
            new_node.link = prev.link
            prev.link = new_node
        self.cnt += 1
    def display(self):
        cur=self.link
        while cur.link!=None:
            print(cur.data,end="->")
            cur=cur.link
        print(cur.data,end="->")
        print(None)
class Menu:
    def __init__(self):
        pass
    def run_menu(self,first):
        while True:
            ch=int(input("1.Insert Node\n2.Display\n3.Exit\nEnter choice:"))     
            match ch:
                case 1:first.insert_node()
                case 2:first.display()
                case 3:exit(0)  
menu=Menu()
first=Node()
menu.run_menu(first)
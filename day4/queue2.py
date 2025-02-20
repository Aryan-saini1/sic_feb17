class Queue():
    def __init__(self,size=5):
        self.queue=[]
        self.size=size
    def insert(self):
        if len(self.queue)==self.size:
            print("Queue overflow")
            return
        element=int(input("Enter a number to be inserted:"))
        self.queue.insert(0,element)
        print("Element inserted !")
    def delete(self):
        if not self.queue:
            print("Queue underflow")
            return
        print(f"Element deleted is {self.queue[-1]}")
        self.queue.pop()
    def display(self):
        if not self.queue:
            print("Queue empty")
            return
        print(f"Queue is:{self.queue}")
class Menu:
    def get_menu(self,queue):
        menu={1:queue.insert,
              2:queue.delete,
              3:queue.display,
              4:self.end_of_prgm}
        return menu
    def select_menu(self):
        queue=Queue()
        while True:
            choice=int(input("1.Insert\n2.Delete\n3.Display\n4.Exit\nchoice:"))
            menu=self.get_menu(queue)
            menu.get(choice,self.invalid_choice)()
    def end_of_prgm(self):
        exit(0)
    def invalid_choice(self):
        print("Invalid Choice !")
menu=Menu()
menu.select_menu()

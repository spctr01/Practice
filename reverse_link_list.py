class  Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class chain:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
       

    def display(self):
        start = self.head
        while start.next !=None:
            start = start.next
            print(start.data)

             

    def  rev(self):
        prev = None
        cur = self.head
        while cur:
            a = cur.next
            cur.next = prev
            prev = cur
            cur = a

        self.head = prev 
        


c = chain()

c.append(1)
c.append(2)
c.append(3)
c.append(4)
c.display()
print('reverse------------')
c.rev()
c.display()
print(c.head.data)
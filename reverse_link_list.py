class  Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class chain:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            cur = self.head
            while cur.next != None :
                cur = cur.next
            cur.next = new
       

    def display(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

             
#iterative method time = O(N)  space = O(1)
    def  rev(self):
        prev = None
        cur = self.head
        while cur:
            a = cur.next
            cur.next = prev
            prev = cur
            cur = a

        self.head = prev 

# reverse usinf recursion t = O{n}  S= O(n)        
    def rec_rev(self, node):
        cur = node
        if not cur or cur.next is None:
            self.head = cur
            return

        self.rec_rev(cur.next)
        cur.next.next = cur
        cur.next = None




c = chain()

c.append(1)
c.append(2)
c.append(3)
c.append(4)
c.display()
print('reverse------------')
c.rev()
c.display()
print('rec-----------------')
c.rec_rev(c.head)
c.display()
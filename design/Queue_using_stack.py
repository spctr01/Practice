class stack:
    """
    Queue using two stack
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, num):
        while self.stack1:
            self.stack2.insert(0, self.stack1[0])
            self.stack1.remove(self.stack1[0])

        self.stack1.append(num)

        while self.stack2:
            self.stack1.insert(0, self.stack2[0])
            self.stack2.remove(self.stack2[0])

        return self.stack1

    def pop(self):
        self.stack1.pop(0)
        return self.stack1


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()

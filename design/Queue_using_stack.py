from pipes import quote


class Queue:
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


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
quote.pop()

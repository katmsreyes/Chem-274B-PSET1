class Queue:
    def __init__(self):
        self.stack1 = []  # for enqueue
        self.stack2 = []  # for dequeue

    def enqueue(self, val):
        # TODO: Implement
        
        self.stack1.append(val)
    

    def dequeue(self):
        # TODO: Implement

        if len(self.stack2) == 0 and len(self.stack1 !=0):
            self.stack2.append(self.stack1.pop())

    def peek(self):
        # TODO: Implement
        return self.stack1[0]

    def is_empty(self):
        # TODO: Implement
        return not bool(self.stack1)

    def get_size(self):
        # TODO: Implement
        print('Length of stack 1: ') , len(self.stack1))
        print('Length of stack 2: '), len(self.stack2)
        return len(self.stack1), len(self.stack2)


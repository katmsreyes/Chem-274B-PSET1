class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, val):
        # TODO: Implement

        new_node = ListNode(val)

        self.rear.insert(new_node)

        if self.size == 0 : #queue is empty
            new_node = self.front = self.rear
        else:
            self.rear.next = new_node
            self.rear = new_node



    def dequeue(self):
        # TODO: Implement
        
        if self.size != 0:
            self.front = self.front.next
            self.size -=1
            if self.size == 0:
                self.rear = None
                print('the queue is now empty')
        
        else:
            print('queue is empty')
            


    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.val

    def is_empty(self):
        # TODO: Implement
        if self.size ==0:
            print('queue is empty')

    def get_size(self):
        return self.size
    
 

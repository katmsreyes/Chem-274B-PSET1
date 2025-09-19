class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self, head):
        # TODO: Implement
        #building linked list

        N = 6
        head = ListNode(0)
        current = head
        for i in range (1,N):
            current.next = ListNode(i)
            current = current.next


            
        #reversing linked list
        
        current = head
        previous = None
        for _ in range (N):

            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        current = previous  # previous is the new head
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next

x = Solution()
print(x.reverse_linked_list(None))





    #[1,2,3,4,5]
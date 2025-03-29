class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    prev = None
    curr = head
    new_head = head.next
    while curr and curr.next:
        first = curr
        second = curr.next
        next_node = second.next
        second.next = first
        if prev:
            prev.next = second
        first.next = next_node
        prev = first
        curr = next_node
    return new_head







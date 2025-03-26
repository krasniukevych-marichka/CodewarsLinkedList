class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return head
    prev = head
    curr = head.next
    while curr is not None:
        if prev.data == curr.data:
            prev.next = curr.next
            curr = curr.next
        else:
            curr = curr.next
            prev = prev.next
    return head
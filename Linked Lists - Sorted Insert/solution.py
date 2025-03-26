class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    curr = head
    if head is None:
        head = Node(data)
        return head
    if head.data >= data:
        new_node = Node(data)
        new_node.next = head  
        head = new_node
        return head
    while curr.next is not None:
        if curr.next.data > data:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
            return head
        curr = curr.next
    new_node = Node(data)
    curr.next = new_node
    return head
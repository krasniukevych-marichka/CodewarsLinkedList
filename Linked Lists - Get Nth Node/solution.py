class Node:
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    count = 0
    curr = node
    while curr is not None:
        if count == index:
            return curr
        else:
            count += 1
    raise IndexError
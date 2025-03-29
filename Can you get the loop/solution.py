class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    first = node
    second = node
    lenght = 0
    while second and second.next:
        first = first.next
        second = second.next.next
        if first == second:
            curr = first
            lenght += 1
            curr = curr.next
            while curr!=first:
                lenght += 1
                curr = curr.next
            return lenght
    return lenght

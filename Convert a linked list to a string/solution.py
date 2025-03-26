class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    curr = node
    result = []
    while curr is not None:
        result.append(str(curr.data))
        curr = curr.next
    result.append(str(curr))
    return " -> ".join(result)

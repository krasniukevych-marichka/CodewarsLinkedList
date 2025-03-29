class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    first_lst = []
    second_lst = []
    curr = head
    is_first = True
    while curr:
        if is_first:
            first_lst.append(curr)
        else:
            second_lst.append(curr)
        curr = curr.next
        is_first = not is_first

    for i in range(len(first_lst) - 1):
        first_lst[i].next = first_lst[i + 1]
    if first_lst:
        first_lst[-1].next = None

    for i in range(len(second_lst) - 1):
        second_lst[i].next = second_lst[i + 1]
    if second_lst:
        second_lst[-1].next = None

    return Context(first_lst[0], second_lst[0])


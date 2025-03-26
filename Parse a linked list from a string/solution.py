class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    linked_list = s.split(" -> ")
    head = None
    for data in linked_list[::-1]:
        if data != "None":
            if data.strip().isdigit():
                head = Node(int(data), head)
            else:
                head = Node(data, head)
    return head
    



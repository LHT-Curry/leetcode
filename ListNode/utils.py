class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create(val_list):
    if not val_list:
        return None
    head = res = ListNode(val_list[0])
    for i in range(1, len(val_list)):
        res.next = ListNode(val_list[i])
        res = res.next
    return head


def printnode(head):
    printlist = []
    while head:
        printlist.append(head.val)
        head = head.next
    return printlist
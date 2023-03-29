from utils import ListNode, create, printnode


class Soluntion:
    def delete_node(self, listnode, val):
        head = res = ListNode(0)
        head.next = listnode
        while head.next:
            if head.next.val == val:
                tmp = head.next.next
                head.next = tmp
            else:
                head = head.next
        return res.next


test = Soluntion()
r = create([0,1,2,3,4])
res = test.delete_node(r, 3)
print(printnode(res))
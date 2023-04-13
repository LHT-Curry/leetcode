from utils import ListNode, create, printnode
class Soluntion:
    def change_node(self, head):
        a = ListNode(-1)
        a.next = head
        res = a
        while head and head.next:
            b = head.next.next
            c = head.next
            a.next = c
            head.next = b
            c.next = head
            a = head
            head = b
        return res.next
test = Soluntion()
r = create([1,2,3,4,5])
res = test.change_node(r)
print(printnode(res))
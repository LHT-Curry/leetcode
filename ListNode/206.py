from utils import ListNode, create, printnode


class Soluntion:
    def clip_node(self, head):
        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        return last


test = Soluntion()
r = create([0,1,2,3,4])
res = test.clip_node(r)
print(printnode(res))
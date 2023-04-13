from utils import ListNode, create, printnode
class Soluntion:
    def del_node(self, head, k):
        res = ListNode(-1)
        res.next = head
        fast = slow = head
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        if k > 0:
            return res.next
        pre = res
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next
        tmp = slow.next
        pre.next = tmp
        return res.next
test = Soluntion()
r = create([1,2,3,4])
res = test.del_node(r, 2)
print(printnode(res))
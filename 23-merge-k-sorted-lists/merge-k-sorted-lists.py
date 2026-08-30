class Solution(object):
    def mergeKLists(self, lists):
        num = []

        for x in lists:
            if isinstance(x, list):
                num += x
            else:
                while x:
                    num.append(x.val)
                    x = x.next

        num.sort()

        dummy = ListNode(0)
        current = dummy

        for x in num:
            current.next = ListNode(x)
            current = current.next

        return dummy.next

lists = [[1,4,5],[1,3,4],[2,6]]
a = Solution()
print(a.mergeKLists(lists))
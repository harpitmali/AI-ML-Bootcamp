# This is just the required solution of the problem this doesn't run properly


def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
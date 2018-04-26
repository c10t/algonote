"""
Detect a cycle in a linked list.
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head.next

    while slow is not fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

from typing import Optional
from Python.merge_sort import ListNode

"""
    Time complexity : O(max(m,n)). 
    Assume that m and n represents the length of l1 and l2 respectively, 
    the algorithm above iterates at most max(m,n) times.

    Space complexity : O(1). The length of the new list is at most max(m,n)+1 
    However, we don't count the answer as part of the space complexity.
"""


def add_two_numbers(
        l1: Optional[ListNode],
        l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Initialize current node to dummy head of the returning list.
    Initialize carry to 0."""
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    """Loop through lists l1 and l2 until you reach both ends and carry is 0. """
    while l1 is None or l2 is None or carry != 0:
        "Set x to node l1's value."
        "If l1 has reached the end of l1, set to 0."
        l1_val = l1.val if l1 else 0
        "Set y to node l2's value."
        "If l2 has reached the end of l2, set to 0."
        l2_val = l2.val if l2 else 0
        "Set sum=x+y+carry."
        column_sum = l1_val + l2_val + carry
        "Update carry=sum/10."
        carry = column_sum // 10
        "Create a new node with the digit value of (sum mod 10)"
        "set it to current node's next"
        "then advance current node to next."
        new_node = ListNode(column_sum % 10)
        current.next = new_node
        current = new_node
        "Advance both l1 and l2."
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    "Return dummy head's next node."
    return dummy_head.next

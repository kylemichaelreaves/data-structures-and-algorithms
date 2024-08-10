# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def rotate_right(head, k)
  return head if head.nil? || head.next.nil? || k == 0

  # Compute the length of the list and make the list circular
  length = 1
  old_tail = head
  while old_tail.next
    old_tail = old_tail.next
    length += 1
  end
  old_tail.next = head  # Make the list circular

  # Find the new tail and the new head
  k = k % length
  new_tail = head
  (length - k - 1).times do
    new_tail = new_tail.next
  end
  new_head = new_tail.next

  # Break the circle
  new_tail.next = nil

  new_head

end
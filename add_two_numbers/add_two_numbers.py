# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(3)
a.next = ListNode(4)

b = ListNode(1)
b.next = ListNode(2)

class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        val_one = Solution.create_string_from_list_node(l1)
        val_two = Solution.create_string_from_list_node(l2)
        val_sum = int(val_one) + int(val_two)
        result = Solution.create_list_node_from_string(val_sum)

        return result

    @staticmethod
    def create_string_from_list_node(list_node: ListNode):
        val = ""
        list_node = list_node
        while list_node.next:
            val += str(list_node.val)
            list_node = list_node.next
        else:
            val += str(list_node.val)
        return val[::-1]

    @staticmethod
    def create_list_node_from_string(value: int):
        last_node = None
        list_numbers = list(str(value)[::-1])
        prev_node = None
        for i in list_numbers[::-1]:
            node = ListNode(i)
            node.next, prev_node = prev_node, node
            last_node = node
        return last_node

    @staticmethod
    def add_two_numbers_nice(l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = ListNode(0)
        head = current
        helper = current
        _sum = 0
        carrier = 0

        while(l1 or l2):
            if not l1:
                _sum = l2.val + carrier
                l2 = l2.next
            elif not l2:
                _sum = l1.val + carrier
            else:
                _sum = l1.val + l2.val + carrier
                l1 = l1.next
                l2 = l2.next
            if _sum >= 10:
                carrier = 1
            else:
                carrier = 0

            current.val = _sum % 10
            current.next = ListNode(0)
            current = current.next

        if carrier == 1:
            current.val = 1
        else:
            helper.next = None

        return head

test = Solution()
test.add_two_numbers_nice(a, b)
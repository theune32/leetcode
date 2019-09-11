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


# test = Solution()
# test.addTwoNumbers(a, b)

def test_simple_version():
    l1 = Solution.create_list_node_from_string(243)
    l2 = Solution.create_list_node_from_string(515)
    l3 = Solution.create_list_node_from_string(758)
    value = Solution.addTwoNumbers(l1, l2)

    assert value == l3

test_simple_version()

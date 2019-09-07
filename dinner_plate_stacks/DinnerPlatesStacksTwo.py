from copy import deepcopy


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.non_max_stacks = []
        self.stacks = [[]]
        self.current_stack = None

    def _verify_stack(self, stack=None, index=None):
        if not stack:
            if len(self.current_stack) == self.capacity:
                self.stacks.append([])
                self.current_stack = self.stacks[-1]
        else:
            if len(stack) == self.capacity:
                self.non_max_stacks.remove(index)

    def push(self, val: int) -> None:
        if not self.non_max_stacks:
            self.current_stack.append(val)
            self._verify_stack()
        else:
            index = min(self.non_max_stacks)
            stack = self.stacks[min(self.non_max_stacks)]
            stack.append(val)
            self._verify_stack(stack=stack, index=index)

    def _clean_stacks_tail(self):
        if not self.stacks[-2]:
            self.stacks.pop()
            self.non_max_stacks.remove(len(self.stacks))
            self._clean_stacks_tail()
        else:
            self.current_stack = self.stacks[-1]

    def pop(self) -> int:
        if self.current_stack:
            value = self.current_stack.pop()
            self._verify_stack()
            return value
        elif self.stacks == [[]]:
            return -1
        else:
            self._clean_stacks_tail()
            self.current_stack = self.stacks[-2]
            return self.current_stack.pop()

    def _check_index(self, index):
        len_stacks = len(self.stacks)
        print(len_stacks, index)
        if index > (len_stacks - 1):
            return None
        elif index == len_stacks - 1:
            return self.current_stack
        else:
            return self.stacks[index]

    def popAtStack(self, index: int) -> int:
        stack = self._check_index(index)
        if not stack:
            return -1
        elif len(stack) == 1:
            value = stack.pop()
            if index == len(self.stacks) - 1:
                self.stacks.pop()
            return value
        elif len(stack) == self.capacity:
            self.non_max_stacks.append(index)
            return stack.pop()
        else:
            return stack.pop()

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

def test_func(commands, values, output):
    d_p = DinnerPlates(values[0][0])
    todo = zip(commands, values, output)
    for i in todo:
        if i[0] == "pop":
            value = d_p.pop()
            assert value == i[2]
        elif i[0] == 'push':
            d_p.push(i[1][0])
        elif i[0] == 'popAtStack':
            value = d_p.popAtStack(i[1][0])
            assert value == i[2]
        elif i[0] == 'DinnerPlates':
            pass
        else:
            print("error, unrecognised command")
        print(i, d_p.stacks, d_p.current_stack, d_p.non_max_stacks)

# Input: 
t_commands = ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
t_values = [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output: 
t_output = [None,None,None,None,None,None,2,None,None,20,21,5,4,3,1,-1]

test_func(t_commands, t_values, t_output)
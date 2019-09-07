
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.non_max_stacks = []  # contains the indices of all stacks not a max capacity except the current one
        self.stacks = []  # list of all stacks, last stack can not be empty
        self.current_stack = None  # rightmost stack that is not empty

    def _remove_from_non_max_stacks(self, index):
        if index in self.non_max_stacks:
            self.non_max_stacks = [x for x in self.non_max_stacks if x is not index]

    def push(self, val: int) -> None:
        if not self.non_max_stacks:
            if self.current_stack is None:
                stack = []
                self.stacks.append(stack)
                self.current_stack = stack
                stack.append(val)
            else:
                self.current_stack.append(val)
            if len(self.current_stack) == self.capacity:
                self.current_stack = None
        else:
            left_stack_index = min(self.non_max_stacks)
            left_stack = self.stacks[left_stack_index]
            left_stack.append(val)
            if len(left_stack) == self.capacity:
                self._remove_from_non_max_stacks(left_stack_index)

    def _rollback_current_stack(self):
        if not self.stacks:
            return
        elif not self.stacks[-1]:
            self._remove_from_non_max_stacks(len(self.stacks) - 1)
            self.stacks.pop()
            # if (len(self.stacks) - 1) in self.non_max_stacks:
            #     self.non_max_stacks.remove(len(self.non_max_stacks))
            self._rollback_current_stack()
        else:
            self.current_stack = self.stacks[-1]

    def pop(self) -> int:
        if not self.stacks:
            return -1
        if self.current_stack is None and self.stacks:
            self.current_stack = self.stacks[-1]
            if (len(self.stacks) - 1) in self.non_max_stacks:
                self.non_max_stacks.remove(len(self.stacks) - 1)
        value = self.current_stack.pop()
        if not self.current_stack:
            self._rollback_current_stack()

        return value

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) - 1:
            stack = self.stacks[index]
            if stack:
                value = self.stacks[index].pop()
                self.non_max_stacks.append(index)
                return value
            else:
                return -1
        elif index == len(self.stacks) - 1:
            # stack = self.stacks[index]
            # if stack:
            #     value = self.stacks[index].pop()
            #     self._rollback_current_stack()
            #     return value
            # else:
            #     return -1
            value = self.pop()
            if not self.current_stack and len(self.stacks[-1]) < self.capacity:
                self.current_stack = self.stacks[-1]
            return value
        else:
            return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

def test_func(commands, values, output=None):
    d_p = DinnerPlates(values[0][0])
    todo = None
    if output:
        todo = zip(commands, values, output)
    else:
        todo = zip(commands, values)
    for i in todo:
        if i[0] == "pop":
            value = d_p.pop()
            print(value)
        elif i[0] == 'push':
            d_p.push(i[1][0])
        elif i[0] == 'popAtStack':
            value = d_p.popAtStack(i[1][0])
            print(value)
        elif i[0] == 'DinnerPlates':
            pass
        else:
            print("error, unrecognised command")
        print(i, d_p.stacks, d_p.current_stack, d_p.non_max_stacks)


# # Input:
# t_commands = ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# t_values = [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# # Output:
# t_output = [None,None,None,None,None,None,2,None,None,20,21,5,4,3,1,-1]
#
#
# tc2 = ["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
# tv2 = [[2],[472],[106],[497],[498],[73],[115],[437],[461],[3],[3],[1],[3],[0],[2],[2],[1],[1],[3],[197],[239],[129],[449],[460],[240],[386],[343],[],[],[],[],[],[],[],[],[],[]]
#
# tc3 = ["DinnerPlates","push","push","push","popAtStack","pop","pop"]
# tv3 = [[1],[1],[2],[3],[1],[],[]]
# to3 = [None,None,None,None,2,3,1]
#
# test_func(tc3, tv3, output=to3)
#
# tc4 = ["DinnerPlates","push","push","popAtStack","pop","push","push","pop","pop"]
# tv4 = [[1],[1],[2],[1],[],[1],[2],[],[]]
# test_func(tc4, tv4)
#
# tc5 = ["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
# tv5 = [[2],[472],[106],[497],[498],[73],[115],[437],[461],[3],[3],[1],[3],[0],[2],[2],[1],[1],[3],[197],[239],[129],[449],[460],[240],[386],[343],[],[],[],[],[],[],[],[],[],[]]
# test_func(tc5, tv5)

def test_cap_1_pop_at_stack():
    d_p = DinnerPlates(1)
    d_p.stacks = [[1], [2]]
    d_p.popAtStack(1)
    assert d_p.stacks == [[1]]

def test_pop_at_current_stack():
    d_p = DinnerPlates(2)
    d_p.stacks = [[472], [497], [73]]
    d_p.current_stack = [73]
    d_p.non_max_stacks = [1, 0]
    d_p.popAtStack(2)
    assert d_p.current_stack == [497]
    assert d_p.non_max_stacks == [0]

test_pop_at_current_stack()

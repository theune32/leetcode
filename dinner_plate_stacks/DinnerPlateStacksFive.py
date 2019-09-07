class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.non_max_stacks = (
            []
        )  # contains the indices of all stacks not a max capacity except the current one
        self.stacks = []  # list of all stacks, last stack can not be empty
        self.current_stack = None  # rightmost stack that is not empty

    def _check_stack(self, index):
        # determines the stack with provided index, and cleans up metadata
        # also checks if last stacks are empty and removes them
        if index == len(self.stacks) - 1:
            self._check_current_stack()
        else:
            if len(self.stacks[index]) < self.capacity:
                self.non_max_stacks.append(index)
            elif len(self.stacks[index]) == self.capacity:
                self._check_index(index)

    def _check_current_stack(self):
        # check if the current stack is an empty list, remove it and check last stack
        curr_length = len(self.stacks)
        if self.current_stack:
            if len(self.current_stack) == self.capacity:
                self.current_stack = None
        else:
            # current stack is empty
            # check if there are still stacks
            # remove the empty stack from stacks
            # and change current stack to the last check, check again
            if curr_length > 1:
                self.stacks.pop()
                self.current_stack = self.stacks[-1]
                self._check_index(curr_length - 2)
                self._check_current_stack()
            elif curr_length == 1:
                self.stacks.pop()
                self.non_max_stacks = []

    def _check_index(self, index):
        if index in self.non_max_stacks:
            self.non_max_stacks = [x for x in self.non_max_stacks if x != index]

    def push(self, val: int) -> None:
        if self.non_max_stacks:
            index = min(self.non_max_stacks)
            self.stacks[index].append(val)
            self._check_stack(index)
        elif self.current_stack:
            self.current_stack.append(val)
            self._check_current_stack()
        else:
            new_stack = [val]
            self.stacks.append(new_stack)
            self.current_stack = self.stacks[-1]
            self._check_current_stack()

    def pop(self) -> int:
        if self.current_stack:
            value = self.current_stack.pop()
            self._check_current_stack()
        elif not self.stacks:
            return -1
        else:
            index = len(self.stacks) - 1
            self.current_stack = self.stacks[-1]
            self._check_index(index)
            value = self.current_stack.pop()
            self._check_current_stack()
        return value

    def popAtStack(self, index: int) -> int:
        curr_length = len(self.stacks)
        if index == curr_length - 1:
            return self.pop()
        elif index >= curr_length:
            return -1
        stack = self.stacks[index]
        if not stack:
            return -1
        value = stack.pop()
        self._check_stack(index)
        return value


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
        elif i[0] == "push":
            d_p.push(i[1][0])
        elif i[0] == "popAtStack":
            value = d_p.popAtStack(i[1][0])
            print(value)
        elif i[0] == "DinnerPlates":
            pass
        else:
            print("error, unrecognised command")
        print(i, d_p.stacks, d_p.current_stack, d_p.non_max_stacks)


# # Input:
# t_commands = ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# t_values = [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# # Output:
# t_output = [None,None,None,None,None,None,2,None,None,20,21,5,4,3,1,-1]
# test_func(t_commands, t_values, t_output)
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

# test_pop_at_current_stack()

from copy import deepcopy


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.non_max_stacks_index = []
        self.current_stack = []
        self.stacks = []

    def clean_stacks(self):
        if not self.stacks[-1]:
            self.stacks.pop()

    def push(self, val: int) -> None:
        if self.non_max_stacks_index:
            # fix append vs index searching
            min_index = min(self.non_max_stacks_index)
            stack = self.stacks[min_index]
            stack.append(val)
            if len(stack) == self.capacity:
                self.non_max_stacks_index.remove(min_index)
        else:
            self.current_stack.append(val)
            if len(self.current_stack) == 1:
                self.stacks.append(deepcopy(self.current_stack))
            if len(self.current_stack) == self.capacity:
                self.current_stack = []

    def pop(self) -> int:
        if not self.stacks or self.stacks == [[]]:
            return -1
        else:
            if self.current_stack:
                value = self.current_stack.pop()
                if not self.current_stack:
                    self.stacks.pop()
                return value
            else:
                self.current_stack = self.stacks.pop()
                self.non_max_stacks_index.append(len(self.stacks) - 1)
                return self.current_stack.pop()

    def popAtStack(self, index: int) -> int:
        length_stacks = len(self.stacks)
        if index < length_stacks - 1:
            stack = self.stacks[index]
            if stack:
                value = stack.pop()
                if index not in self.non_max_stacks_index:
                    self.non_max_stacks_index.append(index)
                return value
            else:
                return -1
        elif index == length_stacks - 1:
            value = self.stacks[index].pop()
            self.clean_stacks()
            return value
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
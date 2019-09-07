from dinner_plate_stacks.DinnerPlateStacks import DinnerPlates


def test_pop_push_two():
    dp = DinnerPlates(2)
    dp.stacks = [[1, 2], [3, 4]]
    assert dp.pop() == 4
    dp.push(20)
    assert dp.pop() == 20
    dp.push(23)
    dp.push(24)
    assert dp.stacks == [[1, 2], [3, 23], [24]]
    assert dp.current_stack == [24]

def test_pop_push_one():
    dp = DinnerPlates(1)
    dp.push(1)
    dp.push(2)
    dp.push(3)
    assert dp.pop() == 3
    assert dp.pop() == 2
    assert dp.pop() == 1
    assert dp.pop() == -1

def test_non_max_stack():
    dp = DinnerPlates(2)
    dp.stacks = [[1, 2], [3], [5, 6]]
    dp.non_max_stacks = [1]
    dp.push(4)
    assert dp.stacks == [[1, 2], [3, 4], [5, 6]]
    assert dp.non_max_stacks == []

def test_pop_at_stack():
    dp = DinnerPlates(2)
    dp.push(1)
    dp.push(2)
    dp.push(3)
    dp.push(4)
    dp.push(5)
    dp.push(6)
    assert dp.stacks == [[1, 2], [3, 4], [5, 6]]
    assert dp.pop() == 6
    assert dp.current_stack == [5]
    assert dp.popAtStack(1) == 4
    assert dp.popAtStack(1) == 3
    assert dp.popAtStack(1) == -1
    assert dp.pop() == 5
    assert dp.stacks == [[1, 2]]


# test_non_max_stack()
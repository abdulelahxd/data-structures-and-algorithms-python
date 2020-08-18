from data_structures_and_algorithms.challenges.array_shift.array_shift import (
    insertShiftArray
)

def test_one():
    actual = insertShiftArray([2,4,6,8], 5)
    expected = [2,4,5,6,8]
    assert actual == expected


def test_two():
    actual = insertShiftArray([4,8,15,23,42], 16)
    expected = [4,8,15,16,23,42]
    assert actual == expected


def test_three():
    actual = insertShiftArray([1,2,8,4,9,6,], 7)
    expected = [1,2,4,6,7,8,9]
    assert actual == expected
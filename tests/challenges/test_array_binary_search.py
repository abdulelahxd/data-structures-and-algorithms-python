from data_structures_and_algorithms.challenges.BinarySearch.array_binary_search import BinarySearch

def test_one():
    actual = BinarySearch([4,8,15,16,23,42],15)
    expected = 2
    assert expected == actual
    
def test_one():
    actual = BinarySearch([11,22,33,44,55,66,77],90)
    expected = -1
    assert expected == actual
    
def test_one():
    actual = BinarySearch([11,22,26,33,44,55,66,77],26)
    expected = 2
    assert expected == actual
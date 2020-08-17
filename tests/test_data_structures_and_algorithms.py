from data_structures_and_algorithms import __version__


def test_version():
    assert __version__ == "0.1.0"

def reverse_numbers():
    array = reverse_array([1,2,3,4,5,6])
    
    excepted = [6,5,4,3,2,1]
    assert array == excepted
    
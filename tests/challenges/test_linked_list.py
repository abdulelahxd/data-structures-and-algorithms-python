from data_structures_and_algorithms.challenges.linked_list.linked_list import (
    LinkedList,
)
linked_list_let = LinkedList()
linked_list_let.insert(3)
linked_list_let.insert(6)
linked_list_let.insert(9)
def test_instance():
    assert isinstance(linked_list_let, LinkedList)
def test_insert():
    result = ''
    linked_list = linked_list_let.head
    while linked_list:
        result += f'{linked_list.value},'
        linked_list = linked_list.next
    assert result == '3,6,9,'
def test_head():
    assert linked_list_let.head.value == 3
def test_finding_notExist_value():
    assert linked_list_let.includes(5) == False
def test_finding_exist_value():
    assert linked_list_let.includes(6) == True
def test_string_str():
    assert linked_list_let.toString() == '{3} -> {6} -> {9} -> NULL'
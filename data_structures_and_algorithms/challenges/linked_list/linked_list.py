class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList():
    """
    Put docstring here
    """
    def __init__(self):
        self.head = None
    def insert(self, value):
        node_let = Node(value)
        if not self.head:
            self.head = node_let
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_let
    def includes(self,number):
        current = self.head
        while current:
            if current.value == number:
                return True
            current = current.next
        return False
    def toString(self):
        result = ""
        current = self.head
        while current:
            result += f'{ {current.value} } -> '
            current = current.next
        result += 'NULL'
        return result


if __name__ == '__main__':
    main_func = LinkedList()
    main_func.insert(3)
    main_func.insert(6)
    main_func.insert(9)
    print(main_func.includes(5))
    print(main_func.toString())
    empty = LinkedList()
    print(empty.toString())
    print(main_func.head.value)
class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"linked list : {self.head}"

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += f"{{ {str(current.value)} }} -> "
            current = current.next
        return res + "NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next #if current is not the value look next
        return False

    def append(self, value):
        current = self.head
        while current:
            if current.next == None: #if there is no next it is the tail
                current.next = Node(value)
                break
            current = current.next

    def insert_before(self, value, newVal):
        current = self.head
        while current:
            if current.next == None:
                return 'Value not in linked list'
            if current.next.value == value: 
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def insert_after(self, value, newVal):
        current = self.head
        while current:
            if current.next == None:
                return 'Value not in linked list'
            if current.value == value:
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def kth_from_end(self, k):
        current = self.head
        arr = []
        if k < 0:
            raise ValueError("value must be positive")
        while current:
            arr.append(current)
            current = current.next

        if len(arr) < k:
            raise IndexError("Value extends length of List.")

        arr.reverse()

        if k == len(arr):
            k = k - 1
        return arr[k].value

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"
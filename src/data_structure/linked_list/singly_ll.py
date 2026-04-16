from typing import Any, List

class Node:
    '''
    Represents a single node in Linked List.
    Attributes:
        data(type will be decided during assignment): value stored in Node
        next(Node): Reference to next Node
    '''
    def __init__(self, value):
        self.data = value
        self.next = None


class SinglyLL():
    """
    Robust Implementation of Singly Linked List
    Attributes:
        head : Reference to first Node of Singly Linked List
    Features defined: 
    -> Insertion (start, end, at some position)
    -> Deletion (start, end, at some position)
    -> Delete a node
    -> Delete linked list
    -> Print Linked List
    -> length of Linked List
    -> Conversion to python list
    -> Search value at some position
    -> Search position for some value
    -> Reverse the linked List
    """
    def __init__(self) -> None:
        """Initiallize an empty list"""
        self.head = None

    def insert_at_start(self, value) -> None:
        """Insert the node at start of linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value) -> None:
        """Insert the node at the end of linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        crr = self.head
        while crr.next:
            crr = crr.next
        crr.next = new_node

    def insert_at_postion(self, pos, value) -> None:
        """Insert the node at given position"""
        if not isinstance(pos, int):
            raise TypeError("Index should be integer")
        if pos < 1:
            raise IndexError("Index should not be lesser than 1")
        if pos == 1:
            self.insert_at_start(value)
            return
        if self.head is None:
            raise ValueError("Empty list and pos is not first")
        new_node = Node(value)
        crr = self.head
        for _ in range(1, pos-1):
            if crr.next is None:
                raise IndexError("Index should be within boundaries (< length)")
            crr = crr.next
        if crr.next is None:
            crr.next = new_node
            return
        new_node.next = crr.next
        crr.next = new_node

    def delete_at_start(self) -> None:
        """Delete the starting node of linked list"""
        if self.head is None:
            raise ValueError("Empty List")
        self.head = self.head.next

    def delete_at_end(self) -> None:
        """Delete the end node of linked list"""
        if self.head is None:
            raise ValueError("Empty List")
        if self.head.next is None:
            self.head = None
            return
        crr = self.head
        while crr.next.next:
            crr = crr.next
        crr.next = None

    def delete_at_position(self, pos) -> None:
        """Delete the node at given position"""
        if not isinstance(pos, int):
            raise TypeError("Index should be in int")
        if pos < 1:
            raise IndexError("Index should be >= 1")
        if pos == 1:
            self.delete_at_start()
            return
        if self.head is None:
            raise ValueError("Empty list")
        crr = self.head
        prev = None
        for _ in range(1, pos):
            if crr is None:
                raise IndexError("Index is out of bound")
            prev = crr
            crr = crr.next
        if crr is None:
            raise IndexError("Out of bound")
        prev.next = crr.next

    def delete_node(self, value) -> None:
        """Delete the node with given value"""
        if self.head is None:
            raise ValueError("Empty List")
        if self.head.data == value:
            self.head = self.head.next
            return
        crr = self.head
        prev = None
        while crr:
            if crr.data == value:
                prev.next = crr.next
                return
            prev = crr
            crr = crr.next
        raise ValueError("Value not found")

    def delete_list(self) -> None:
        """Delete the linked list"""
        if self.head is None:
            raise ValueError("List is already Empty")
        self.head = None

    def print_sll(self) -> None:
        """Print the linked list"""
        if self.head is None:
            print("Empty list")
        crr = self.head
        while crr.next:
            print(crr.data,end =  " -> ")
            crr = crr.next
        print(crr.data)

    def length_sll(self) -> int:
        """Return the length of linked list"""
        count = 0
        crr = self.head
        while crr:
            crr = crr.next
            count+= 1
        return count

    def to_list(self) -> List[Any]:
        """Return the python list converted from linked list"""
        crr = self.head
        lst = []
        while crr:
            lst.append(crr.data)
            crr = crr.next
        return lst

    def __str__(self):
        return " -> ".join(map(str, self.to_list()))

    def search_at_pos(self, pos) -> Any:
        """Return the value at given position"""
        if self.head is None:
            raise ValueError("Empty list")
        if not isinstance(pos, int):
            raise TypeError("Index should be in int")
        if pos < 1:
            raise IndexError("Index should be >= 1")
        crr = self.head
        for _ in range(1, pos):
            if crr is None:
                raise IndexError("Index is out of bound")
            crr = crr.next
        return crr.data

    def search_node(self, value) -> int:
        """Return the position of the given node"""
        if self.head is None:
            raise ValueError("Empty list")
        crr = self.head
        cnt = 1
        while crr:
            if crr.data == value:
                return cnt
            crr = crr.next
            cnt+=1
        raise ValueError("Value not found")

    def reverse(self) -> None:
        """Reverse the given linked list"""
        if self.head is None or self.head.next is None:
            return
        prev = None
        crr = self.head
        while crr:
            nxt = crr.next
            crr.next = prev
            prev = crr
            crr = nxt
        self.head = prev

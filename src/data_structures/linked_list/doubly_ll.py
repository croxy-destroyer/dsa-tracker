from typing import Any, List

class Node:
    """
    Represents a single Node in doubly linked list.
    Attributes:
        data: value contained by Node
        next: reference to next Node
        prev: reference to prev Node
    """
    def __init__(self, value: Any):
        self.data = value
        self.prev = None
        self.next = None


class DoublyLL:
    """
    Robust Implementation of doubly linked list.
    Attributes:
        head: reference to first node of dll
    Features:
    -> Insertion: insert a node in dll at start , at end, at some position
    -> Deletion: Delete a node in dll at start, at end, at some position 
    -> Delete a node by value 
    -> Delete the linked list
    -> Utilities: print the list, conversion to python list, length of dll
    -> Searching: Search the node at position p, or search the node with value v
    -> Reverse: Reverse the linked list
    """
    def __init__(self):
        self.head = None
    
    # INSERTION #
    
    def insert_at_start(self, value: Any) -> None:
        """Insert the node at start of DLL"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, value: Any) -> None:
        """Insert the node at end of DLL"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        crr = self.head
        while crr.next:
            crr = crr.next
        crr.next = new_node
        new_node.prev = crr
    
    # Utilities #

    def to_list(self) -> List[Any]:
        """Conversion of linked list to python list"""
        lst = []
        crr = self.head
        while crr:
            lst.append(crr.data)
            crr = crr.next
        return lst
    

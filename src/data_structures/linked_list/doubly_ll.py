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
    
    def insert_at_position(self, pos, value: Any) -> None:
        """Insert node at given position in DLL"""
        if not isinstance(pos, int):
            raise TypeError("Index should be of type int")
        if pos < 1:
            raise IndexError("Index should be >=1")
        if pos == 1:
            self.insert_at_start(value)
            return
        if self.head is None:
            raise ValueError("Empty list and pos is not one")
        
        new_node = Node(value)
        crr = self.head
        for i in range(pos-2):
            if crr.next is None: # important checkpoint for future ref
                raise IndexError("Index is out of bound should be < (length +1)")
            crr = crr.next
        new_node.next = crr.next
        new_node.prev = crr
        if crr.next:
            crr.next.prev = new_node
        crr.next = new_node

                                # Deletion #
    
    def delete_at_start(self) -> None:
        """Delete the starting node of DLL"""
        if self.head is None:
            raise ValueError("Empty List")
        if self.head.next is None:
            self.head = None
            return
        
        self.head = self.head.next
        self.head.prev = None
    
    def delete_at_end(self) -> None:
        """Delete the end node of DLL"""
        if self.head is None:
            raise ValueError("Empty List")
        if self.head.next is None:
            self.head = None
            return
        
        crr = self.head
        while crr.next:
            crr = crr.next
        crr.prev.next = None
    
    def delete_at_position(self, pos) -> None:
        """Delete the node at given position"""
        if not isinstance(pos, int):
            raise TypeError("Index should be of type int")
        if pos < 1:
            raise IndexError("Index should be >=1")
        if self.head is None:
            raise ValueError("Empty List")
        if pos == 1:
            self.delete_at_start()
            return
        crr = self.head
        for i in range(pos - 1):
            if crr.next is None:
                raise IndexError("Index is out of bound should be < length")
            crr = crr.next
        # if crr is None:
        #     raise IndexError("Index is out of bound should be < length")
        if crr.next:
            crr.next.prev = crr.prev
        if crr.prev:
            crr.prev.next = crr.next
    
    def delete_node(self, value) -> None:
        """Delete node from DLL"""
        if self.head is None:
            raise ValueError("Empty list")
        crr = self.head
        while crr:
            if crr.data == value:
                if crr.prev:
                    crr.prev.next = crr.next
                else:
                    self.head = crr.next
                if crr.next:
                    crr.next.prev = crr.prev
                return
            crr = crr.next
        raise ValueError("Value not found")
    
    def delete_list(self) -> None:
        """Delete the entire list """
        if self.head is None:
            raise ValueError("Empty List")
        self.head = None

                                        # Utilities #

    def to_list(self) -> List[Any]:
        """Conversion of linked list to python list"""
        lst = []
        crr = self.head
        while crr:
            lst.append(crr.data)
            crr = crr.next
        return lst

    def __str__(self) -> str:
        """return the linked list joined with dual side arrows """
        return " <-> ".join(map(str, self.to_list()))
    
    def length(self) -> int:
        """Return the length of linked list"""
        count = 0
        crr = self.head
        while crr:
            count+= 1
            crr = crr.next
        return count

    def search_node(self, value) -> int:
        """Return the position of given node"""
        crr = self.head
        p = 1
        while crr:
            if crr.data == value:
                return p
            crr = crr.next
            p+= 1
        raise ValueError("Value not found")
    
    def search_at_position(self, pos) -> Any:
        """Return the value of node at given position"""
        if not isinstance(pos, int):
            raise TypeError("Index should be of type int")
        if pos < 1:
            raise IndexError("Index should be >=1")
        if self.head is None:
            raise ValueError("Empty List")
        crr = self.head 
        for i in range(pos - 1):
            if crr is None:
                raise IndexError("Index is out of bound should be < (length)")
            crr = crr.next
        
        return crr.data
    
    def reverse(self) -> None:
        """Reverse the linked list"""
        if self.head is None:
            return
        
        crr = self.head
        prev_node = None
        while crr:
            crr.prev, crr.next = crr.next, crr.prev
            prev_node = crr
            crr = crr.prev
        self.head = prev_node
    
    def traverse_backward(self) -> List[Any]:
        if self.head is None:
            return []
        crr = self.head
        while crr.next:
            crr = crr.next
        
        result = []
        while crr:
            result.append(crr.data)
            crr = crr.prev
        
        return result


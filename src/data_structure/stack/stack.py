from typing import Any, List


class Node:
    """
    Represents a single node in the Stack.
    Attributes:
        data : value stored in the node
        next : reference to the node below it in the stack
    """
    def __init__(self, value: Any) -> None:
        self.data = value
        self.next = None


class Stack:
    """
    Robust implementation of Stack using Linked List (LIFO).
    Attributes:
        top   : reference to the top node of the stack
        _size : number of elements in the stack
    Features:
    -> Push         : push element onto stack
    -> Pop          : pop element from stack
    -> Peek         : view top element without removing
    -> is_empty     : check if stack is empty
    -> size/len     : number of elements
    -> clear        : empty the entire stack
    -> search       : check if a value exists / find its depth
    -> to_list      : convert stack to python list (top → bottom)
    -> min / max    : minimum and maximum element in stack
    -> __str__      : human readable string representation
    """

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self.top= None
        self._size= 0

    #               CORE OPERATIONS

    def push(self, value: Any) -> None:
        """Push a new element onto the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self) -> Any:
        """
        Remove and return the top element.
        Raises:
            IndexError: if stack is empty (Stack Underflow)
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: cannot pop from an empty stack")
        value = self.top.data
        self.top = self.top.next
        self._size -= 1
        return value

    def peek(self) -> Any:
        """
        Return the top element without removing it.
        Raises:
            IndexError: if stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.data

    #               STATE CHECKS

    def is_empty(self) -> bool:
        """Return True if the stack has no elements."""
        return self.top is None

    def size(self) -> int:
        """Return the number of elements in the stack."""
        return self._size

    def __len__(self) -> int:
        """Support len(stack)."""
        return self._size

    #               UTILITIES

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        Raises:
            IndexError: if stack is already empty
        """
        if self.is_empty():
            raise IndexError("Stack is already empty")
        self.top = None
        self._size = 0

    def to_list(self) -> List[Any]:
        """Return a python list of elements from top to bottom."""
        result = []
        crr = self.top
        while crr:
            result.append(crr.data)
            crr = crr.next
        return result

    def search(self, value: Any) -> int:
        """
        Return the 1-based depth of the value from the top.
        (top element has depth 1)
        Raises:
            ValueError: if value is not found in the stack
        """
        depth = 1
        crr = self.top
        while crr:
            if crr.data == value:
                return depth
            crr = crr.next
            depth += 1
        raise ValueError(f"{value} not found in stack")

    def min(self) -> Any:
        """
        Return the minimum value in the stack.
        Raises:
            IndexError: if stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        crr = self.top
        minimum = crr.data
        while crr:
            if crr.data < minimum:
                minimum = crr.data
            crr = crr.next
        return minimum

    def max(self) -> Any:
        """
        Return the maximum value in the stack.
        Raises:
            IndexError: if stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        crr = self.top
        maximum = crr.data
        while crr:
            if crr.data > maximum:
                maximum = crr.data
            crr = crr.next
        return maximum

    def __str__(self) -> str:
        """Human readable: TOP → [4, 3, 2, 1] → BOTTOM"""
        if self.is_empty():
            return "Stack: empty"
        return "TOP → [" + ", ".join(map(str, self.to_list())) + "] → BOTTOM"

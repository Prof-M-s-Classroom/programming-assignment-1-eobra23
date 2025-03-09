from distance import Distance

class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    def __init__(self, capacity = 5):
        """Initialize the stack with an empty state."""
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.rear = None

    def push(self, reading):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_distance = Distance(reading)
        new_node = Node(new_distance)

        if self.size == 0:
            self.top = new_node
            self.rear = new_node
            self.rear.next = self.top #Circular stack
        elif self.size < self.capacity:
            self.top.next = new_node
            self.top = new_node
            self.top.next = self.rear #Maintains circularity
        else:
            self.rear = self.rear.next
            self.top.next = new_node
            new_node.next = self.rear
            self.top = new_node

        if self.size < self.capacity:
            self.size += 1

    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.size == 0:
            return None

        removed_data = self.rear.data #Save data before removing

        if self.size == 1: #One element in stack
            self.rear = None
            self.top = None
        else:
            self.rear = self.rear.next
            self.top.next = self.rear

        self.size -=1
        return removed_data #Remove popped data

    def peek(self):
        """Return the most recent temperature entry without removing it."""
        if self.top is None:
            raise IndexError("Circular stack is empty")
        return self.top.data

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.size == 0:
            print("Stack is empty")
            return
        iterator = self.rear
        for _ in range(self.size):
            print(iterator.data.__str__())
            iterator = iterator.next

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.top is None

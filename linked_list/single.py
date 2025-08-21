"""
==============================
Single Linked List (SLL) in Python
==============================

What is a Linked List?
    A Linked List is a linear data structure where elements (nodes) are connected using pointers/references.

    Each node contains:
        Data (the actual value)
        Pointer/Reference to the next node (and sometimes the previous node in doubly linked list).

How it Works?
    Unlike arrays, linked list elements are not stored in contiguous memory.
    You access nodes by traversing from the head (start) one by one.
    Example: Head → Node1 → Node2 → Node3 → NULL

How it Solves Array Problems?
Arrays have some drawbacks → Linked List fixes some:
    Dynamic Size
        Array: Fixed size (need resizing if full).
        Linked List: Can grow/shrink easily since memory is allocated per node.

    Insert/Delete Efficiency
        Array: Inserting in middle = shift elements (O(n)).
        Linked List: Just update pointers (O(1) if you have the reference).

    Memory Utilization
        Array: May waste space (allocated upfront).
        Linked List: Uses only what is needed (but extra memory for pointers).

Big-O Analysis (Array vs Linked List)
    Access (Random Read)
        Array → O(1) → Direct index lookup.
        Linked List → O(n) → Must traverse from head.

    Search (Unsorted)

        Array → O(n) → Linear scan.

        Linked List → O(n) → Traverse nodes one by one.

    Insert

    At Front
        Array → O(n) (shift all elements).
        Linked List → O(1) (just update head pointer).

    At End
        Array → O(1) amortized (dynamic resize can make it O(n) occasionally).
        Linked List → O(n) (unless tail pointer is kept → then O(1)).

    In Middle
        Array → O(n) (shift elements).
        Linked List → O(1) if reference to node is known, else O(n) to find it.

    Delete

    At Front
        Array → O(n) (shift elements).
        Linked List → O(1) (move head).

    At End
        Array → O(1).
        Linked List → O(n) (singly, unless doubly with tail → O(1)).

    In Middle
        Array → O(n) (shift).
        Linked List → O(1) if reference given, else O(n) to locate.

    Quick takeaway:
        Use Array when you need fast access.
        Use Linked List when you need fast insert/delete, especially at the front.

"""


class Node:
    # This defines a class named 'Node'
    # A Node is the basic building block of a Linked List.

    def __init__(self, data, next=None):
        # __init__ is the constructor method that runs when you create a new Node object.
        # 'data' is the value stored in the node.
        # 'next' is a reference (or pointer) to the next Node in the linked list.
        # By default, 'next=None' means the node doesn't point to anything yet (i.e., it's the last node for now).

        self.data = data
        # Store the actual data value inside this Node instance.
        # Example: If data=10, then this node holds the value 10.

        self.next = next
        # Store the reference to the next Node.
        # If next=None → this is the last node.
        # Otherwise, it points to another Node object.


# Define LinkedList class
class LinkedList:
    def __init__(self):
        # Initialize LinkedList with empty head (no elements yet)
        self.head = None

    def insert_at_beg(self, value):
        # Insert a new node at the beginning of the list
        node = Node(data=value, next=self.head)  # New node points to current head
        self.head = node  # Update head to the new node
        return

    def insert_at_end(self, value):
        # Insert a new node at the end of the list
        if self.head is None:
            # If list is empty, new node becomes the head
            self.head = Node(data=value)
            return

        # Otherwise, get the last node
        prev, last_el = self.get_last()
        last_el.next = Node(data=value)  # Attach new node at the end
        return

    def insert_at_position(self, pos, value):
        # Insert a node at a specific position (0-indexed)
        count = 0
        itr = self.head

        # Traverse until we reach desired position
        while count != pos:
            itr = itr.next
            count += 1

        # Create new node, point it to current 'next', and link it
        itr.next = Node(data=value, next=itr.next)
        return

    def delete(self):
        # Delete the last node in the list
        prev, last = self.get_last()  # Get second last and last node
        prev.next = None  # Remove link to last node (garbage collected)
        return

    def delete_at_position(self, pos):
        # Delete node at specific position
        count = 0
        itr = self.head

        # Traverse until the node BEFORE the one we want to delete
        while count + 1 != pos:
            itr = itr.next
            count += 1

        # If data is invalid, just return
        if not itr.data:
            return

        # Skip the target node (unlink it from the list)
        itr.next = itr.next.next if itr.next else None
        return

    def length(self):
        # Count the number of nodes in the list
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def get_last(self):
        # Get last node and the one before it
        prev, itr = None, self.head

        # Traverse until the last node
        while itr.next:
            prev = itr
            itr = itr.next

        return prev, itr

    def is_empty(self):
        # Return True if list is empty
        return True if self.head == None else False

    def search(self, value):
        # Search for a value and return its index if found, else -1
        itr = self.head
        index = 0

        while itr:
            if itr.data == value:
                return index  # Return index if found
            index += 1
            itr = itr.next
        return -1

    def display(self):
        # Print the linked list elements in order
        ll = ""
        itr = self.head

        while itr:
            ll += f"{itr.data} --> "
            itr = itr.next

        print(ll)

    # Make LinkedList iterable (so we can use 'for x in ll')
    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data  # Yield one value at a time
            itr = itr.next

    # Define __len__ (so we can use 'len(ll)')
    def __len__(self):
        return self.length()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(45)  # LinkedList: 45
    ll.insert_at_end(55)  # LinkedList: 45 -> 55
    ll.insert_at_end(85)  # LinkedList: 45 -> 55 -> 85
    ll.insert_at_beg(21)  # LinkedList: 21 -> 45 -> 55 -> 85
    ll.insert_at_position(2, 77)  # LinkedList: 21 -> 45 -> 77 -> 55 -> 85
    ll.display()

    ll.delete()  # Delete last node → removes 85
    ll.delete_at_position(2)  # Delete node at index 2 (77 removed)
    print("linked list length", ll.length())  # Count nodes
    print("is linked list empty", ll.is_empty())  # False
    print("target found at index --> ", ll.search(55))  # Should return index of 55
    ll.display()

    # Iterating with __iter__
    for value in ll:
        print("iterated value:", value)

    # Using len() thanks to __len__
    print("Length using len():", len(ll))

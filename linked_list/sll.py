"""
==============================
Single Linked List (SLL) in Python
==============================

What is a Linked List?
    A Linked List is a linear data structure where elements (nodes) are connected using pointers/references.

    Each node contains:
        - Data (the actual value)
        - Pointer/Reference to the next node (and sometimes the previous node in doubly linked list).

How it Works?
    Unlike arrays, linked list elements are not stored in contiguous memory.
    You access nodes by traversing from the head (start) one by one.
    Example: Head → Node1 → Node2 → Node3 → NULL

How it Solves Array Problems?
Arrays have some drawbacks → Linked List fixes some:
    - Dynamic Size
        Array: Fixed size (need resizing if full).
        Linked List: Can grow/shrink easily since memory is allocated per node.

    - Insert/Delete Efficiency
        Array: Inserting in middle = shift elements (O(n)).
        Linked List: Just update pointers (O(1) if you have the reference).

    - Memory Utilization
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
    - Use Array when you need fast access.
    - Use Linked List when you need fast insert/delete, especially at the front.

"""


# ===============================
# Node Class
# ===============================
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


# ===============================
# Singly Linked List Class
# ===============================
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list (head points to nothing)

    # ---------------------------------
    # Insert node at the beginning (O(1))
    # ---------------------------------
    def insert_at_beg(self, value):
        node = Node(data=value, next=self.head)  # New node points to current head
        self.head = node  # Update head to new node
        return

    # ---------------------------------
    # Insert node at the end (O(n))
    # ---------------------------------
    def insert_at_end(self, value):
        if self.head is None:  # Case 1: Empty list
            self.head = Node(data=value)  # New node becomes head
            return

        prev, last_el = self.get_last()  # Case 2: Find last node
        last_el.next = Node(data=value)  # Attach new node after last
        return

    # ---------------------------------
    # Insert node at a specific position (0-indexed) (O(n))
    # ---------------------------------
    def insert_at_position(self, pos, value):
        count = 0
        itr = self.head

        # Traverse until reaching the desired position
        while count != pos:
            itr = itr.next
            count += 1

        # Insert new node: point it to current next, and link in chain
        itr.next = Node(data=value, next=itr.next)
        return

    # ---------------------------------
    # Delete the last node (O(n))
    # ---------------------------------
    def delete(self):
        prev, last = self.get_last()  # Get 2nd last and last node
        prev.next = None  # Remove last node by unlinking it
        return

    # ---------------------------------
    # Delete node at a specific position (O(n))
    # ---------------------------------
    def delete_at_position(self, pos):
        count = 0
        itr = self.head

        # Traverse until reaching the node BEFORE target position
        while count + 1 != pos:
            itr = itr.next
            count += 1

        if not itr.data:  # If invalid node, do nothing
            return

        # Skip target node (unlink from chain)
        itr.next = itr.next.next if itr.next else None
        return

    # ---------------------------------
    # Count number of nodes (O(n))
    # ---------------------------------
    def length(self):
        count = 0
        itr = self.head
        while itr:  # Traverse list until end
            count += 1
            itr = itr.next
        return count

    # ---------------------------------
    # Get last node and its previous node (O(n))
    # ---------------------------------
    def get_last(self):
        prev, itr = None, self.head
        while itr.next:  # Traverse until reaching last node
            prev = itr
            itr = itr.next
        return prev, itr

    # ---------------------------------
    # Check if list is empty (O(1))
    # ---------------------------------
    def is_empty(self):
        return True if self.head is None else False

    # ---------------------------------
    # Search for value and return index (O(n))
    # ---------------------------------
    def search(self, value):
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:  # Value found
                return index
            index += 1
            itr = itr.next
        return -1  # Not found

    # ---------------------------------
    # Display linked list (O(n))
    # ---------------------------------
    def display(self):
        ll = ""
        itr = self.head
        while itr:
            ll += f"{itr.data} --> "  # Collect nodes into string
            itr = itr.next
        print(ll)

    # ---------------------------------
    # Make LinkedList iterable (support for `for x in ll`)
    # ---------------------------------
    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data  # Yield one value at a time
            itr = itr.next

    # ---------------------------------
    # Support len() function (O(n))
    # ---------------------------------
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
    ll.delete_at_position(2)  # Delete node at index 2 → removes 77
    print("linked list length", ll.length())  # Count nodes
    print("is linked list empty", ll.is_empty())  # False
    print("target found at index --> ", ll.search(55))  # Should return index of 55
    ll.display()

    # Iterating with __iter__
    for value in ll:
        print("iterated value:", value)

    # Using len() thanks to __len__
    print("Length using len():", len(ll))

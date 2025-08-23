"""
==============================
Doubly Linked List (DLL) in Python
==============================

What is a Linked List?
----------------------
A Linked List is a linear data structure where elements (nodes) are connected using pointers/references.

In a Doubly Linked List (DLL):
    • Each node contains:
        - Data (the actual value)
        - Pointer to the next node
        - Pointer to the previous node
    • Traversal is possible in both directions (forward & backward).
    • Example:
        NULL ← Head ↔ Node1 ↔ Node2 ↔ Node3 → NULL

How it Works?
-------------
Unlike arrays, linked list elements are NOT stored in contiguous memory.
You must traverse from the head (start) node one by one.

How it Solves Array Problems?
-----------------------------
Arrays have some drawbacks → Linked Lists solve some of them:

1. Dynamic Size
   - Array: Fixed size (requires resizing).
   - Linked List: Grows/shrinks easily (memory per node).

2. Insert/Delete Efficiency
   - Array: Inserting/deleting in the middle = O(n) (shift elements).
   - Linked List: Update pointers = O(1) if you already have reference.

3. Memory Utilization
   - Array: May waste space (pre-allocated).
   - Linked List: Uses memory as needed (but needs extra pointers).

Big-O Analysis (Array vs Doubly Linked List)
--------------------------------------------
Operation        Array               Doubly Linked List
--------------------------------------------------------
Access           O(1)                O(n)
Search           O(n)                O(n)
Insert at Front  O(n)                O(1)
Insert at End    O(1) amortized      O(1) (with tail)
Insert Middle    O(n)                O(1) if ref, O(n) otherwise
Delete at Front  O(n)                O(1)
Delete at End    O(1)                O(1) (with tail)
Delete Middle    O(n)                O(1) if ref, O(n) otherwise

Quick takeaway:
---------------
• Use Array if you need fast random access (indexing).
• Use Linked List if you need frequent insert/delete at front/back
  or backward traversal.
"""


# ===============================
# Node class
# ===============================
class Node:
    # A Node represents one element in a Doubly Linked List (DLL).

    def __init__(self, data, next=None, prev=None):
        # Initialize a node with:
        # data = the value of the node
        # next = reference to the next node
        # prev = reference to the previous node

        self.data = data
        # Store the actual data value in the node

        self.next = next
        # Pointer to the next node (default None)

        self.prev = prev
        # Pointer to the previous node (default None)


# ===============================
# Doubly Linked List class
# ===============================
class LinkedList:
    def __init__(self):
        # Initialize empty DLL
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list

    # Insert at beginning
    def insert_at_beg(self, value):
        node = Node(data=value)  # Create new node
        if self.head:  # If list not empty
            node.next = self.head  # New node points to current head
            self.head.prev = node  # Current head points back to new node
        else:  # If list empty
            self.tail = node  # Tail also becomes new node
        self.head = node  # Update head to new node
        return

    # Insert at end
    def insert_at_end(self, value):
        node = Node(data=value)  # Create new node
        if self.tail:  # If list not empty
            node.prev = self.tail  # New node points back to current tail
            self.tail.next = node  # Current tail points forward to new node
        else:  # If list empty
            self.head = node  # Head also becomes new node
        self.tail = node  # Update tail to new node
        return

    # Insert at a specific position (0-indexed)
    def insert_at_position(self, pos, value):
        count = 0
        itr = self.head  # Start from head
        while itr:
            if count + 1 == pos:  # Stop at node before position
                break
            itr = itr.next  # Move forward
            count += 1
        node = Node(data=value, next=itr.next, prev=itr)  # Create new node
        if itr.next:  # If not inserting at end
            itr.next.prev = node  # Next node points back to new node
        itr.next = node  # Current node points forward to new node
        return

    # Delete last node
    def delete(self):
        if not self.tail:  # Empty list
            return
        self.tail = self.tail.prev  # Move tail backward
        if self.tail:  # If list still not empty
            self.tail.next = None  # Remove forward pointer of new tail
        else:  # List became empty
            self.head = None
        return

    # Delete node at specific position
    def delete_at_position(self, pos):
        if pos == 0 and self.head:  # Delete head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == pos:
                # Remove itr from the list
                if itr.next:
                    itr.next.prev = itr.prev
                if itr.prev:
                    itr.prev.next = itr.next
                if itr == self.tail:
                    self.tail = itr.prev
                return
            itr = itr.next
            count += 1

    # Count nodes
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Check if list is empty
    def is_empty(self):
        return self.head is None

    # Search for value and return index
    def search(self, value):
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index += 1
        return -1

    # Display list (forward or backward)
    def display(self, is_backward=False):
        itr = self.head if not is_backward else self.tail
        dll = ""
        while itr:
            dll += f"{itr.data} --> "
            itr = itr.next if not is_backward else itr.prev
        print(dll)
        return

    # Iterator to use in loops
    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            itr = itr.next

    # Enable len() function
    def __len__(self):
        return self.length()


# ===============================
# Demo usage
# ===============================
if __name__ == "__main__":
    ll = LinkedList()
    print("is linked list empty", ll.is_empty())  # True

    # Insert nodes
    ll.insert_at_end(45)  # DLL: 45
    ll.insert_at_end(55)  # DLL: 45 <-> 55
    ll.insert_at_end(85)  # DLL: 45 <-> 55 <-> 85
    ll.insert_at_beg(21)  # DLL: 21 <-> 45 <-> 55 <-> 85
    ll.insert_at_position(2, 77)  # DLL: 21 <-> 45 <-> 77 <-> 55 <-> 85

    ll.display()  # Forward display
    ll.delete()  # Remove last node (85)
    ll.display()  # Forward display
    ll.display(is_backward=True)  # Backward display

    print("target found at index -->", ll.search(55))  # Index of 55
    print("is linked list empty", ll.is_empty())  # False
    print("linked list length", ll.length())  # Count nodes

    # Iterate using __iter__
    for value in ll:
        print("iterated value:", value)

    # Using len()
    print("Length using len():", len(ll))

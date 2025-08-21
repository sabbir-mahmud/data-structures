"""
==============================
Doubly Linked List (DLL) in Python
==============================

What is a Linked List?
----------------------
A Linked List is a linear data structure where elements (nodes) are connected using pointers/references.

In a Doubly Linked List:
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


class Node:
    # Define a class named Node which will represent a single node
    # in a Doubly Linked List (DLL).

    def __init__(self, data, next=None, prev=None):
        # __init__ is the constructor method in Python.
        # It initializes a new Node object when created.

        self.data = data
        # Store the actual value (data) inside the node.
        # Example: if you create Node(10), then self.data = 10.

        self.next = next
        # A pointer/reference to the "next" node in the list.
        # By default, it is None (meaning no next node yet).
        # Later, when linking nodes, this will point to another Node.

        self.prev = prev
        # A pointer/reference to the "previous" node in the list.
        # By default, it is None (meaning no previous node yet).
        # Later, when linking nodes, this will point to another Node.


# Doubly Linked List implementation
class LinkedList:
    def __init__(self):
        self.head = None  # pointer to the first node of the list
        self.tail = None  # pointer to the last node of the list

    # Insert at the beginning of the list
    def insert_at_beg(self, value):
        node = Node(data=value)  # create a new node with given value

        if self.head:  # if list already has nodes
            node.next = self.head  # new node points to current head
            self.head.prev = node  # current head points back to new node
        else:  # if list is empty
            self.tail = node  # tail also becomes this new node

        self.head = node  # update head to new node
        return

    # Insert at the end of the list
    def insert_at_end(self, value):
        node = Node(data=value)  # create a new node with given value

        if self.tail:  # if list already has nodes
            node.prev = self.tail  # new node points back to current tail
            self.tail.next = node  # current tail points forward to new node
        else:  # if list is empty
            self.head = node  # head also becomes this new node

        self.tail = node  # update tail to new node
        return

    # Insert at a given position (pos = index starting from 0)
    def insert_at_position(self, pos, value):
        count = 0
        itr = self.head  # start from head

        # Traverse until the node just before desired position
        while itr:
            if count + 1 == pos:  # stop just before position
                break
            count += 1
            itr = itr.next

        # Create new node between itr and itr.next
        node = Node(data=value, next=itr.next, prev=itr)

        # Fix connections
        itr.next.prev = node  # old next node's prev → new node
        itr.next = node  # current node's next → new node
        return

    # Delete last element from the list
    def delete(self):
        self.tail = self.tail.prev  # move tail backward
        self.tail.next = None  # new tail should point to None
        return

    # Return length of list
    def length(self):
        count = 0
        itr = self.head  # start from head
        while itr:
            count += 1
            itr = itr.next  # move forward
        return count

    # Check if list is empty
    def is_empty(self):
        return True if not self.head else False

    # Search for a value and return index if found, else -1
    def search(self, value):
        itr = self.head  # start from head
        index = 0

        while itr:
            if itr.data == value:  # if found
                return index
            itr = itr.next  # move forward
            index += 1

        return -1  # not found

    # Display the list either forward or backward
    def display(self, is_backward=False):
        # if forward, start from head
        # if backward, start from tail
        itr = self.head if not is_backward else self.tail
        ll = ""

        while itr:
            ll += f"{itr.data} --> "
            # move forward if normal display, else move backward
            itr = itr.next if not is_backward else itr.prev

        print(ll)
        return

    # Iterator method to make LinkedList iterable
    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data  # return node data one by one
            itr = itr.next
        return

    # Enable len() function to return length
    def __len__(self):
        return self.length()


# 🔹 Demo usage
if __name__ == "__main__":
    ll = LinkedList()
    print("is linked list empty", ll.is_empty())  # True (list is empty)

    # Insert nodes
    ll.insert_at_end(45)  # LinkedList: 45
    ll.insert_at_end(55)  # LinkedList: 45 -> 55
    ll.insert_at_end(85)  # LinkedList: 45 -> 55 -> 85
    ll.insert_at_beg(21)  # LinkedList: 21 -> 45 -> 55 -> 85
    ll.insert_at_position(2, 77)  # LinkedList: 21 -> 45 -> 77 -> 55 -> 85

    ll.display()  # Forward display

    ll.delete()  # Remove last node (85)
    ll.display()  # Display again

    ll.display(is_backward=True)  # Display backward

    print("target found at index --> ", ll.search(55))  # Should return 3
    print("is linked list empty", ll.is_empty())  # False
    print("linked list length", ll.length())  # Count nodes

    # Iterating with __iter__
    for value in ll:
        print("iterated value:", value)

    # Using len() thanks to __len__
    print("Length using len():", len(ll))

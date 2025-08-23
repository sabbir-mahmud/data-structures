"""
==============================
Circular Doubly Linked List (CDLL) in Python
==============================

What is a Circular Doubly Linked List?
--------------------------------------
A Circular Doubly Linked List (CDLL) is a type of linked list where:
    • Each node contains:
        - Data (the actual value)
        - Pointer to the next node
        - Pointer to the previous node
    • Unlike normal doubly linked lists:
        - The last node (tail) points to the first node (head).
        - The first node (head) points back to the last node (tail).
    • Traversal is possible in BOTH directions, and you can loop endlessly.

Example:
    Head ↔ Node1 ↔ Node2 ↔ Node3 ↔ (back to Head)

How it Works?
-------------
Unlike arrays, elements are NOT stored in contiguous memory.
You must traverse from the head or tail step by step.
Since it’s circular, traversal can wrap around endlessly.

How it Solves Array Problems?
-----------------------------
Arrays have drawbacks → CDLL fixes some of them:

1. Dynamic Size
   - Array: Fixed size (needs resizing).
   - CDLL: Grows/shrinks easily (memory allocated per node).

2. Insert/Delete Efficiency
   - Array: Inserting/deleting in middle = O(n).
   - CDLL: O(1) if you already have node reference.

3. Two-way Traversal
   - Array: O(1) random access, but no easy "previous" link.
   - CDLL: Can move forward or backward efficiently.

Big-O Analysis (Array vs Circular DLL)
--------------------------------------
Operation        Array               Circular DLL
--------------------------------------------------
Access           O(1)                O(n)
Search           O(n)                O(n)
Insert at Front  O(n)                O(1)
Insert at End    O(1) amortized      O(1)
Insert Middle    O(n)                O(1) if ref, O(n) otherwise
Delete at Front  O(n)                O(1)
Delete at End    O(1)                O(1)
Delete Middle    O(n)                O(1) if ref, O(n) otherwise

Quick takeaway:
---------------
• Use Array if you need fast random access.
• Use CDLL if you need frequent insert/delete and bidirectional circular traversal.
"""


class Node:
    # A Node is the basic building block of a Circular Doubly Linked List (CDLL).

    def __init__(self, data, next=None, prev=None):
        # __init__ is the constructor that runs when you create a new Node.

        self.data = data
        # Store the actual data (value) in this node.

        self.next = next
        # A reference (pointer) to the NEXT node in the list.
        # Will be updated when nodes are linked together.

        self.prev = prev
        # A reference (pointer) to the PREVIOUS node in the list.
        # Will be updated when nodes are linked together.


class CircularDoublyLinkedList:
    def __init__(self):
        # Initialize the CDLL with empty head and tail
        self.head = None
        self.tail = None

    def insert_at_beg(self, value):
        # Insert a new node at the BEGINNING of the list
        node = Node(data=value)

        if self.head is None:
            # If list is empty, new node becomes both head and tail
            self.head = self.tail = node
            node.next = node.prev = node  # point to itself (circular link)
        else:
            # Link new node with current head and tail
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node  # update head to new node
        return

    def insert_at_end(self, value):
        # Insert a new node at the END of the list
        node = Node(data=value)

        if self.head is None:
            # If list is empty, new node becomes both head and tail
            self.head = self.tail = node
            node.next = node.prev = node  # circular link
        else:
            # Link new node between tail and head
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node  # update tail
        return

    def delete(self):
        # Delete the LAST node from the list
        if self.head is None:
            return  # nothing to delete

        if self.head == self.tail:
            # Only one node exists
            self.head = self.tail = None
        else:
            # Remove tail by linking its prev with head
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        return

    def length(self):
        # Count number of nodes in the CDLL
        if self.head is None:
            return 0

        count = 1
        itr = self.head
        while itr.next != self.head:
            count += 1
            itr = itr.next
        return count

    def is_empty(self):
        # Return True if list is empty
        return self.head is None

    def search(self, value):
        # Search for a value and return index if found, else -1
        if self.head is None:
            return -1

        index = 0
        itr = self.head
        while True:
            if itr.data == value:
                return index
            itr = itr.next
            index += 1
            if itr == self.head:
                break
        return -1

    def display(self, is_backward=False):
        # Display the list forward (head → tail) or backward (tail → head)
        if self.head is None:
            print("List is empty")
            return

        ll = ""
        if not is_backward:
            # Traverse forward
            itr = self.head
            while True:
                ll += f"{itr.data} --> "
                itr = itr.next
                if itr == self.head:
                    break
        else:
            # Traverse backward
            itr = self.tail
            while True:
                ll += f"{itr.data} --> "
                itr = itr.prev
                if itr == self.tail:
                    break
        print(ll)
        return

    def __iter__(self):
        # Make CDLL iterable using forward traversal
        if self.head is None:
            return
        itr = self.head
        while True:
            yield itr.data
            itr = itr.next
            if itr == self.head:
                break

    def __len__(self):
        # Allow len(cdll) usage
        return self.length()


# 🔹 Demo usage
if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    print("is linked list empty", cdll.is_empty())  # True

    # Insert nodes
    cdll.insert_at_end(45)
    cdll.insert_at_end(55)
    cdll.insert_at_end(85)
    cdll.insert_at_beg(21)
    cdll.display()  # Forward
    cdll.display(is_backward=True)  # Backward

    # Delete last node
    cdll.delete()
    cdll.display()

    print("target found at index --> ", cdll.search(55))
    print("is linked list empty", cdll.is_empty())
    print("linked list length", cdll.length())

    # Iterating with __iter__
    for value in cdll:
        print("iterated value:", value)

    # Using len()
    print("Length using len():", len(cdll))

"""
==========================================
   Circular Singly Linked List (CSLL)
==========================================

Key Rules:
    1. Each Node contains:
       - data (value)
       - next (pointer to next node)

    2. The last node (tail) points back to head → makes it circular.

    3. We maintain:
       - head (first node)
       - tail (last node, whose .next points to head)

Why no 'prev'?
   Unlike Doubly Linked List, CSLL only needs forward links.
   The circular connection (tail.next → head) lets us traverse endlessly.

==========================================
   Time Complexity (Big-O)
==========================================
Insert at beginning   : O(1)
Insert at end         : O(1)  (since we maintain tail pointer)
Delete at beginning   : O(1)
Delete at end         : O(n)  (need to find the 2nd last node)
Search                : O(n)
Display traversal     : O(n)
Space Complexity      : O(n)  (storing n nodes)
"""


# ===============================
# Node class (Building block of CSLL)
# ===============================
class Node:
    def __init__(self, data):
        self.data = data  # Stores value of the node
        self.next = None  # Points to the next node (default None)


# ===============================
# Circular Singly Linked List
# ===============================
class LinkedList:
    def __init__(self):
        self.head = None  # Head → first node of the list
        self.tail = None  # Tail → last node (points back to head)

    # ---------------------------------
    # Insert node at the beginning (O(1))
    # ---------------------------------
    def insert_at_beg(self, value):
        node = Node(data=value)  # Create new node
        if self.head is None:  # Case 1: List is empty
            self.head = self.tail = node  # Both head & tail point to new node
            self.tail.next = self.head  # Make it circular (tail.next → head)
        else:  # Case 2: Non-empty list
            node.next = self.head  # New node points to current head
            self.head = node  # Move head to new node
            self.tail.next = self.head  # Update tail.next → new head
        return

    # ---------------------------------
    # Insert node at the end (O(1))
    # ---------------------------------
    def insert_at_end(self, value):
        node = Node(data=value)  # Create new node
        if self.tail is None:  # Case 1: List empty
            self.tail = self.head = node
            self.tail.next = self.head  # Circular link
        else:  # Case 2: Non-empty
            self.tail.next = node  # Old tail points to new node
            node.next = self.head  # New node points back to head
            self.tail = node  # Update tail
        return

    # ---------------------------------
    # Delete last node (O(n))
    # ---------------------------------
    def delete(self):
        itr = self.head
        # Traverse until 2nd last node
        while itr.next != self.tail:
            itr = itr.next

        itr.next = self.head  # 2nd last node points back to head
        self.tail = itr  # Update tail to 2nd last node
        return

    # ---------------------------------
    # Length of CSLL (O(n))
    # ---------------------------------
    def length(self):
        count = 0
        itr = self.head
        last = self.tail

        # Traverse nodes until we reach the tail
        while itr:
            count += 1
            if itr == last:  # Stop when we reach last node
                break
            itr = itr.next
        return count

    # ---------------------------------
    # Check if list is empty (O(1))
    # ---------------------------------
    def is_empty(self):
        return self.head is None

    # ---------------------------------
    # Search for a value (O(n))
    # ---------------------------------
    def search(self, value):
        index = 0
        itr = self.head
        last = self.tail

        while itr:
            if itr.data == value:  # Value found
                return index
            if itr == last:  # Reached last node → stop
                break
            itr = itr.next
            index += 1
        return -1  # Not found

    # ---------------------------------
    # Display all nodes (O(n))
    # ---------------------------------
    def display(self):
        itr = self.head
        last = self.tail
        ll = ""

        while itr:
            ll += f"{itr.data} --> "  # Add node to string
            if itr == last:  # Stop at last node
                break
            itr = itr.next
        print(ll)
        return

    # ---------------------------------
    # Iterator support (__iter__)
    # ---------------------------------
    def __iter__(self):
        itr = self.head
        last = self.tail
        while itr:
            yield itr.data
            if itr == last:  # Stop after last node
                break
            itr = itr.next
        return

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
    ll.display()

    ll.delete()  # Delete last node → removes 85
    ll.display()

    print("linked list length", ll.length())  # Count nodes
    print("is linked list empty", ll.is_empty())  # False
    print("target found at index --> ", ll.search(55))  # Should return index of 55
    ll.display()

    # Iterating with __iter__
    for value in ll:
        print("iterated value:", value)

    # Using len() thanks to __len__
    print("Length using len():", len(ll))

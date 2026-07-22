"""
==================================================
Singly Linked List (সিঙ্গলি লিংকড লিস্ট) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Linked List? (Linked List কী?)
--------------------------------------------------
- A Linked List is a linear data structure where elements (nodes) are connected using pointers/references. (Linked List হলো একটি Linear Data Structure, যেখানে প্রতিটি এলিমেন্ট বা Node একে অপরের সাথে Pointer বা Reference দিয়ে যুক্ত থাকে।)
- Data is NOT stored in contiguous memory. (ডেটা মেমরিতে পরপর বা Contiguous ভাবে থাকে না।)
- In a Singly Linked List, each node knows only the NEXT node. (Singly Linked List-এ প্রতিটি Node শুধু তার পরের Node-কে চেনে।)

Structure of a Node (Node-এর গঠন)
--------------------------------------------------
Each node has two parts. (প্রতিটি Node-এ দুইটি অংশ থাকে।)

+--------+--------+
|  data  |  next  |
+--------+--------+
    |        |
  value   address of next node

- data -> The actual value. (আসল ডেটা বা মান।)
- next -> Reference to the next node. (পরের Node-এর ঠিকানা বা Reference।)

--------------------------------------------------
How a Singly Linked List Looks (দেখতে কেমন হয়)
--------------------------------------------------

head
 |
 v
+----+----+     +----+----+     +----+------+
| 21 |  *-|---->| 45 |  *-|---->| 55 | None |
+----+----+     +----+----+     +----+------+
   Node1           Node2           Node3

- head points to the first node. (head প্রথম Node-কে Point করে।)
- The last node's next is None, which marks the end. (শেষ Node-এর next = None, এটাই লিস্টের শেষ বোঝায়।)
- If head is None, the list is empty. (head যদি None হয়, তার মানে লিস্ট খালি।)

--------------------------------------------------
How Data is Stored in Memory (মেমরিতে ডেটা কীভাবে থাকে)
--------------------------------------------------
Array -> Contiguous (পাশাপাশি)
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+
1000 1004 1008 1012

Linked List -> Scattered (ছড়ানো ছিটানো)
Address 5000 : [ 10 | 8200 ]
Address 8200 : [ 20 | 3100 ]
Address 3100 : [ 30 | None ]

- Nodes can live anywhere in memory. (Node গুলো মেমরির যেকোনো জায়গায় থাকতে পারে।)
- They are connected only by addresses. (এরা শুধু ঠিকানার মাধ্যমে একে অপরের সাথে যুক্ত থাকে।)
- This is why arr[i] style indexing is impossible here. (এই কারণেই এখানে Array-এর মতো সরাসরি Index ব্যবহার করা যায় না।)

--------------------------------------------------
Why Access is O(n) (Access কেন O(n)?)
--------------------------------------------------
There is no address formula like an array has. (Array-এর মতো কোনো Address ফর্মুলা এখানে নেই।)
To reach index 3, you must walk from head one node at a time. (Index 3-এ পৌঁছাতে হলে head থেকে এক এক করে হেঁটে যেতে হয়।)

head -> Node0 -> Node1 -> Node2 -> Node3
        step 1   step 2   step 3   step 4

Therefore Time Complexity = O(n). (তাই Time Complexity O(n)।)

--------------------------------------------------
Insert at Beginning - O(1) (শুরুতে Insert করা)
--------------------------------------------------
Before:
head -> [45] -> [55] -> None

Step 1: New node points to the current head. (নতুন Node বর্তমান head-কে Point করে।)
       [21] -> [45] -> [55] -> None

Step 2: Move head to the new node. (head-কে নতুন Node-এ সরিয়ে দাও।)
head -> [21] -> [45] -> [55] -> None

No shifting is needed, so it is O(1). (কোনো ডেটা সরাতে হয় না, তাই O(1)।)
* This is the biggest win over an array, where insert at front is O(n). (Array-তে শুরুতে Insert করলে O(n) লাগে, এখানেই Linked List জেতে।)

--------------------------------------------------
Insert at End - O(n) (শেষে Insert করা)
--------------------------------------------------
head -> [21] -> [45] -> [55] -> None
                                 ^
                          we must reach here first

- We must traverse the whole list to find the last node. (শেষ Node খুঁজে পেতে পুরো লিস্ট ঘুরতে হয়।)
- Then set last.next = new node. (তারপর শেষ Node-এর next-এ নতুন Node বসাতে হয়।)
- Keeping a tail pointer makes this O(1). (একটি tail Pointer রাখলে এটি O(1) হয়ে যায়।)

--------------------------------------------------
Delete a Node (Node ডিলিট করা)
--------------------------------------------------
Delete 45 from: [21] -> [45] -> [55] -> None

Step 1: Find the PREVIOUS node (21). (আগের Node খুঁজে বের করো।)
Step 2: prev.next = prev.next.next  (আগের Node-কে পরের পরের Node-এ যুক্ত করো।)

        +-------------------+
        |                   v
[21] ---+     [45]        [55] -> None
              (unlinked)

- The unlinked node is cleaned up by the garbage collector. (বিচ্ছিন্ন Node গুলো Garbage Collector মুছে দেয়।)
- Finding the previous node costs O(n), the unlinking itself is O(1). (আগের Node খুঁজতে O(n), কিন্তু লিংক পরিবর্তন করতে O(1)।)

--------------------------------------------------
Why Linked Lists are NOT Cache-Friendly (কেন Cache-Friendly নয়)
--------------------------------------------------
Array in memory (CPU loads neighbours together):
+----+----+----+----+
| 1  | 2  | 3  | 4  |
+----+----+----+----+

Linked List in memory (scattered, CPU cache misses):
[1] ......... [3] .......... [2] ...... [4]

- Every "next" jump can be a cache miss. (প্রতিবার next-এ যাওয়া মানে একটি Cache Miss হতে পারে।)
- So even though both are O(n), array traversal is much faster in practice. (দুটোই O(n) হলেও বাস্তবে Array অনেক দ্রুত চলে।)

--------------------------------------------------
Extra Memory Cost (অতিরিক্ত মেমরি খরচ)
--------------------------------------------------
Array element  = value only. (শুধু মান।)
Linked node    = value + pointer. (মান + Pointer।)

- Each node needs extra space for the next reference. (প্রতিটি Node-এ next Reference রাখার জন্য বাড়তি জায়গা লাগে।)
- For small data (like single integers), the pointer can cost more than the data itself. (ছোট ডেটার ক্ষেত্রে Pointer-ই ডেটার চেয়ে বেশি মেমরি খায়।)

--------------------------------------------------
Array vs Singly Linked List (পার্থক্য)
--------------------------------------------------
| Feature              | Array         | Singly Linked List |
|----------------------|---------------|--------------------|
| Random Access        | O(1)          | O(n)               |
| Insert Beginning     | O(n)          | O(1)               |
| Delete Beginning     | O(n)          | O(1)               |
| Insert End           | O(1) amortized| O(n) / O(1) w/ tail|
| Delete End           | O(1)          | O(n)               |
| Search               | O(n)          | O(n)               |
| Cache Friendly       | Yes           | No                 |
| Memory Usage         | Lower         | Higher (pointers)  |
| Contiguous Memory    | Yes           | No                 |
| Size                 | Resize needed | Grows freely       |

--------------------------------------------------
Making It Behave Like a Python Object (Python-এর মতো আচরণ করানো)
--------------------------------------------------
Dunder (double underscore) methods let your class act like a built-in type. (Dunder Method গুলো তোমার ক্লাসকে Python-এর নিজস্ব টাইপের মতো আচরণ করায়।)

  __iter__  ->  enables  `for value in ll:`   (for লুপ চালানো যায়।)
  __len__   ->  enables  `len(ll)`            (len() ব্যবহার করা যায়।)

Without dunders          With dunders
--------------------     --------------------
ll.display()             for v in ll: ...
ll.length()              len(ll)

- __iter__ uses `yield`, which makes it a GENERATOR. (__iter__ এ yield ব্যবহার করায় এটি একটি Generator।)
- A generator hands over one value at a time and never builds a full list. (Generator একবারে একটি মান দেয়, পুরো List মেমরিতে বানায় না।)
- So iteration costs O(n) time but only O(1) extra memory. (তাই ঘোরার সময় O(n), কিন্তু বাড়তি মেমরি O(1)।)
- __len__ here is O(n) because it counts every node. (এখানে __len__ O(n), কারণ প্রতিটি Node গুনতে হয়।)
* A Python list stores its length, so len(list) is O(1). Keeping a self.size counter would do the same here. (Python List নিজের দৈর্ঘ্য মনে রাখে, তাই len() O(1); এখানেও একটি self.size রাখলে O(1) হতো।)

Helper methods (সহায়ক মেথড):
- is_empty() -> just checks `head is None` -> O(1). (শুধু head দেখেই বলে দেয় - O(1)।)
- search(value) -> walks node by node, returns the index or -1 -> O(n). (এক এক করে ঘুরে Index অথবা -1 ফেরত দেয় - O(n)।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Singly Linked Lists are used in:
- Implementing Stacks and Queues
- Hash Table collision chaining (bucket-এর ভিতরের চেইন)
- Adjacency lists in graphs
- Music / video playlists (next song)
- Undo-free simple history logs
- Memory managers (free block lists)

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. Why access is O(n) (No address formula, must traverse).
2. Why insert at beginning is O(1) (Only head pointer changes).
3. Why insert at end is O(n) (Must find the last node, unless tail is stored).
4. Why deletion needs the PREVIOUS node in a singly list.
5. Why linked lists are not cache-friendly (Scattered memory).
6. Extra memory overhead for pointers.
7. Common tricky problems: reverse a list, detect a cycle (Floyd's slow/fast pointer), find the middle node.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Thinking a Python list is a Linked List.
✔ A Python list is a Dynamic Array.

❌ Thinking insert/delete is always O(1).
✔ It is O(1) ONLY when you already hold the node reference; finding it costs O(n).

❌ Forgetting to handle the empty list (head is None).
✔ Always check the empty case first.

❌ Losing the rest of the list while relinking.
✔ Save the next reference BEFORE you overwrite a pointer.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation          | Complexity | Why?                              |
|--------------------|------------|-----------------------------------|
| Access / Index     | O(n)       | Must traverse from head           |
| Search             | O(n)       | Linear scan through nodes         |
| Insert Beginning   | O(1)       | Only head pointer changes         |
| Insert End         | O(n)       | Must reach the last node          |
| Insert at Position | O(n)       | Must traverse to that position    |
| Delete Beginning   | O(1)       | Move head to head.next            |
| Delete End         | O(n)       | Must find the second-last node    |
| Delete at Position | O(n)       | Must find the previous node       |
| Length / __len__   | O(n)       | Counts every node (no size field) |
| Iteration          | O(n)       | Visits every node, O(1) extra mem |
| is_empty           | O(1)       | Single `head is None` check       |
| Space              | O(n)       | One node + pointer per element    |

==================================================
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

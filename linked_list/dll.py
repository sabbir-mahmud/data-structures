"""
==================================================
Doubly Linked List (ডাবলি লিংকড লিস্ট) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Doubly Linked List? (Doubly Linked List কী?)
--------------------------------------------------
- A Doubly Linked List (DLL) is a linear data structure where each node is connected to BOTH its next and previous node. (DLL হলো এমন একটি Linear Data Structure, যেখানে প্রতিটি Node তার পরের এবং আগের - দুই দিকের Node-এর সাথেই যুক্ত থাকে।)
- Traversal is possible in both directions. (দুই দিকেই (সামনে ও পিছনে) ঘোরা যায়।)
- Data is NOT stored in contiguous memory. (ডেটা মেমরিতে পরপর বা Contiguous ভাবে থাকে না।)

Structure of a Node (Node-এর গঠন)
--------------------------------------------------
Each node has three parts. (প্রতিটি Node-এ তিনটি অংশ থাকে।)

+--------+--------+--------+
|  prev  |  data  |  next  |
+--------+--------+--------+
    |        |        |
 previous  value    next
 address           address

- prev -> Reference to the previous node. (আগের Node-এর ঠিকানা।)
- data -> The actual value. (আসল ডেটা বা মান।)
- next -> Reference to the next node. (পরের Node-এর ঠিকানা।)

--------------------------------------------------
How a Doubly Linked List Looks (দেখতে কেমন হয়)
--------------------------------------------------

        head                                    tail
         |                                       |
         v                                       v
+------+----+----+   +----+----+----+   +----+----+------+
| None | 21 |  *-|-->| *  | 45 |  *-|-->| *  | 55 | None |
+------+----+----+<--+----+----+----+<--+----+----+------+
        Node1              Node2              Node3

- head.prev is None and tail.next is None. (head-এর prev = None এবং tail-এর next = None।)
- Every middle node knows both neighbours. (মাঝের প্রতিটি Node তার দুই পাশের Node-কেই চেনে।)
- Keeping a tail pointer makes end operations O(1). (tail Pointer রাখলে শেষের কাজগুলো O(1) হয়।)

--------------------------------------------------
Why DLL Beats SLL (SLL-এর তুলনায় DLL কেন ভালো)
--------------------------------------------------
In a Singly Linked List, to delete a node you must find its PREVIOUS node. (SLL-এ কোনো Node ডিলিট করতে হলে আগে তার আগের Node খুঁজতে হয়।)
In a DLL, the node already knows its previous node. (DLL-এ Node নিজেই তার আগের Node-কে চেনে।)

SLL delete -> must traverse to find prev  -> O(n)
DLL delete -> node.prev is already there  -> O(1)

- Backward traversal is possible only in a DLL. (পিছন দিকে ঘোরা শুধু DLL-এই সম্ভব।)
- Delete at end is O(1) in a DLL (with tail), but O(n) in an SLL. (শেষের Node ডিলিট করা DLL-এ O(1), কিন্তু SLL-এ O(n)।)

--------------------------------------------------
Insert at Beginning - O(1) (শুরুতে Insert করা)
--------------------------------------------------
Before:
head -> [45] <-> [55] -> None

Step 1: new.next = head        (নতুন Node বর্তমান head-কে Point করে।)
Step 2: head.prev = new        (পুরোনো head পিছনে নতুন Node-কে Point করে।)
Step 3: head = new             (head নতুন Node-এ সরে যায়।)

After:
head -> [21] <-> [45] <-> [55] -> None

Only pointers change, nothing shifts. (শুধু Pointer পরিবর্তন হয়, কোনো ডেটা সরাতে হয় না।)

--------------------------------------------------
Insert at End - O(1) with tail (শেষে Insert করা)
--------------------------------------------------
Before:
head -> [21] <-> [45] <-> [55] <- tail

Step 1: new.prev = tail        (নতুন Node পিছনে tail-কে Point করে।)
Step 2: tail.next = new        (পুরোনো tail সামনে নতুন Node-কে Point করে।)
Step 3: tail = new             (tail নতুন Node-এ সরে যায়।)

After:
head -> [21] <-> [45] <-> [55] <-> [85] <- tail

* Without a tail pointer this becomes O(n). (tail Pointer না থাকলে এটি O(n) হয়ে যায়।)

--------------------------------------------------
Delete a Middle Node - O(1) with reference (মাঝের Node ডিলিট)
--------------------------------------------------
Delete 45 from: [21] <-> [45] <-> [55]

Step 1: node.prev.next = node.next   (আগের Node-কে পরের Node-এ যুক্ত করো।)
Step 2: node.next.prev = node.prev   (পরের Node-কে আগের Node-এ যুক্ত করো।)

        +-------------------+
        |                   v
[21] <--+     [45]        [55]
        ^   (unlinked)      |
        +-------------------+

- Both links must be fixed, otherwise the list breaks. (দুই দিকের লিংকই ঠিক করতে হবে, নাহলে লিস্ট ভেঙে যাবে।)
- Do not forget to update head or tail if you deleted an end node. (শুরু বা শেষের Node ডিলিট করলে head/tail আপডেট করতে ভুলো না।)

--------------------------------------------------
Extra Memory Cost (অতিরিক্ত মেমরি খরচ)
--------------------------------------------------
Array node = value. (শুধু মান।)
SLL node   = value + 1 pointer. (মান + ১টি Pointer।)
DLL node   = value + 2 pointers. (মান + ২টি Pointer।)

- A DLL uses more memory than an SLL for the same data. (একই ডেটার জন্য DLL, SLL-এর চেয়ে বেশি মেমরি খরচ করে।)
- You pay extra memory to buy O(1) backward operations. (বাড়তি মেমরি খরচ করে তুমি O(1) Backward Operation কিনছো।)
- Like an SLL, a DLL is NOT cache-friendly (nodes are scattered). (SLL-এর মতোই DLL-ও Cache-Friendly নয়, কারণ Node গুলো ছড়ানো থাকে।)

--------------------------------------------------
Array vs SLL vs DLL (পার্থক্য)
--------------------------------------------------
| Feature            | Array          | Singly LL   | Doubly LL   |
|--------------------|----------------|-------------|-------------|
| Random Access      | O(1)           | O(n)        | O(n)        |
| Insert Beginning   | O(n)           | O(1)        | O(1)        |
| Insert End         | O(1) amortized | O(n)        | O(1) w/tail |
| Delete Beginning   | O(n)           | O(1)        | O(1)        |
| Delete End         | O(1)           | O(n)        | O(1) w/tail |
| Delete Given Node  | O(n)           | O(n)        | O(1)        |
| Backward Traversal | Yes (index)    | No          | Yes         |
| Pointers per Node  | 0              | 1           | 2           |
| Cache Friendly     | Yes            | No          | No          |
| Memory Usage       | Lowest         | Medium      | Highest     |

--------------------------------------------------
Making It Behave Like a Python Object (Python-এর মতো আচরণ করানো)
--------------------------------------------------
Dunder (double underscore) methods let your class act like a built-in type. (Dunder Method গুলো তোমার ক্লাসকে Python-এর নিজস্ব টাইপের মতো আচরণ করায়।)

  __iter__  ->  enables  `for value in ll:`   (for লুপ চালানো যায়।)
  __len__   ->  enables  `len(ll)`            (len() ব্যবহার করা যায়।)

- __iter__ uses `yield`, which makes it a GENERATOR. (__iter__ এ yield ব্যবহার করায় এটি একটি Generator।)
- It walks forward from head, so iteration costs O(n) time and O(1) extra memory. (head থেকে সামনে এগোয়, তাই সময় O(n) কিন্তু বাড়তি মেমরি O(1)।)
- __len__ here is O(n) because it counts every node. (এখানে __len__ O(n), কারণ প্রতিটি Node গুনতে হয়।)
* A self.size counter updated on insert/delete would make len() O(1). (Insert/Delete-এর সময় self.size আপডেট করলে len() O(1) হতো।)

A DLL bonus: backward iteration (DLL-এর বাড়তি সুবিধা: পিছন দিকে ঘোরা)

    forward  : start at head, follow .next  (head থেকে .next ধরে)
    backward : start at tail, follow .prev  (tail থেকে .prev ধরে)

- display(is_backward=True) uses exactly this. (display(is_backward=True) ঠিক এই কাজটিই করে।)
- An SLL can NEVER do this, because it has no prev pointer. (SLL কখনোই এটি পারে না, কারণ তার prev নেই।)
- You could add a __reversed__ method to support Python's reversed(). (চাইলে __reversed__ যোগ করে reversed() সাপোর্ট দেওয়া যায়।)

Helper methods (সহায়ক মেথড):
- is_empty() -> just checks `head is None` -> O(1). (শুধু head দেখেই বলে দেয় - O(1)।)
- search(value) -> walks node by node, returns the index or -1 -> O(n). (এক এক করে ঘুরে Index অথবা -1 ফেরত দেয় - O(n)।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Doubly Linked Lists are used in:
- Browser history (back and forward buttons)
- Undo / Redo in text editors
- Music players (previous / next track)
- LRU Cache (DLL + HashMap is the classic design)
- Deque implementations (Python's collections.deque)
- Thread schedulers and process lists in operating systems

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. Why deleting a known node is O(1) in a DLL but O(n) in an SLL.
2. Why a tail pointer is what makes end operations O(1).
3. Why access is still O(n) (No address formula, still must traverse).
4. The memory trade-off: 2 pointers per node.
5. How LRU Cache uses a DLL + HashMap to get O(1) get and put.
6. The four pointers you must fix when inserting in the middle.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Updating only next and forgetting prev.
✔ Every insert/delete must fix BOTH directions.

❌ Forgetting to update head or tail when deleting the first/last node.
✔ Always check if the node is head or tail before unlinking.

❌ Thinking a DLL gives O(1) access.
✔ Access is still O(n); only pointer surgery is O(1).

❌ Assuming a DLL is always better than an SLL.
✔ It costs an extra pointer per node; use an SLL if you never go backward.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation          | Complexity | Why?                              |
|--------------------|------------|-----------------------------------|
| Access / Index     | O(n)       | Must traverse from head or tail   |
| Search             | O(n)       | Linear scan through nodes         |
| Insert Beginning   | O(1)       | Only head links change            |
| Insert End         | O(1)       | Tail pointer is already known     |
| Insert at Position | O(n)       | Must traverse to that position    |
| Delete Beginning   | O(1)       | Move head to head.next            |
| Delete End         | O(1)       | Tail knows its prev node          |
| Delete Given Node  | O(1)       | node.prev and node.next are known |
| Length / __len__   | O(n)       | Counts every node (no size field) |
| Iteration          | O(n)       | Visits every node, O(1) extra mem |
| Backward traversal | O(n)       | Follows .prev from tail           |
| is_empty           | O(1)       | Single `head is None` check       |
| Space              | O(n)       | One node + 2 pointers per element |

==================================================
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

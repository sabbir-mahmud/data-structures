"""
==================================================
Circular Doubly Linked List (সার্কুলার ডাবলি লিংকড লিস্ট) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Circular Doubly Linked List? (CDLL কী?)
--------------------------------------------------
- A CDLL is a Doubly Linked List where the two ends are joined together. (CDLL হলো এমন একটি Doubly Linked List, যার দুই মাথা একসাথে জোড়া লাগানো থাকে।)
- tail.next points to head, and head.prev points to tail. (tail.next হলো head, আর head.prev হলো tail।)
- No None anywhere - traversal in BOTH directions never ends. (কোথাও None নেই, তাই দুই দিকেই অসীমভাবে ঘোরা যায়।)
- It is the most powerful (and most memory-hungry) linked list variant. (এটি সবচেয়ে শক্তিশালী, কিন্তু সবচেয়ে বেশি মেমরি খরচকারী Linked List।)

Structure of a Node (Node-এর গঠন)
--------------------------------------------------
+--------+--------+--------+
|  prev  |  data  |  next  |
+--------+--------+--------+

- prev -> Previous node; for the head it points to tail. (আগের Node; head-এর ক্ষেত্রে এটি tail-কে Point করে।)
- data -> The actual value. (আসল ডেটা বা মান।)
- next -> Next node; for the tail it points to head. (পরের Node; tail-এর ক্ষেত্রে এটি head-কে Point করে।)

--------------------------------------------------
How a CDLL Looks (দেখতে কেমন হয়)
--------------------------------------------------

        head                                  tail
         |                                     |
         v                                     v
   +----+----+----+   +----+----+----+   +----+----+----+
+->| *  | 21 |  *-|-->| *  | 45 |  *-|-->| *  | 55 |  *-|--+
|  +----+----+----+<--+----+----+----+<--+----+----+----+  |
|    ^                                                     |
|    +--------------------- prev --------------------------+
+-------------------------- next --------------------------+

- Both ends wrap around, forming a two-way ring. (দুই মাথাই ঘুরে যুক্ত হয়ে দুই-মুখী বৃত্ত তৈরি করে।)
- With a single node: node.next = node.prev = node (itself). (একটি মাত্র Node থাকলে সে নিজেই নিজের next এবং prev হয়।)

--------------------------------------------------
Why CDLL is the Best of Both Worlds (CDLL কেন সেরা)
--------------------------------------------------
CSLL problem: delete at end is O(n) (no prev pointer). (CSLL-এ শেষের Node ডিলিট করা O(n), কারণ prev নেই।)
CDLL fix:     tail.prev is already known -> O(1). (CDLL-এ tail.prev আগে থেকেই জানা, তাই O(1)।)

| Operation      | CSLL | CDLL |
|----------------|------|------|
| Insert Front   | O(1) | O(1) |
| Insert End     | O(1) | O(1) |
| Delete Front   | O(1) | O(1) |
| Delete End     | O(n) | O(1) |
| Go backward    | No   | Yes  |

- Every end operation is O(1) in a CDLL. (CDLL-এ দুই মাথার সব কাজই O(1)।)
- This is exactly why Python's collections.deque is built on a doubly linked structure. (এই কারণেই Python-এর deque এই ধরনের গঠন ব্যবহার করে।)

--------------------------------------------------
Insert at End - O(1) (শেষে Insert করা)
--------------------------------------------------
Four pointers must be fixed. (চারটি Pointer ঠিক করতে হয়।)

Step 1: new.prev = tail        (নতুন Node পিছনে tail-কে চেনে।)
Step 2: new.next = head        (নতুন Node সামনে head-কে চেনে।)
Step 3: tail.next = new        (পুরোনো tail সামনে নতুন Node-কে চেনে।)
Step 4: head.prev = new        (head পিছনে নতুন Node-কে চেনে।)
Then:   tail = new             (tail নতুন Node-এ সরে যায়।)

- Miss any one of the four and the ring breaks. (চারটির একটিও ভুলে গেলে বৃত্ত ভেঙে যাবে।)

--------------------------------------------------
Delete at End - O(1) (শেষের Node ডিলিট করা)
--------------------------------------------------
Before: head -> [21] <-> [45] <-> [55] <- tail (ring)

Step 1: tail = tail.prev       (tail এক ধাপ পিছনে সরে যায়।)
Step 2: tail.next = head       (নতুন tail আবার head-কে Point করে।)
Step 3: head.prev = tail       (head পিছনে নতুন tail-কে Point করে।)

After:  head -> [21] <-> [45] <- tail (ring)

- No traversal needed because prev exists -> O(1). (prev থাকার কারণে ঘুরতে হয় না, তাই O(1)।)
- Special case: if head == tail, the list becomes empty. (বিশেষ ক্ষেত্র: head আর tail এক হলে লিস্ট খালি হয়ে যায়।)

--------------------------------------------------
The Infinite Loop Danger (অসীম লুপের বিপদ)
--------------------------------------------------
Nothing is ever None, so `while itr:` never stops. (কিছুই None হয় না, তাই `while itr:` কখনো থামবে না।)

Correct pattern (do-while style): (সঠিক নিয়ম:)

    itr = self.head
    while True:
        process(itr)
        itr = itr.next
        if itr == self.head:   # came back to start (শুরুতে ফিরে এসেছি)
            break

- Forward: stop when you return to head. (সামনে গেলে head-এ ফিরে এলে থামো।)
- Backward: stop when you return to tail. (পিছনে গেলে tail-এ ফিরে এলে থামো।)
- Always guard the empty list first. (আগে লিস্ট খালি কিনা দেখে নাও।)

--------------------------------------------------
Memory Cost (মেমরি খরচ)
--------------------------------------------------
Array node = value. (শুধু মান।)
CSLL node  = value + 1 pointer. (মান + ১টি Pointer।)
CDLL node  = value + 2 pointers. (মান + ২টি Pointer।)

- A CDLL is the heaviest of all linked list variants. (সব Linked List-এর মধ্যে CDLL সবচেয়ে ভারী।)
- Like all linked lists, it is NOT cache-friendly. (সব Linked List-এর মতো এটিও Cache-Friendly নয়।)
- You pay memory to get O(1) operations at both ends plus two-way traversal. (দুই মাথায় O(1) এবং দুই-মুখী ঘোরার সুবিধা পেতে বাড়তি মেমরি দিতে হয়।)

--------------------------------------------------
All Four Variants Compared (চার ধরনের তুলনা)
--------------------------------------------------
| Feature            | SLL  | DLL  | CSLL | CDLL |
|--------------------|------|------|------|------|
| Pointers per node  | 1    | 2    | 1    | 2    |
| Insert Front       | O(1) | O(1) | O(1) | O(1) |
| Insert End         | O(n) | O(1) | O(1) | O(1) |
| Delete Front       | O(1) | O(1) | O(1) | O(1) |
| Delete End         | O(n) | O(1) | O(n) | O(1) |
| Backward traversal | No   | Yes  | No   | Yes  |
| Endless loop       | No   | No   | Yes  | Yes  |
| Memory usage       | Low  | Med  | Low  | High |

--------------------------------------------------
Making It Behave Like a Python Object (Python-এর মতো আচরণ করানো)
--------------------------------------------------
Dunder (double underscore) methods let your class act like a built-in type. (Dunder Method গুলো তোমার ক্লাসকে Python-এর নিজস্ব টাইপের মতো আচরণ করায়।)

  __iter__  ->  enables  `for value in cdll:`   (for লুপ চালানো যায়।)
  __len__   ->  enables  `len(cdll)`            (len() ব্যবহার করা যায়।)

A CDLL __iter__ needs TWO guards: (CDLL-এর __iter__ এ দুইটি সুরক্ষা লাগে:)

  1. Empty check first, otherwise head.next crashes. (আগে খালি কিনা দেখো, নাহলে head.next এ Error হবে।)
  2. A do-while loop that breaks on returning to head. (head-এ ফিরে এলে break করতে হবে।)

     if self.head is None:
         return                       <-- guard 1 (সুরক্ষা ১)
     itr = self.head
     while True:
         yield itr.data
         itr = itr.next
         if itr == self.head:
             break                    <-- guard 2 (সুরক্ষা ২)

- `while True` + break is the do-while pattern Python lacks. (Python-এ do-while নেই, তাই while True + break ব্যবহার হয়।)
- Using a plain `while itr:` would loop FOREVER. (শুধু `while itr:` লিখলে চিরকাল চলতে থাকবে।)
- __iter__ uses `yield`, so it is a generator: O(n) time, O(1) extra memory. (__iter__ একটি Generator: সময় O(n), বাড়তি মেমরি O(1)।)
- __len__ counts nodes around the ring -> O(n). (__len__ রিং ঘুরে Node গোনে - O(n)।)

Helper methods (সহায়ক মেথড):
- is_empty() -> just checks `head is None` -> O(1). (শুধু head দেখেই বলে দেয় - O(1)।)
- search(value) -> walks the ring, returns the index or -1 -> O(n). (রিং ঘুরে Index অথবা -1 ফেরত দেয় - O(n)।)
- display(is_backward=True) -> same pattern, but follows .prev from tail. (একই নিয়ম, তবে tail থেকে .prev ধরে ঘোরে।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Circular Doubly Linked Lists are used in:
- Music / video players with repeat and previous-next (আগে-পরে দুই দিকেই যাওয়া যায়)
- Image carousels and photo sliders
- Fibonacci Heaps (root list is a CDLL)
- Advanced round-robin schedulers that must also step backward
- Deque implementations
- Undo/Redo rings with a fixed history size
- Multiplayer board games where turn order can reverse

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. The two defining links: tail.next = head AND head.prev = tail.
2. Why delete at end is O(1) here but O(n) in a CSLL.
3. The four pointers you must update on every insert.
4. How to terminate traversal safely (Come back to head/tail).
5. The single-node case where the node points to itself.
6. The memory trade-off: 2 pointers per node, worst cache locality.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Using `while itr:` to traverse.
✔ Nothing is None here; stop when you return to the starting node.

❌ Updating only 2 of the 4 pointers on insert.
✔ Fix new.prev, new.next, neighbour.next AND neighbour.prev.

❌ Forgetting the single-node case.
✔ With one node, node.next == node.prev == node itself.

❌ Forgetting to set head = tail = None when the last node is deleted.
✔ Always handle the "list becomes empty" case.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation          | Complexity | Why?                              |
|--------------------|------------|-----------------------------------|
| Access / Index     | O(n)       | Must traverse the ring            |
| Search             | O(n)       | Linear scan around the ring       |
| Insert Beginning   | O(1)       | Only end links change             |
| Insert End         | O(1)       | Tail pointer is already known     |
| Delete Beginning   | O(1)       | Relink head, tail.next, head.prev |
| Delete End         | O(1)       | tail.prev is already known        |
| Delete Given Node  | O(1)       | node.prev and node.next are known |
| Length / __len__   | O(n)       | Counts every node (no size field) |
| Iteration          | O(n)       | Stops at head, O(1) extra memory  |
| Backward traversal | O(n)       | Follows .prev from tail           |
| is_empty           | O(1)       | Single `head is None` check       |
| Space              | O(n)       | One node + 2 pointers per element |

==================================================
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

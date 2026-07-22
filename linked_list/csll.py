"""
==================================================
Circular Singly Linked List (সার্কুলার সিঙ্গলি লিংকড লিস্ট) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Circular Singly Linked List? (CSLL কী?)
--------------------------------------------------
- A CSLL is a Singly Linked List where the LAST node points back to the FIRST node. (CSLL হলো এমন একটি Singly Linked List, যেখানে শেষ Node আবার প্রথম Node-কে Point করে।)
- There is no None at the end - the list forms a closed ring. (শেষে কোনো None থাকে না, পুরো লিস্টটি একটি বৃত্ত বা রিং তৈরি করে।)
- Each node still has only a next pointer (no prev). (প্রতিটি Node-এ এখনো শুধু next Pointer থাকে, prev থাকে না।)

Structure of a Node (Node-এর গঠন)
--------------------------------------------------
+--------+--------+
|  data  |  next  |
+--------+--------+

- data -> The actual value. (আসল ডেটা বা মান।)
- next -> Next node; for the tail it points to head. (পরের Node; tail-এর ক্ষেত্রে এটি head-কে Point করে।)

--------------------------------------------------
How a CSLL Looks (দেখতে কেমন হয়)
--------------------------------------------------

  head                                   tail
   |                                      |
   v                                      v
+----+----+    +----+----+    +----+----+
| 21 |  *-|--->| 45 |  *-|--->| 55 |  *-|--+
+----+----+    +----+----+    +----+----+  |
   ^                                       |
   |                                       |
   +---------------------------------------+
            tail.next points to head

- tail.next = head is what makes it circular. (tail.next = head - এটাই একে Circular বানায়।)
- Starting from any node you can reach every other node. (যেকোনো Node থেকে শুরু করে সব Node-এ পৌঁছানো যায়।)
- If head is None, the list is empty. (head যদি None হয়, তার মানে লিস্ট খালি।)

--------------------------------------------------
Why Circular? (Circular কেন দরকার?)
--------------------------------------------------
Normal SLL: [21] -> [45] -> [55] -> None
            Traversal ends here. (এখানেই ঘোরা শেষ।)

Circular SLL: [21] -> [45] -> [55] --+
                ^                    |
                +--------------------+
            Traversal never ends. (ঘোরা কখনো শেষ হয় না।)

- Perfect for round-robin style problems where you must cycle forever. (Round-Robin ধরনের সমস্যার জন্য উপযুক্ত, যেখানে বারবার ঘুরতে হয়।)
- Insert at end becomes O(1) because tail already points to head. (শেষে Insert করা O(1) হয়, কারণ tail আগে থেকেই head-কে চেনে।)
- No need to reset any pointer to go back to the start. (শুরুতে ফিরে যেতে আলাদা কোনো Pointer লাগে না।)

--------------------------------------------------
The Infinite Loop Danger (অসীম লুপের বিপদ)
--------------------------------------------------
In an SLL you stop when itr becomes None. (SLL-এ itr যখন None হয়, তখন থামা যায়।)
In a CSLL, itr NEVER becomes None. (CSLL-এ itr কখনোই None হয় না।)

while itr:              <-- WRONG, runs forever! (ভুল, চিরকাল চলবে!)
    itr = itr.next

Correct stopping conditions: (সঠিক থামার নিয়ম:)
    1. Stop when itr == tail (after processing it). (tail-এ পৌঁছালে থামো।)
    2. Or use a do-while style: process, move, stop when itr == head. (অথবা head-এ ফিরে এলে থামো।)

- This is the single most important rule of circular lists. (Circular List-এর সবচেয়ে গুরুত্বপূর্ণ নিয়ম এটাই।)

--------------------------------------------------
Insert at Beginning - O(1) (শুরুতে Insert করা)
--------------------------------------------------
Before:  head -> [45] -> [55] --+ (tail)
            ^                   |
            +-------------------+

Step 1: new.next = head        (নতুন Node বর্তমান head-কে Point করে।)
Step 2: head = new             (head নতুন Node-এ সরে যায়।)
Step 3: tail.next = head       (tail এখন নতুন head-কে Point করে।)

After:   head -> [21] -> [45] -> [55] --+ (tail)
            ^                           |
            +---------------------------+

* Step 3 is the step everyone forgets. (৩ নম্বর ধাপটাই সবাই ভুলে যায়।)

--------------------------------------------------
Insert at End - O(1) (শেষে Insert করা)
--------------------------------------------------
Step 1: tail.next = new        (পুরোনো tail নতুন Node-কে Point করে।)
Step 2: new.next = head        (নতুন Node আবার head-কে Point করে।)
Step 3: tail = new             (tail নতুন Node-এ সরে যায়।)

- Because we store tail, no traversal is needed -> O(1). (tail সংরক্ষণ করা আছে বলে ঘুরতে হয় না, তাই O(1)।)
- In a plain SLL this would cost O(n). (সাধারণ SLL-এ এটি O(n) খরচ করত।)

--------------------------------------------------
Delete at End - O(n) (শেষের Node ডিলিট করা)
--------------------------------------------------
head -> [21] -> [45] -> [55] --+ (tail)
                  ^            |
          we need this node    |
                  +------------+

- We must find the SECOND LAST node. (আমাদের দ্বিতীয় শেষ Node খুঁজে বের করতে হয়।)
- A singly list has no prev pointer, so we traverse -> O(n). (Singly List-এ prev নেই, তাই ঘুরতে হয় - O(n)।)
- Then: secondLast.next = head and tail = secondLast. (তারপর দ্বিতীয় শেষ Node-কে head-এর সাথে যুক্ত করে tail বানাতে হয়।)
- A Circular DOUBLY Linked List solves this in O(1). (Circular Doubly Linked List এটি O(1)-এ সমাধান করে।)

Two edge cases delete() must handle: (delete()-কে দুইটি বিশেষ অবস্থা সামলাতে হয়:)

  1. Empty list (head is None) -> there is nothing to delete. (খালি লিস্ট - মোছার কিছু নেই।)
  2. Single node (head == tail) -> the list must become EMPTY. (একটিমাত্র Node - লিস্ট খালি হয়ে যাওয়া উচিত।)

     Single node:  head = tail = [21], and 21.next = 21 (itself)

     `while itr.next != self.tail` never runs, because itr.next IS tail.
     (লুপটি একবারও চলে না, কারণ itr.next-ই হলো tail।)
     Result: head and tail must be set to None by hand. (তাই হাতে করে head ও tail কে None করতে হয়।)

* The delete() in THIS file is the simplified version and does not guard these two cases. (এই ফাইলের delete() সরল ভার্সন, এই দুইটি অবস্থা সামলায় না।)
* Always ask about empty and single-element cases in an interview. (ইন্টারভিউতে সবসময় খালি ও একটিমাত্র এলিমেন্টের অবস্থা নিয়ে ভাবো।)

--------------------------------------------------
SLL vs CSLL (পার্থক্য)
--------------------------------------------------
| Feature              | Singly LL     | Circular Singly LL |
|----------------------|---------------|--------------------|
| Last node's next     | None          | head               |
| Insert Beginning     | O(1)          | O(1)               |
| Insert End           | O(n)          | O(1) (with tail)   |
| Delete Beginning     | O(1)          | O(1)               |
| Delete End           | O(n)          | O(n)               |
| Search               | O(n)          | O(n)               |
| Endless traversal    | No            | Yes                |
| Stop condition       | itr is None   | itr == tail/head   |
| Risk                 | Low           | Infinite loop      |

--------------------------------------------------
Making It Behave Like a Python Object (Python-এর মতো আচরণ করানো)
--------------------------------------------------
Dunder (double underscore) methods let your class act like a built-in type. (Dunder Method গুলো তোমার ক্লাসকে Python-এর নিজস্ব টাইপের মতো আচরণ করায়।)

  __iter__  ->  enables  `for value in ll:`   (for লুপ চালানো যায়।)
  __len__   ->  enables  `len(ll)`            (len() ব্যবহার করা যায়।)

The circular twist: iteration MUST stop itself. (Circular-এর বিশেষ দিক: ঘোরা নিজে থেকেই থামতে হবে।)

  Normal SLL __iter__          Circular SLL __iter__
  --------------------         ----------------------------
  while itr:                   while itr:
      yield itr.data               yield itr.data
      itr = itr.next               if itr == last: break   <-- required!
                                   itr = itr.next

- Without that break, `for v in ll:` would loop FOREVER. (ঐ break না থাকলে for লুপ চিরকাল চলতে থাকবে।)
- The same rule applies to length(), search() and display(). (একই নিয়ম length(), search() ও display()-এর জন্যও প্রযোজ্য।)
- Every method in this file stops by comparing against self.tail. (এই ফাইলের প্রতিটি মেথড self.tail-এর সাথে তুলনা করে থামে।)
- __iter__ uses `yield`, so it is a generator: O(n) time, O(1) extra memory. (__iter__ একটি Generator: সময় O(n), বাড়তি মেমরি O(1)।)

Helper methods (সহায়ক মেথড):
- is_empty() -> just checks `head is None` -> O(1). (শুধু head দেখেই বলে দেয় - O(1)।)
- search(value) -> walks the ring, returns the index or -1 -> O(n). (রিং ঘুরে Index অথবা -1 ফেরত দেয় - O(n)।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Circular Singly Linked Lists are used in:
- Round-robin CPU scheduling (প্রতিটি প্রসেস পালা করে সময় পায়)
- Multiplayer game turn management
- Circular buffers / streaming data
- Repeat-all mode in music players
- Token ring networks
- The Josephus problem (classic interview question)

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. Why tail.next = head is the defining property.
2. Why insert at end is O(1) here but O(n) in a plain SLL.
3. Why delete at end is still O(n) (No prev pointer).
4. How to avoid infinite loops (Stop at tail or when you return to head).
5. How to detect a cycle in a list (Floyd's slow/fast pointer algorithm).
6. Why the Josephus problem maps naturally onto a CSLL.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Using `while itr:` to traverse.
✔ It never ends; stop at tail or when you come back to head.

❌ Forgetting to update tail.next after changing head.
✔ Every head change must be followed by tail.next = head.

❌ Forgetting the single-node case.
✔ With one node, head == tail and node.next must point to itself; deleting it must reset head and tail to None.

❌ Thinking circular means faster access.
✔ Access and search are still O(n).

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation          | Complexity | Why?                              |
|--------------------|------------|-----------------------------------|
| Access / Index     | O(n)       | Must traverse from head           |
| Search             | O(n)       | Linear scan around the ring       |
| Insert Beginning   | O(1)       | Only head and tail.next change    |
| Insert End         | O(1)       | Tail pointer is already known     |
| Delete Beginning   | O(1)       | Move head, relink tail.next       |
| Delete End         | O(n)       | Must find the second-last node    |
| Length / __len__   | O(n)       | Counts every node (no size field) |
| Iteration          | O(n)       | Stops at tail, O(1) extra memory  |
| is_empty           | O(1)       | Single `head is None` check       |
| Space              | O(n)       | One node + pointer per element    |

==================================================
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

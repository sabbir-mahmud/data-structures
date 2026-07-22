"""
==================================================
Queue (কিউ) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Queue? (Queue কী?)
--------------------------------------------------
- A Queue is a linear data structure that follows the FIFO principle - First In, First Out. (Queue হলো একটি Linear Data Structure, যা FIFO নিয়ম মেনে চলে - যেটি সবার আগে ঢোকে, সেটিই সবার আগে বের হয়।)
- Insertion happens at the REAR, deletion happens at the FRONT. (ডেটা ঢোকে পিছন দিক (Rear) দিয়ে, আর বের হয় সামনের দিক (Front) দিয়ে।)
- Think of a queue at a ticket counter: first come, first served. (টিকিট কাউন্টারের লাইন ভাবো - আগে আসলে আগে পাবে।)

Basic Operations (মূল অপারেশনসমূহ)
--------------------------------------------------
- enqueue -> Add an element at the rear. (পিছনে একটি এলিমেন্ট যোগ করা।)
- dequeue -> Remove and return the front element. (সামনের এলিমেন্ট সরিয়ে ফেরত দেওয়া।)
- peek    -> View the front element without removing it. (না সরিয়ে শুধু সামনের এলিমেন্ট দেখা।)
- is_empty -> Check whether the queue is empty. (Queue খালি কিনা দেখা।)
- size    -> Number of elements currently stored. (বর্তমানে কয়টি এলিমেন্ট আছে।)

--------------------------------------------------
How a Queue Works (Queue কীভাবে কাজ করে)
--------------------------------------------------

enqueue(10), enqueue(20), enqueue(30)

   dequeue                                    enqueue
   (exit)                                     (entry)
      ^                                          |
      |                                          v
   +------+     +------+     +------+     +------+
   |  10  | <-- |  20  | <-- |  30  | <-- | new  |
   +------+     +------+     +------+     +------+
    FRONT                                   REAR

- 10 came in first, so 10 goes out first. (১০ আগে ঢুকেছে, তাই ১০ আগে বের হবে।)
- Both ends are used: one for entry, one for exit. (দুই প্রান্তই ব্যবহার হয় - একটি ঢোকার, একটি বের হওয়ার।)

--------------------------------------------------
Stack vs Queue (Stack বনাম Queue)
--------------------------------------------------
Stack (LIFO)              Queue (FIFO)
-----------------         --------------------------
push/pop same end         enqueue rear, dequeue front
Reverses order            Preserves order
Undo, DFS, recursion      Scheduling, BFS, buffers

     | 3 | <- in/out       in -> | 1 | 2 | 3 | -> out
     | 2 |
     | 1 |

- A stack REVERSES the order, a queue PRESERVES it. (Stack ক্রম উল্টে দেয়, Queue ক্রম ঠিক রাখে।)
- This is exactly why DFS uses a stack and BFS uses a queue. (এই কারণেই DFS-এ Stack আর BFS-এ Queue ব্যবহার হয়।)

--------------------------------------------------
Why NOT a Plain Python List (কেন সাধারণ List ব্যবহার করবে না)
--------------------------------------------------
Using a list: arr.pop(0) removes the front element. (List দিয়ে arr.pop(0) করলে সামনের এলিমেন্ট মুছে যায়।)

Before pop(0):
+----+----+----+----+
| 10 | 20 | 30 | 40 |
+----+----+----+----+

After pop(0) -> every element shifts left! (সব এলিমেন্ট বামে সরে আসে!)
+----+----+----+
| 20 | 30 | 40 |
+----+----+----+
  <--  <--  <--   O(n) shifting

- list.pop(0) and list.insert(0, x) are O(n). (এই দুটি অপারেশন O(n)।)
- collections.deque does both ends in O(1) with no shifting. (deque দুই প্রান্তেই O(1)-এ কাজ করে, কোনো Shift লাগে না।)
- That is why a real queue is built on a deque or a linked list. (তাই সত্যিকারের Queue বানানো হয় deque বা Linked List দিয়ে।)

--------------------------------------------------
Circular Queue Idea (Circular Queue-এর ধারণা)
--------------------------------------------------
In a fixed array, after many dequeues the front slots are wasted. (নির্দিষ্ট Array-তে অনেকবার dequeue করলে সামনের জায়গাগুলো নষ্ট হয়।)

Linear queue (wasted space):
+----+----+----+----+
| XX | XX | 30 | 40 |     XX = freed but unusable
+----+----+----+----+

Circular queue (reuses space):
        front
          |
+----+----+----+----+
| 50 | XX | 30 | 40 |  <- rear wraps around to index 0
+----+----+----+----+
   ^                |
   +----------------+

- Rear wraps using: rear = (rear + 1) % capacity. (Rear ঘুরে আসে মডুলাস ব্যবহার করে।)
- This reuses freed slots and avoids wasted memory. (এতে খালি জায়গা আবার ব্যবহার হয়, মেমরি নষ্ট হয় না।)

--------------------------------------------------
Types of Queues (Queue-এর প্রকারভেদ)
--------------------------------------------------
| Type            | Description                                       |
|-----------------|---------------------------------------------------|
| Simple Queue    | Plain FIFO (সাধারণ FIFO)                          |
| Circular Queue  | Rear wraps around, reuses space                   |
| Deque           | Insert/delete at BOTH ends (দুই দিকেই কাজ করা যায়) |
| Priority Queue  | Highest priority leaves first, not the oldest     |

--------------------------------------------------
Underflow (Underflow বা খালি Queue)
--------------------------------------------------
Dequeue from an empty queue = Underflow. (খালি Queue থেকে dequeue করা = Underflow।)

+------+
|      |  <-- nothing to remove
+------+

- Always check is_empty() before dequeue or peek. (dequeue বা peek করার আগে সবসময় is_empty() চেক করো।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Queues are used in:
- CPU / process scheduling in operating systems
- Printer job queues (আগে পাঠানো কাজ আগে ছাপা হয়)
- Web server request handling
- Breadth-First Search (BFS) in graphs and trees
- Message queues (RabbitMQ, Kafka style systems)
- Real-time data buffers (IO streams, video streaming)
- Call center waiting lines

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. FIFO in one line: first in, first out.
2. Why list.pop(0) is O(n) and deque is O(1) (Shifting vs pointer move).
3. Why BFS needs a queue and DFS needs a stack.
4. What a circular queue solves (Wasted front slots in a fixed array).
5. The difference between a queue and a priority queue (Arrival order vs priority order).
6. How to implement a queue using two stacks (a classic interview question).

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Using list.pop(0) for dequeue.
✔ That is O(n) because everything shifts; use a deque.

❌ Confusing front and rear.
✔ enqueue happens at the REAR, dequeue happens at the FRONT.

❌ Dequeuing without checking if the queue is empty.
✔ Always check is_empty() first to avoid underflow.

❌ Thinking a priority queue is a normal queue.
✔ A priority queue serves by priority, not by arrival order.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation    | Complexity | Why?                               |
|--------------|------------|------------------------------------|
| Enqueue      | O(1)       | Adds at the rear only              |
| Dequeue      | O(1)       | Removes from the front only        |
| Peek / Front | O(1)       | Reads the front element directly   |
| isEmpty      | O(1)       | Just a length check                |
| Size         | O(1)       | Length is tracked internally       |
| Search       | O(n)       | Must scan through all elements     |
| Space        | O(n)       | Stores n elements                  |

==================================================
"""

# Import deque from collections
# deque (double-ended queue) is ideal for implementing queues
# It allows us to add/remove elements from both ends in O(1) time.
from collections import deque


class Queue:
    """Class to represent a Queue using deque"""

    def __init__(self):
        # Initialize an empty deque container for queue elements
        self.container = deque()

    def enqueue(self, data):
        """Add (enqueue) an element at the rear of the queue"""
        # Append element to the left to maintain FIFO order
        self.container.appendleft(data)

    def dequeue(self):
        """Remove (dequeue) the front element from the queue"""
        # Check if queue is empty to avoid underflow
        if self.is_empty():
            return "Queue Underflow"  # Error message if no element exists
        return self.container.pop()  # Removes and returns the rightmost element

    def peek(self):
        """View the front element without removing it"""
        # Check if queue is empty
        if self.is_empty():
            return "Queue is Empty"
        return self.container[-1]  # Rightmost element is the front of the queue

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.container) == 0

    def size(self):
        """Return the number of elements in the queue"""
        return len(self.container)


# ================================
# Example Usage of Queue
# ================================
if __name__ == "__main__":
    q = Queue()

    # Enqueue some stock price data (FIFO order)
    q.enqueue(
        {"company": "Wall Mart", "timestamp": "15 Apr, 11:01 AM", "price": 131.10}
    )
    q.enqueue({"company": "Wall Mart", "timestamp": "15 Apr, 11:02 AM", "price": 132})
    q.enqueue({"company": "Wall Mart", "timestamp": "15 Apr, 11:03 AM", "price": 135})

    # Current size of the queue
    print("Queue size:", q.size())  # Expected: 3

    # Peek at the front element
    print("Front element:", q.peek())  # Expected: First enqueued element

    # Dequeue elements one by one
    print("Dequeued:", q.dequeue())  # Removes first element
    print("Dequeued:", q.dequeue())  # Removes second element
    print("Dequeued:", q.dequeue())  # Removes third element

    # Now queue should be empty
    print("Is queue empty?", q.is_empty())  # Expected: True

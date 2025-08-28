"""
=====================================
Queue Notes
=====================================

What is a Queue?
A queue is a linear data structure that follows the FIFO (First In, First Out) principle:
- The first inserted (enqueued) element is the first to be removed (dequeued).

Basic Operations
- Enqueue → Add an element to the rear of the queue.
- Dequeue → Remove the front element.
- Peek / Front → View the front element without removing it.
- isEmpty → Check if the queue is empty.

Why Use a Queue?
Queues are useful when order matters and processing must happen in the same order as input.

Common Uses:
- Task scheduling (OS process scheduling, printer queue).
- Handling requests in web servers.
- Breadth-First Search (BFS) in graphs/trees.
- Message queues (inter-process communication).
- Real-time data buffers (IO streams, networking).

Pros
- Simple & Fast → Easy to implement with deque.
- Efficient → Enqueue & Dequeue operations are O(1).
- Preserves Order → FIFO ensures fairness.

Cons
- Limited Access → Only front and rear accessible.
- Fixed Size in array-based queues (overflow possible).
- Underflow → Dequeuing from an empty queue.
- Not suitable for random access or searching (O(n)).

Time Complexity (Big-O)
| Operation   | Complexity |
|-------------|------------|
| Enqueue     | O(1) |
| Dequeue     | O(1) |
| Peek / Front| O(1) |
| isEmpty     | O(1) |
| Search      | O(n) |

=====================================
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

"""
=====================================
Stack Notes
=====================================

What is a Stack?
A stack is a linear data structure that follows the LIFO (Last In, First Out) principle:
- The last inserted (pushed) element is the first to be removed (popped).

Basic Operations
- Push → Add an element.
- Pop → Remove the top element.
- Peek / Top → View the top element without removing it.
- isEmpty → Check if the stack is empty.

Why Use a Stack?
Stacks are efficient for managing data where order matters (especially reverse order).

Common Uses:
- Function call management (call stack).
- Undo/Redo in editors.
- Expression evaluation (infix, postfix, prefix).
- Balanced parentheses checking.
- Backtracking (DFS, maze solving).
- Memory management (stack allocation).
- Browser history navigation.

Pros
- Simple & Fast → Easy to implement.
- Efficient → Push & Pop are O(1).
- Memory Efficient (if array-based).
- Widely Used in real-world problems.

Cons
- Limited Access → Only top element accessible.
- Fixed Size in array-based stacks (overflow possible).
- Underflow → Popping from an empty stack.
- Search Costly → Finding requires O(n).

Time Complexity (Big-O)
| Operation   | Complexity |
|-------------|------------|
| Push        | O(1) |
| Pop         | O(1) |
| Peek / Top  | O(1) |
| isEmpty     | O(1) |
| Search      | O(n) |

=====================================
"""

# Import deque from collections
# deque (double-ended queue) is a fast and memory-efficient data structure
# It allows us to append/pop elements from both ends in O(1) time.
from collections import deque


class Stack:
    """Class to represent a Stack using deque"""

    def __init__(self):
        # Initialize an empty deque container for stack elements
        self.container = deque()

    def push(self, data):
        """Add (push) an element onto the stack"""
        # Append adds the element to the right end (top of the stack)
        self.container.append(data)

    def pop(self):
        """Remove (pop) the top element from the stack"""
        # Check if stack is empty to avoid underflow
        if self.is_empty():
            return "Stack Underflow"  # Error message if no element exists
        return self.container.pop()  # Removes and returns the last element

    def peek(self):
        """View the top element without removing it"""
        # Check if stack is empty
        if self.is_empty():
            return "Stack is Empty"  # Error message if no element exists
        return self.container[-1]  # Return last element (top of stack)

    def is_empty(self):
        """Check if the stack is empty"""
        # Returns True if stack has no elements
        return len(self.container) == 0

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.container)


# ================================
# Example Usage of Stack
# ================================
if __name__ == "__main__":
    # Create a new Stack instance
    st = Stack()

    # Initial check → stack should be empty
    print("Is stack empty?", st.is_empty())  # Expected: True

    # Sample array of elements to push
    arr = [5, 6, 9, 11]

    # Push elements from arr into the stack
    for i in arr:
        st.push(i)
        print(f"Pushed {i} → Current Size: {st.size()}")

    # Now stack should not be empty
    print("Is stack empty?", st.is_empty())  # Expected: False

    # Pop an element (removes 11 since it was last pushed)
    print("Popped:", st.pop())  # Expected: 11

    # Peek at the current top element (should be 9)
    print("Top element (peek):", st.peek())  # Expected: 9

    # Check current size
    print("Current stack size:", st.size())  # Expected: 3

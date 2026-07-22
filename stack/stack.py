"""
==================================================
Stack (স্ট্যাক) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Stack? (Stack কী?)
--------------------------------------------------
- A Stack is a linear data structure that follows the LIFO principle - Last In, First Out. (Stack হলো একটি Linear Data Structure, যা LIFO নিয়ম মেনে চলে - যেটি সবার শেষে ঢোকে, সেটিই সবার আগে বের হয়।)
- Insertion and deletion happen at ONE end only, called the TOP. (ডেটা ঢোকানো এবং বের করা শুধু একটি প্রান্ত দিয়েই হয়, যাকে বলা হয় Top।)
- Think of a stack of plates: the last plate you put on is the first one you take off. (থালার স্তূপ ভাবো - সবার উপরে যেটি রাখবে, সেটিই আগে তুলে নেবে।)

Basic Operations (মূল অপারেশনসমূহ)
--------------------------------------------------
- push  -> Add an element on top. (উপরে একটি এলিমেন্ট বসানো।)
- pop   -> Remove and return the top element. (উপরের এলিমেন্ট সরিয়ে ফেরত দেওয়া।)
- peek  -> View the top element without removing it. (না সরিয়ে শুধু উপরের এলিমেন্ট দেখা।)
- is_empty -> Check whether the stack is empty. (Stack খালি কিনা দেখা।)
- size  -> Number of elements currently stored. (বর্তমানে কয়টি এলিমেন্ট আছে।)

--------------------------------------------------
How a Stack Works (Stack কীভাবে কাজ করে)
--------------------------------------------------

push(5), push(6), push(9), push(11)

        push                pop
         |                   ^
         v                   |
     +------+            +------+
     |  11  | <-- TOP    |  11  | <-- removed first
     +------+            +------+
     |   9  |            |   9  |
     +------+            +------+
     |   6  |            |   6  |
     +------+            +------+
     |   5  | <-- BOTTOM |   5  | <-- removed last
     +------+            +------+

- Both push and pop touch only the TOP. (push এবং pop দুটোই শুধু Top-এ কাজ করে।)
- Nothing shifts, so both are O(1). (কোনো ডেটা সরাতে হয় না, তাই দুটোই O(1)।)
- The bottom element is the hardest to reach. (নিচের এলিমেন্টে পৌঁছানো সবচেয়ে কঠিন।)

--------------------------------------------------
LIFO in Action - Reversing (LIFO দিয়ে উল্টানো)
--------------------------------------------------
Input order  : 5, 6, 9, 11   (ঢোকানোর ক্রম)
Output order : 11, 9, 6, 5   (বের হওয়ার ক্রম)

- A stack naturally reverses the order of data. (Stack স্বাভাবিকভাবেই ডেটার ক্রম উল্টে দেয়।)
- This is why it is used for undo, backtracking and reversing strings. (এই কারণেই Undo, Backtracking এবং String উল্টাতে এটি ব্যবহার হয়।)

--------------------------------------------------
Underflow and Overflow (Underflow ও Overflow)
--------------------------------------------------
Underflow -> Popping from an empty stack. (খালি Stack থেকে pop করার চেষ্টা।)

     +------+
     |      |  <-- empty, nothing to pop
     +------+

Overflow -> Pushing into a full fixed-size stack. (নির্দিষ্ট সাইজের Stack ভরে গেলে আবার push করা।)

- Always check is_empty() before pop or peek. (pop বা peek করার আগে সবসময় is_empty() চেক করো।)
- A Python deque grows dynamically, so overflow is not a practical concern here. (Python-এর deque নিজে থেকেই বড় হয়, তাই এখানে Overflow-এর সমস্যা নেই।)

--------------------------------------------------
Why deque and not list? (list-এর বদলে deque কেন?)
--------------------------------------------------
A Python list CAN work as a stack (append/pop at the end are O(1) amortized). (Python List দিয়েও Stack বানানো যায়, শেষে append/pop করলে O(1) Amortized।)

But a list must occasionally resize and copy everything. (কিন্তু List মাঝে মাঝে Resize করে সব ডেটা কপি করে।)

     list resize:  [1|2|3|4] -> allocate bigger -> copy all -> O(n)
     deque       : linked blocks -> no full copy -> true O(1)

- deque is a doubly linked list of blocks, so push/pop at both ends is truly O(1). (deque হলো ব্লকের একটি Doubly Linked গঠন, তাই দুই প্রান্তেই O(1)।)
- deque never pays a big copy cost. (deque-কে কখনো বড় কপির খরচ দিতে হয় না।)
- For a pure stack, list is fine too; deque is safer for both-end use. (শুধু Stack-এর জন্য List-ও ভালো; দুই প্রান্তে কাজ করলে deque নিরাপদ।)

--------------------------------------------------
Recursion IS a Stack (Recursion আসলে একটি Stack)
--------------------------------------------------
Every function call is pushed onto the CALL STACK. (প্রতিটি Function Call, Call Stack-এ push হয়।)

factorial(3)
  -> factorial(2)
       -> factorial(1)

Call stack while running:        Then it unwinds (তারপর খালি হয়):

  +---------------+                +---------------+
  | factorial(1)  | <- TOP         |               | returns 1
  +---------------+                +---------------+
  | factorial(2)  |                | factorial(2)  | returns 2
  +---------------+                +---------------+
  | factorial(3)  |                | factorial(3)  | returns 6
  +---------------+                +---------------+

- Each frame stores local variables and the return address. (প্রতিটি Frame এ Local Variable ও ফেরার ঠিকানা থাকে।)
- Too many frames -> RecursionError / stack overflow. (অনেক বেশি Frame হলে Stack Overflow হয়।)
- Python's default recursion limit is around 1000. (Python-এর ডিফল্ট সীমা প্রায় ১০০০।)
- ANY recursive solution can be rewritten iteratively using an explicit stack. (যেকোনো Recursive সমাধান একটি Stack দিয়ে Iterative ভাবে লেখা যায়।)

--------------------------------------------------
Classic Problem: Balanced Parentheses (ব্যালান্সড ব্র্যাকেট)
--------------------------------------------------
Check whether every opening bracket has a matching closing one. (প্রতিটি খোলা বন্ধনীর সঠিক বন্ধ বন্ধনী আছে কিনা দেখা।)

Input: ( [ ] )

  read '('  -> push        stack: [ (        ]
  read '['  -> push        stack: [ ( [      ]
  read ']'  -> pop '['     matches -> ok (মিলে গেছে)
  read ')'  -> pop '('     matches -> ok (মিলে গেছে)
  end       -> stack empty -> BALANCED (ব্যালান্সড)

Input: ( ]
  read '('  -> push
  read ']'  -> pop '(' -> does NOT match -> NOT BALANCED (মেলে না)

Rules: (নিয়ম:)
- Opening bracket -> push. (খোলা বন্ধনী হলে push করো।)
- Closing bracket -> pop and compare. (বন্ধ বন্ধনী হলে pop করে মেলাও।)
- Pop on an empty stack -> unbalanced. (খালি Stack-এ pop করতে হলে ব্যালান্সড নয়।)
- Leftover items at the end -> unbalanced. (শেষে কিছু বাকি থাকলে ব্যালান্সড নয়।)

Time O(n), Space O(n). (সময় O(n), জায়গা O(n)।)

--------------------------------------------------
Array-based vs Linked-List-based Stack (দুই ধরনের Stack)
--------------------------------------------------
| Feature          | Array-based    | Linked-List-based |
|------------------|----------------|-------------------|
| Push / Pop       | O(1) amortized | O(1)              |
| Memory           | Contiguous     | Scattered         |
| Cache Friendly   | Yes            | No                |
| Overflow         | Possible       | Only if RAM ends  |
| Extra Memory     | Unused slots   | Pointer per node  |
| Resize Cost      | O(n) sometimes | Never             |

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Stacks are used in:
- Function call management (the call stack)
- Undo / Redo in editors (শেষ কাজটিই আগে বাতিল হয়)
- Expression evaluation (infix, postfix, prefix)
- Balanced parentheses checking
- Backtracking (DFS, maze solving, N-Queens)
- Browser back button history
- Recursion (internally uses the call stack)
- Syntax parsing in compilers

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. LIFO in one line: last in, first out.
2. Why push/pop are O(1) (Only the top changes, nothing shifts).
3. Why search is O(n) (You must pop or scan through everything).
4. Underflow vs Overflow and how to guard against them.
5. That recursion is really a stack (the call stack), so any recursive solution can be rewritten iteratively with a stack.
6. Classic problems: balanced brackets, next greater element, min-stack in O(1), infix to postfix.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Popping without checking if the stack is empty.
✔ Always check is_empty() first to avoid underflow.

❌ Confusing peek with pop.
✔ peek only LOOKS; pop REMOVES.

❌ Thinking you can access the middle of a stack in O(1).
✔ Only the top is reachable in O(1); anything else is O(n).

❌ Using list.pop(0) or insert(0, x) to build a stack.
✔ That is O(n); use append/pop at the END, or a deque.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation   | Complexity | Why?                                |
|-------------|------------|-------------------------------------|
| Push        | O(1)       | Adds at the top only                |
| Pop         | O(1)       | Removes from the top only           |
| Peek / Top  | O(1)       | Reads the top element directly      |
| isEmpty     | O(1)       | Just a length check                 |
| Size        | O(1)       | Length is tracked internally        |
| Search      | O(n)       | Must scan through all elements      |
| Space       | O(n)       | Stores n elements                   |

==================================================
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

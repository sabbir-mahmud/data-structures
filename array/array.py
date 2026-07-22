"""
==================================================
Array (অ্যারে) Notes - Bilingual DSA Reference (10/10)
==================================================

What is an Array? (Array কী?)
--------------------------------------------------
- An array is a contiguous block of memory used to store multiple elements. (Array হলো মেমরির একটি পরপর বা Contiguous অংশ, যেখানে একাধিক ডেটা সংরক্ষণ করা হয়।)
- Every element can be accessed using its index. (প্রতিটি ডেটা Index ব্যবহার করে অ্যাক্সেস করা যায়।)
- Traditional arrays store elements of the same data type. (সাধারণত একই ধরণের ডেটা রাখা হয়।)

Python Array (Python-এ Array)
--------------------------------------------------
- Python's most common array-like structure is the list. (Python-এ সবচেয়ে বেশি ব্যবহৃত Array-এর মতো Data Structure হলো List।)
- A Python list is a Dynamic Array.
- Unlike C/C++ arrays, Python lists store references (pointers) to Python objects, not the actual objects themselves. (Python List মূল ডেটার Reference বা Pointer সংরক্ষণ করে।)
- Lists automatically grow and shrink as needed.

--------------------------------------------------
Size vs Capacity (Size বনাম Capacity)
--------------------------------------------------
Size:
- Number of elements currently stored in the array. (বর্তমানে অ্যারেতে কয়টি এলিমেন্ট আছে।)

Capacity:
- Total number of elements that can be stored before resizing. (মেমরিতে মোট কতটি জায়গা বরাদ্দ আছে।)

Example:
Size = 5
Capacity = 8

+----+----+----+----+----+----+----+----+
| 1  | 2  | 3  | 4  | 5  |    |    |    |
+----+----+----+----+----+----+----+----+
Used = 5
Free = 3

Python reserves extra memory so appending new elements usually doesn't require resizing immediately. (Python অতিরিক্ত মেমরি Reserve করে রাখে যাতে বারবার Resize করতে না হয়।)

--------------------------------------------------
How Data is Stored in Memory (মেমরিতে ডেটা কীভাবে সংরক্ষণ হয়)
--------------------------------------------------
Traditional Array (C/C++)

Index :  0    1    2    3
Value : 10   20   30   40

Memory:
+----+----+----+----+
|10  |20  |30  |40  |
+----+----+----+----+

- Elements are stored one after another (contiguous memory). (ডেটা মেমরিতে পরপর থাকে।)
- Address of any element is calculated using:

Address = Base Address + (Index × Element Size)

Example:
Base Address = 1000
Element Size = 4 bytes

Index 0 -> 1000
Index 1 -> 1004
Index 2 -> 1008
Index 3 -> 1012

This is why array indexing is O(1). (এই কারণেই Array-এর Index-এ পৌঁছাতে O(1) সময় লাগে।)

--------------------------------------------------
Why Arrays are Cache-Friendly (Array কেন Cache-Friendly?)
--------------------------------------------------
Because array elements are stored in contiguous memory, the CPU loads nearby elements into the CPU cache together.
(Contiguous Memory হওয়ার কারণে CPU একসাথে মেমরি থেকে ডেটা Cache-এ নিয়ে আসতে পারে।)

Memory
+----+----+----+----+----+----+
| 1  | 2  | 3  | 4  | 5  | 6  |
+----+----+----+----+----+----+

CPU Cache
+-----------------------+
| 1 | 2 | 3 | 4 | 5 | 6 |
+-----------------------+

Benefits: Faster traversal, Better CPU performance. (খুব দ্রুত কাজ করে।)
* Linked Lists are not cache-friendly because nodes are scattered.

--------------------------------------------------
Python List Memory (Python List মেমরিতে কীভাবে থাকে)
--------------------------------------------------
Python list stores references instead of actual values.

Example: numbers = [10, 20, 30]

List Memory:
+------+-------+-------+
|  *   |   *   |   *   |
+------+-------+-------+
   |        |       |
   v        v       v
  10       20      30

Each "*" is a pointer (reference) to a Python object. (এখানে * হলো একটি Reference। List সরাসরি ডেটা রাখে না, ডেটার লোকেশন রাখে।)

--------------------------------------------------
Python Objects vs C Arrays (Python Object-এর মেমরি)
--------------------------------------------------
C Array Stores raw integers. (সরাসরি সংখ্যা রাখে।)

Python List: Each integer is a full Python object. (প্রতিটি সংখ্যা একটি Object।)
Every object stores:
- Value
- Type information
- Reference count
- Object metadata

Therefore, Python lists use significantly more memory than C arrays. (তাই Python List অনেক বেশি মেমরি ব্যবহার করে।)

--------------------------------------------------
How Dynamic Array Allocates Memory (নতুন Memory কীভাবে Allocate করে)
--------------------------------------------------
Initially:
Capacity = 4, Size = 4
+----+----+----+----+
| 1  | 2  | 3  | 4  |
+----+----+----+----+

Append(5) -> Current array is full. Python allocates a larger block of memory. (অ্যারে ফুল হলে বড় মেমরি ব্লক নেয়।)

CPython does NOT simply double. The real formula is: (CPython শুধু দ্বিগুণ করে না, আসল সূত্রটি হলো:)

    new_capacity = (new_size + (new_size >> 3) + 6) rounded down to a multiple of 4

- The (new_size >> 3) part is what gives the famous ~1.125x growth. (এই অংশটিই বিখ্যাত ~1.125x বৃদ্ধি দেয়।)
- The + 6 constant makes SMALL lists grow much faster than 1.125x. (কিন্তু + 6 অংশটি ছোট List-কে 1.125x-এর চেয়ে অনেক দ্রুত বাড়ায়।)
- So 1.125x is only the ASYMPTOTIC rate, true for large lists. (তাই 1.125x শুধু বড় List-এর ক্ষেত্রে প্রযোজ্য।)

Real CPython capacity sequence: (আসল CPython Capacity ক্রম:)
    0, 4, 8, 16, 24, 32, 40, 52, 64, 76, 92, ...
       ^--^--^  small lists nearly double (ছোট List প্রায় দ্বিগুণ হয়)
                  later growth slows to ~1.125x (পরে বৃদ্ধি কমে ~1.125x হয়)

Here size 4 is full, so new_size = 5 -> (5 + 0 + 6) = 11 -> rounded to 8. (তাই Capacity 4 থেকে 8 হয়।)
+----+----+----+----+----+----+----+----+
| 1  | 2  | 3  | 4  |    |    |    |    |
+----+----+----+----+----+----+----+----+

Copy all existing elements, then add 5. (পুরোনো ডেটা কপি করে নতুন ডেটা বসায়।)
+----+----+----+----+----+----+----+----+
| 1  | 2  | 3  | 4  | 5  |    |    |    |
+----+----+----+----+----+----+----+----+

Old memory is released by the garbage collector.

Because resizing doesn't happen on every append, append() is O(1) amortized. (সবসময় Resize হয় না, তাই Append এর Complexity O(1) Amortized.)

--------------------------------------------------
Why Insert/Delete in Middle is O(n) (মাঝখানে Insert/Delete কেন O(n)?)
--------------------------------------------------
Original:
Index : 0  1  2  3  4
Value : 1  2  3  4  5

Insert 9 at index 2:
1  2  9  3  4  5

Elements shifted: (বাকি ডেটাগুলোকে ডানদিকে সরাতে হয়।)
3 -> Shift right
4 -> Shift right
5 -> Shift right

Worst Case: Insert at beginning (শুরুতে বসালে) -> All elements shift.
Therefore, Time Complexity = O(n).

--------------------------------------------------
Static vs Dynamic Arrays (স্ট্যাটিক বনাম ডায়নামিক অ্যারে)
--------------------------------------------------
Static Array: Fixed size, memory allocated once, cannot grow. (নির্দিষ্ট সাইজ, একবারই মেমরি বরাদ্দ হয়, বড় করা যায় না।)
Dynamic Array: Grows automatically, keeps spare capacity, copies on resize. (নিজে থেকেই বড় হয়, বাড়তি জায়গা রাখে, Resize-এর সময় কপি করে।)

| Feature          | Static Array (C/C++) | Dynamic Array (Python list) |
|------------------|----------------------|-----------------------------|
| Size             | Fixed at compile time| Grows at runtime            |
| Resize           | Not possible         | Automatic                   |
| Extra capacity   | None                 | Yes (spare slots)           |
| Append cost      | N/A                  | O(1) amortized              |
| Memory overhead  | Lowest               | Higher (unused slots)       |
| Speed            | Fastest              | Slightly slower             |

--------------------------------------------------
Array vs Linked List (পার্থক্য)
--------------------------------------------------
| Feature              | Array         | Linked List   |
|----------------------|---------------|---------------|
| Random Access        | O(1)          | O(n)          |
| Insert Beginning     | O(n)          | O(1)          |
| Delete Beginning     | O(n)          | O(1)          |
| Insert End           | O(1) amortized| O(1)          |
| Search               | O(n)          | O(n)          |
| Cache Friendly       | Yes           | No            |
| Memory Usage         | Lower         | Higher        |
| Contiguous Memory    | Yes           | No            |

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Arrays are used in:
- Image processing (pixels)
- Matrices / Math
- Dynamic Programming tables
- Hash Tables (internal buckets)
- Stacks & Queues

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. Why indexing is O(1) (Address calculation).
2. Why insert/delete in the middle is O(n) (Element shifting).
3. Why append() is amortized O(1) (Resizes occasionally, not always).
4. Difference between size and capacity.
5. Why arrays are cache-friendly (Contiguous memory).
6. Why Python lists use more memory (They store object references, not raw data).

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Thinking Python List is a Linked List.
✔ Python List is a Dynamic Array.

❌ Thinking append() is always O(1).
✔ It is O(1) amortized.

❌ Thinking Python stores integers directly in the list.
✔ The list stores references to integer objects.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation          | Complexity     | Why?                       |
|--------------------|----------------|----------------------------|
| Access             | O(1)           | Direct address calculation |
| Update             | O(1)           | Direct access              |
| Append             | O(1) Amortized | Usually empty capacity     |
| Resize             | O(n)           | Copy all elements          |
| Insert Beginning   | O(n)           | Shift elements right       |
| Delete Beginning   | O(n)           | Shift elements left        |
| Insert/Del Middle  | O(n)           | Shift elements             |
| Search / Traverse  | O(n)           | Linear scan                |

==================================================
"""

# ================================
# Basic Usages of Python Lists (Arrays)
# ================================
arr = [1, 2, 3, 4, 5]
print(f"Original array: {arr}")

# Append element at the end
arr.append(6)
print(f"After append: {arr}")

# Insert element at a specific index
arr.insert(2, 99)  # Insert 99 at index 2
print(f"After inserting 99 at index 2: {arr}")

# Remove element by value
arr.remove(99)
print(f"After removing 99: {arr}")

# Remove last element using pop
last = arr.pop()
print(f"After pop (removed {last}): {arr}")

# Slice array
print(f"Slice from index 1 to 3: {arr[1:4]}")

# Reverse the array
arr.reverse()
print(f"After reverse: {arr}")

# Sort the array
arr.sort()
print(f"After sort: {arr}")


# ================================
# Exercise 01: Monthly Expenses
# ================================
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

# 1. Extra spent in Feb compared to Jan
extra_feb = monthly_expenses[1] - monthly_expenses[0]
print(f"Extra spent in Feb compared to Jan: {extra_feb} dollars")

# 2. Total expenses in Q1 (Jan, Feb, Mar)
q1_expenses = sum(monthly_expenses[:3])
print(f"Total expenses in Q1: {q1_expenses} dollars")

# 3. Check if exactly $2000 was spent in any month
if 2000 in monthly_expenses:
    print("Found a month with exactly $2000 spent")
else:
    print("No month with exactly $2000 spent")

# 4. Add June expense of $1980
monthly_expenses.append(1980)
print(f"Expenses after adding June: {monthly_expenses}")

# 5. April refund of $200
monthly_expenses[3] -= 200
print(f"Expenses after April refund: {monthly_expenses}")


# ================================
# Exercise 02: Heroes List
# ================================
heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# 1. Length of the list
print(f"Number of heroes: {len(heroes)}")

# 2. Add "black panther" at end
heroes.append("black panther")
print(f"Heroes after adding 'black panther': {heroes}")

# 3. Move "black panther" after "hulk"
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(f"Heroes after rearranging: {heroes}")

# 4. Replace "thor" and "hulk" with "doctor strange"
heroes[1:3] = ["doctor strange"]
print(f"Heroes after replacement: {heroes}")

# 5. Sort alphabetically
heroes.sort()
print(f"Heroes sorted alphabetically: {heroes}")


# ================================
# Exercise 03: Odd Numbers List
# ================================
# Generate all odd numbers up to a user-specified max
max_num = int(input("Enter the max number: "))
odd_numbers = [i for i in range(1, max_num + 1) if i % 2 != 0]
print(f"Odd numbers up to {max_num}: {odd_numbers}")
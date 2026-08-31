"""
## What is an Array?

English:
An array is a contiguous block of memory used to store multiple elements. Each element can be accessed using an index. Traditional arrays usually store elements of the same data type. However, Python's list can store elements of different data types.

বাংলা (BN):
Array হলো memory-এর একটি contiguous block, যেখানে একাধিক element store করা হয়। প্রতিটি element-কে index ব্যবহার করে access করা যায়। Traditional array সাধারণত একই data type-এর element store করে। তবে Python-এর list-এ বিভিন্ন data type-এর element store করা যায়।

---

## Types of Array

Arrays are commonly divided into two types:

### 1. Static Array

English:
A static array has a fixed capacity. Once its capacity is full, adding a new element can raise an error or require creating a new array.

বাংলা (BN):
Static array-এর capacity fixed থাকে। Capacity পূর্ণ হয়ে গেলে নতুন element add করলে error হতে পারে অথবা নতুন array তৈরি করতে হয়।

### 2. Dynamic Array

English:
A dynamic array can automatically resize when its capacity becomes full. It allocates a larger memory block and copies the existing elements into the new memory.

A common growth strategy is:
New Capacity = Old Capacity + (Old Capacity × 2)

However, Python's list uses a more sophisticated over-allocation strategy rather than simply doubling its capacity.

বাংলা (BN):
Dynamic array-এর capacity পূর্ণ হয়ে গেলে এটি automatically resize হতে পারে। তখন বড় memory block allocate করে existing element-গুলো নতুন memory-তে copy করা হয়।

একটি সাধারণ growth strategy হলো:
New Capacity = Old Capacity + (Old Capacity × 2)

তবে Python-এর list শুধু capacity double করে না; এটি আরও sophisticated over-allocation strategy ব্যবহার করে।

---

# Big O — Complexity

| Operation | Complexity | Why? |
|---|---|---|
| Access | O(1) | Direct index-based access |
| Update | O(1) | Direct index-based access |
| Append | O(1) Amortized | Usually there is available capacity |
| Resize | O(n) | Existing elements must be copied |
| Insert Beginning | O(n) | Elements must be shifted right |
| Delete Beginning | O(n) | Elements must be shifted left |
| Insert Middle | O(n) | Elements must be shifted |
| Delete Middle | O(n) | Elements must be shifted |
| Search / Traverse | O(n) | Linear scan may be required |

## Complexity Explanation

English:

- O(1): Accessing or updating an element by index is constant time.
- O(1) Amortized: Most append operations are O(1), but occasionally resizing requires O(n).
- O(n): Insertion/deletion at the beginning or middle requires shifting elements.
- O(n): Searching an unsorted array may require checking every element.

বাংলা (BN):

- O(1): Index ব্যবহার করে element access বা update করতে constant time লাগে।
- O(1) Amortized: বেশিরভাগ append operation O(1), কিন্তু মাঝে মাঝে resize করার জন্য O(n) সময় লাগে।
- O(n): Beginning বা middle-এ insert/delete করলে element shift করতে হয়।
- O(n): Unsorted array-তে search করার সময় প্রতিটি element check করতে হতে পারে।

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
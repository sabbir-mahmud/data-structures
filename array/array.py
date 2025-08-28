"""
=====================================
Array Notes
=====================================

What is an Array in Python?
- Python's most common array-like structure is the list, which is dynamic.
- Lists automatically resize when elements are added or removed.
- The array module exists for type-restricted arrays but is less common.

Static vs Dynamic Arrays
- Static Array: Fixed size; requires predefined memory; resizing means creating a new array.
- Dynamic Array (Python list): Flexible size; automatically resizes; may copy elements during resize.

Pros (Dynamic Arrays)
- Flexible and easy to use.
- Simple insertion and deletion.
- Many built-in methods.

Cons
- More memory overhead.
- Slower for certain operations due to resizing and dynamic typing.

Time Complexity (Big-O for Python Lists)
| Operation            | Complexity |
|----------------------|------------|
| Access by index      | O(1) |
| Append               | O(1) amortized |
| Insert/Delete at end | O(1) amortized |
| Insert/Delete middle | O(n) |
| Search               | O(n) |

=====================================
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

"""
Python Array Overview:
- Python's most common array-like structure is the **list**, which is dynamic.
- Lists automatically resize when elements are added or removed.
- The `array` module exists for type-restricted arrays but is less common.

Static vs Dynamic Arrays:
- Static Array: Fixed size; requires predefined memory; resizing means creating a new array.
- Dynamic Array (Python list): Flexible size; automatically resizes; may copy elements during resize.

Pros (Dynamic Arrays):
1. Flexible and easy to use.
2. Simple insertion and deletion.
3. Many built-in methods.

Cons:
1. More memory overhead.
2. Slower for certain operations due to resizing and dynamic typing.

Big-O Complexity (Lists):
- Access by index: O(1)
- Append: O(1) amortized
- Insert/Delete at end: O(1) amortized
- Insert/Delete in middle: O(n)
- Search: O(n)
"""

# Basic usages of Python lists (arrays)
arr = [1, 2, 3, 4, 5]
print(f"Original array: {arr}")

# Append element
arr.append(6)
print(f"After append: {arr}")

# Insert element at index
arr.insert(2, 99)
print(f"After inserting 99 at index 2: {arr}")

# Remove element by value
arr.remove(99)
print(f"After removing 99: {arr}")

# Remove last element
last = arr.pop()
print(f"After pop (removed {last}): {arr}")

# Slice
print(f"Slice from index 1 to 3: {arr[1:4]}")

# Reverse
arr.reverse()
print(f"After reverse: {arr}")

# Sort
arr.sort()
print(f"After sort: {arr}")

"""
Exercise: Array Data Structure
Monthly expenses:
    Jan - 2200, Feb - 2350, Mar - 2600, Apr - 2130, May - 2190
Tasks:
1. Feb extra spent compared to Jan.
2. Total expense in Q1.
3. Check if $2000 spent in any month.
4. Add June expense of $1980.
5. April refund of $200.

Marvel heroes:
    ['spider man','thor','hulk','iron man','captain america']
Tasks:
1. List length.
2. Add 'black panther' at end.
3. Move 'black panther' after 'hulk'.
4. Replace 'thor' and 'hulk' with 'doctor strange'.
5. Sort alphabetically.

Odd numbers list:
    Generate all odd numbers up to a user-specified max.
"""

# Exercise 01: Monthly Expenses
monthly_expenses = [2200, 2350, 2600, 2130, 2190]
extra_feb = monthly_expenses[1] - monthly_expenses[0]
print(f"Extra spent in Feb compared to Jan: {extra_feb} dollars")

q1_expenses = sum(monthly_expenses[:3])
print(f"Total expenses in Q1: {q1_expenses} dollars")

print(
    "Found a month with exactly $2000 spent"
    if 2000 in monthly_expenses
    else "No month with exactly $2000 spent"
)

monthly_expenses.append(1980)
print(f"Expenses after adding June: {monthly_expenses}")

monthly_expenses[3] -= 200
print(f"Expenses after April refund: {monthly_expenses}")

# Exercise 02: Heroes List
heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]
print(f"Number of heroes: {len(heroes)}")

heroes.append("black panther")
print(f"Heroes after adding 'black panther': {heroes}")

heroes.remove("black panther")
heroes.insert(3, "black panther")
print(f"Heroes after rearranging: {heroes}")

heroes[1:3] = ["doctor strange"]
print(f"Heroes after replacement: {heroes}")

heroes.sort()
print(f"Heroes sorted alphabetically: {heroes}")

# Exercise 03: Odd Numbers List
max_num = int(input("Enter the max number: "))
odd_numbers = [i for i in range(1, max_num + 1) if i % 2 != 0]
print(f"Odd numbers up to {max_num}: {odd_numbers}")

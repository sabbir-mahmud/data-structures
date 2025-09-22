"""
=====================================
Binary Search Tree (BST) Notes
=====================================

What is a Binary Search Tree (BST)?
A Binary Search Tree is a **node-based hierarchical data structure** where:
- Each node has at most two children → Left & Right.
- Left subtree contains only nodes with values **less than the parent**.
- Right subtree contains only nodes with values **greater than the parent**.
- No duplicate nodes (in classic BST definition).

Basic Operations
- Insert / Add → Add a new node while maintaining BST property.
- Search → Check if a value exists in the tree.
- Delete / Remove → Remove a node (3 cases: leaf, one child, two children).
- Traversals → Inorder, Preorder, Postorder.
- Find Min → Leftmost node.
- Find Max → Rightmost node.
- Calculate Sum → Sum of all node values.

Why Use a BST?
- Maintains sorted order of elements.
- Efficient searching, insertion, and deletion.
- Provides structured hierarchical storage.

Common Uses:
- Efficient searching (dictionary, phonebook).
- Sorting (inorder traversal gives ascending order).
- Range queries (find values between two numbers).
- Auto-suggestions (prefix trees derived from BST logic).
- Symbol tables in compilers.
- Database indexing.

Pros
- Efficient searching and insertion (O(log n) in average case).
- Maintains sorted order automatically.
- Useful for dynamic datasets (data changes over time).
- Supports ordered operations (min, max, range search).

Cons
- Becomes skewed (like a linked list) if not balanced → O(n) worst case.
- Balancing not automatic (need AVL, Red-Black Trees for that).
- Extra memory for storing links (left/right pointers).

Time Complexity (Big-O)
| Operation          | Average Case | Worst Case (Skewed) |
|--------------------|--------------|----------------------|
| Insert (Add)       | O(log n)     | O(n) |
| Search             | O(log n)     | O(n) |
| Delete (Remove)    | O(log n)     | O(n) |
| Find Min/Max       | O(log n)     | O(n) |
| Traversal (In/Pre/Post) | O(n)   | O(n) |
| Calculate Sum      | O(n)         | O(n) |

=====================================
"""

from collections import deque


class BinarySearchTreeNode:
    """Class to represent a Binary Search Tree (BST)"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """Insert a new node while maintaining BST property"""
        if self.data == data:  # Duplicates not allowed
            return

        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, value):
        """Search for a value in the BST"""
        if self.data == value:
            return True

        if value < self.data:
            return self.left.search(value) if self.left else False

        if value > self.data:
            return self.right.search(value) if self.right else False

    def find_min(self):
        """Find the minimum value in the BST (leftmost node)"""
        return self.left.find_min() if self.left else self.data

    def find_max(self):
        """Find the maximum value in the BST (rightmost node)"""
        return self.right.find_max() if self.right else self.data

    def calculate_sum(self):
        """Calculate sum of all node values"""
        return sum(self.in_order_traversal())

    def remove(self, value):
        """Remove a node from the BST"""
        if value < self.data:
            if self.left:
                self.left = self.left.remove(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.remove(value)

        else:
            # Case 1: No children (leaf node)
            if self.left is None and self.right is None:
                return None
            # Case 2: One child
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # Case 3: Two children
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.remove(min_val)

        return self

    def in_order_traversal(self):
        """Inorder traversal (Left → Root → Right) → Sorted order"""
        result = []
        if self.left:
            result += self.left.in_order_traversal()
        result.append(self.data)
        if self.right:
            result += self.right.in_order_traversal()
        return result

    def pre_order_traversal(self):
        """Preorder traversal (Root → Left → Right)"""
        result = [self.data]
        if self.left:
            result += self.left.pre_order_traversal()
        if self.right:
            result += self.right.pre_order_traversal()
        return result

    def post_order_traversal(self):
        """Postorder traversal (Left → Right → Root)"""
        result = []
        if self.left:
            result += self.left.post_order_traversal()
        if self.right:
            result += self.right.post_order_traversal()
        result.append(self.data)
        return result

    def breadth_first_traversal(self):
        results = []
        queue = deque([self])

        while queue:
            node = queue.popleft()
            results.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return results


# ================================
# Example Usage of BST
# ================================
if __name__ == "__main__":
    arr = [96, 1, 5, 1, 3, 5, 9, 12, 36, 25, 48, 88, 88, 96]

    # Create BST root node
    root = BinarySearchTreeNode(arr[0])

    # Insert elements into BST
    for i in arr[1:]:
        root.add_child(i)

    print("Breadth-First Traversal:", root.breadth_first_traversal())
    print("DFS --> In order Traversal (sorted):", root.in_order_traversal())
    print("DFS --> Pre order Traversal:", root.pre_order_traversal())
    print("DFS --> Post order Traversal:", root.post_order_traversal())
    print("Search 88:", root.search(88))
    print("Minimum:", root.find_min())
    print("Maximum:", root.find_max())
    print("Sum of all nodes:", root.calculate_sum())
    root.remove(1)
    print("After removing 1 → In order:", root.in_order_traversal())

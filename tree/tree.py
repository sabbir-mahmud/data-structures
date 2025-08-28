"""
=====================================
Tree (General Tree) Notes
=====================================

What is a TreeNode?
A tree node is a fundamental unit of a tree data structure.
This particular tree is a **General Tree**:
- Each node can have any number of children.
- No strict ordering of children (unlike binary trees).

Common Operations:
- add_child → Add a child node.
- get_level → Determine node depth (root is level 0).
- print_tree → Recursively display the tree.

Why Use a General Tree?
- Hierarchical data representation.
- Flexible for nested structures.
- Useful in file systems, organization charts, UI components.

Pros
- Natural representation of hierarchy.
- Flexible → Nodes can have any number of children.

Cons
- Traversal can be recursive → stack overflow for very deep trees.
- Finding nodes requires traversal → O(n) in general.

Time Complexity:
| Operation      | Complexity |
|----------------|------------|
| add_child      | O(1)       |
| get_level      | O(h)       | (h = height of node)
| print_tree     | O(n)       |
=====================================
"""


class TreeNode:
    """Class to represent a node in a tree"""

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        """Add a child to this node"""
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """Return the depth level of the node"""
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree(self):
        """Recursively print the tree structure"""
        indent = " " * self.get_level() * 4
        prefix = "|__" if self.parent else ""
        print(f"{indent}{prefix}{self.data}")

        for child in self.children:
            child.print_tree()


def build_product_tree():
    """Build and print a sample product tree"""
    root = TreeNode("Electronics")

    # Laptop subtree
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    # Cell Phone subtree
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    # TV subtree
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    # Assemble the full tree
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # Print the tree
    root.print_tree()


if __name__ == "__main__":
    build_product_tree()

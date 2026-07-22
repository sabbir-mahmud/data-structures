r"""
==================================================
Tree / General Tree (ট্রি বা গাছ) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Tree? (Tree কী?)
--------------------------------------------------
- A Tree is a NON-LINEAR, hierarchical data structure. (Tree হলো একটি Non-Linear বা স্তরভিত্তিক Data Structure।)
- Data is stored in a parent-child relationship, not in a straight line. (ডেটা সরলরেখায় নয়, বাবা-সন্তান সম্পর্কে সাজানো থাকে।)
- A General Tree means each node can have ANY number of children. (General Tree মানে প্রতিটি Node-এর যত খুশি সন্তান থাকতে পারে।)
- There is no ordering rule among children (unlike a BST). (সন্তানদের মধ্যে কোনো ক্রম বা নিয়ম নেই, BST-এর মতো নয়।)

Array/Linked List -> Linear (একটার পর একটা)
Tree              -> Hierarchical (স্তরে স্তরে)

--------------------------------------------------
Tree Terminology (Tree-এর পরিভাষা)
--------------------------------------------------

                    [Electronics]          <- Root (মূল, level 0)
                    /     |      \
              [Laptop] [Phone]  [TV]       <- Children (সন্তান, level 1)
              /   |  \            |   \
          [Mac][Surface][Thinkpad][LG][Samsung]  <- Leaves (পাতা, level 2)

- Root      -> The topmost node; it has no parent. (সবার উপরের Node, যার কোনো Parent নেই।)
- Parent    -> A node that has children. (যে Node-এর সন্তান আছে।)
- Child     -> A node directly under a parent. (Parent-এর ঠিক নিচের Node।)
- Siblings  -> Nodes sharing the same parent. (একই Parent-এর সন্তানরা।)
- Leaf      -> A node with no children. (যে Node-এর কোনো সন্তান নেই।)
- Level     -> Distance from the root (root = 0). (Root থেকে দূরত্ব; Root-এর Level 0।)
- Height    -> Longest path from a node down to a leaf. (কোনো Node থেকে পাতা পর্যন্ত সবচেয়ে লম্বা পথ।)
- Depth     -> Distance from the root down to that node. (Root থেকে ঐ Node পর্যন্ত দূরত্ব।)
- Subtree   -> Any node together with all its descendants. (কোনো Node এবং তার সব বংশধর মিলে একটি Subtree।)
- Degree    -> Number of children a node has. (একটি Node-এর সন্তানের সংখ্যা।)
- Edge      -> The link between a parent and a child. (Parent ও Child-এর মধ্যকার সংযোগ।)

* A tree with n nodes always has exactly n-1 edges. (n সংখ্যক Node-এর Tree-তে সবসময় ঠিক n-1টি Edge থাকে।)

--------------------------------------------------
How a Node is Structured (Node-এর গঠন)
--------------------------------------------------
+--------+--------+------------+
|  data  | parent |  children  |
+--------+--------+------------+
    |        |          |
  value   upward     list of
          link       child nodes

- data     -> The actual value. (আসল ডেটা বা মান।)
- parent   -> Reference upward, used to compute the level. (উপরের দিকের Reference, Level হিসাব করতে লাগে।)
- children -> A LIST of child nodes (that is what makes it "general"). (সন্তানদের একটি List - এটিই একে "General" বানায়।)

* A Linked List node has 1 next; a tree node has MANY nexts. (Linked List-এ next একটি, Tree-তে অনেকগুলো।)

--------------------------------------------------
How get_level() Works (get_level কীভাবে কাজ করে)
--------------------------------------------------
We walk UPWARD through parent links and count the steps. (আমরা parent ধরে উপরের দিকে হাঁটি এবং ধাপ গুনি।)

[Mac] -> parent [Laptop] -> parent [Electronics] -> parent None
 count 0          count 1            count 2         stop

Level of "Mac" = 2

- Cost is O(h) where h is the height. (খরচ O(h), যেখানে h হলো Height।)
- The level is used to decide the indentation when printing. (Print করার সময় কতটা ফাঁকা জায়গা দিতে হবে, তা Level দিয়ে ঠিক হয়।)

--------------------------------------------------
Why print_tree() is Recursive (print_tree কেন Recursive)
--------------------------------------------------
Every subtree is itself a tree, so the same function works at every level. (প্রতিটি Subtree নিজেই একটি Tree, তাই একই Function সব স্তরে কাজ করে।)

print_tree(Electronics)
   -> print "Electronics"
   -> print_tree(Laptop)
        -> print "   |__Laptop"
        -> print_tree(Mac)      -> print "      |__Mac"
        -> print_tree(Surface)  -> print "      |__Surface"
   -> print_tree(Phone)
        -> ...

- This is DFS (Depth First Search) - go deep before going wide. (এটি DFS - আগে গভীরে যায়, তারপর পাশে।)
- Total cost O(n) because every node is visited exactly once. (মোট খরচ O(n), কারণ প্রতিটি Node ঠিক একবার করে দেখা হয়।)
- Recursion depth equals the tree height, so a very deep tree can overflow the stack. (Recursion-এর গভীরতা = Tree-এর Height, তাই খুব গভীর Tree-তে Stack Overflow হতে পারে।)

--------------------------------------------------
DFS vs BFS Traversal (দুই ধরনের ভ্রমণ)
--------------------------------------------------
DFS (Depth First) - uses recursion / a stack:
    Electronics -> Laptop -> Mac -> Surface -> Phone -> ...
    Goes as deep as possible first. (আগে যতদূর সম্ভব গভীরে যায়।)

BFS (Breadth First) - uses a queue, level by level:
    Level 0: Electronics
    Level 1: Laptop, Phone, TV
    Level 2: Mac, Surface, Thinkpad, ...
    Finishes one level before moving down. (এক স্তর শেষ করে তারপর নিচে নামে।)

- Use DFS to explore whole branches (file system size, path finding). (পুরো শাখা ঘুরতে DFS ব্যবহার করো।)
- Use BFS to find the shortest path or to work level by level. (সবচেয়ে ছোট পথ বা স্তরভিত্তিক কাজে BFS ব্যবহার করো।)

--------------------------------------------------
General Tree vs Binary Tree (পার্থক্য)
--------------------------------------------------
| Feature            | General Tree        | Binary Tree         |
|--------------------|---------------------|---------------------|
| Children per node  | Any number          | At most 2           |
| Ordering rule      | None                | Left / Right        |
| Storage of kids    | List                | left, right fields  |
| Search             | O(n)                | O(n), O(log n) in BST |
| Typical use        | Hierarchies         | Searching, sorting  |
| Traversal          | DFS / BFS           | In/Pre/Post/Level   |

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
General Trees are used in:
- File systems (folders inside folders)
- Organization charts (CEO -> CTO -> Team Lead -> Developer)
- HTML DOM and UI component trees
- XML / JSON nested documents
- Category trees in e-commerce sites
- Menus and navigation structures
- Family trees

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. That a tree is non-linear and hierarchical, unlike arrays or linked lists.
2. The vocabulary: root, parent, child, sibling, leaf, level, height, depth, subtree.
3. That n nodes always mean n-1 edges.
4. Why a general tree stores children in a LIST while a binary tree uses two fields.
5. Why traversal is O(n) (Every node must be visited).
6. Why get_level is O(h) (It walks up the parent chain).
7. The DFS vs BFS trade-off and which one needs a stack vs a queue.
8. The recursion depth risk on very deep trees.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Confusing height with depth.
✔ Depth counts DOWN from the root; height counts UP from the leaves.

❌ Forgetting to set child.parent when adding a child.
✔ Without the parent link, get_level() can never work.

❌ Thinking a tree gives fast search by default.
✔ A general tree search is O(n); only an ordered tree like a BST gives O(log n).

❌ Assuming every tree node has at most two children.
✔ That is a BINARY tree; a general tree has no such limit.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation      | Complexity | Why?                                |
|----------------|------------|-------------------------------------|
| add_child      | O(1)       | Just appends to the children list   |
| get_level      | O(h)       | Walks up the parent chain           |
| print_tree     | O(n)       | Visits every node once              |
| Search a value | O(n)       | No ordering rule to guide the search|
| Traversal      | O(n)       | Every node is visited once          |
| Space          | O(n)       | One node object per element         |
| Recursion Stack| O(h)       | One frame per level of depth        |

==================================================
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

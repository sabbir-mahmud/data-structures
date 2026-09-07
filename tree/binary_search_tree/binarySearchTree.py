r"""
==================================================
Binary Search Tree (বাইনারি সার্চ ট্রি) Notes - Bilingual DSA Reference (10/10)
==================================================

What is a Binary Search Tree? (BST কী?)
--------------------------------------------------
- A Binary Tree is a tree where each node has AT MOST two children: left and right. (Binary Tree হলো এমন Tree, যেখানে প্রতিটি Node-এর সর্বোচ্চ দুইটি সন্তান থাকে - left এবং right।)
- A Binary SEARCH Tree adds one strict ordering rule. (Binary Search Tree-তে একটি কঠোর ক্রম-নিয়ম যোগ করা হয়।)
- Left subtree < Node < Right subtree, for EVERY node. (প্রতিটি Node-এর জন্য: বাম পাশের সব মান ছোট, ডান পাশের সব মান বড়।)
- Classic BSTs do not allow duplicates. (সাধারণ BST-তে একই মান দুইবার রাখা হয় না।)

This one rule is what turns O(n) searching into O(log n). (এই একটিমাত্র নিয়মই O(n) খোঁজাকে O(log n) বানিয়ে দেয়।)

--------------------------------------------------
The BST Property (BST-এর নিয়ম)
--------------------------------------------------

                     [50]
                    /    \
            smaller /      \ larger
                   /        \
                [30]        [70]
               /    \      /    \
            [20]   [40] [60]   [80]

- Everything in the LEFT subtree is less than 50. (বাম পাশের সবকিছু ৫০-এর চেয়ে ছোট।)
- Everything in the RIGHT subtree is greater than 50. (ডান পাশের সবকিছু ৫০-এর চেয়ে বড়।)
- This rule holds recursively at EVERY node, not just the root. (এই নিয়ম শুধু Root-এ নয়, প্রতিটি Node-এই প্রযোজ্য।)

--------------------------------------------------
Why Search is O(log n) (Search কেন O(log n)?)
--------------------------------------------------
At every step you throw away HALF the tree. (প্রতিটি ধাপে তুমি অর্ধেক Tree বাদ দিয়ে দাও।)

Search 60 in the tree above:

  60 > 50  -> go RIGHT, discard the entire left half (বাম অর্ধেক বাদ)
  60 < 70  -> go LEFT
  60 == 60 -> FOUND (পাওয়া গেছে)

  3 comparisons instead of scanning 7 nodes. (৭টি Node না দেখে মাত্র ৩টি তুলনা।)

n = 1,000,000 nodes -> only about 20 comparisons. (১০ লক্ষ Node-এ মাত্র ~২০টি তুলনা।)

- This is exactly the binary search idea, but in a linked structure. (এটি Binary Search-এর ধারণাই, তবে Linked গঠনে।)
- The cost equals the HEIGHT of the tree, not the number of nodes. (খরচ Node-এর সংখ্যা নয়, Tree-এর Height-এর সমান।)

--------------------------------------------------
The Skewed Tree Problem (স্কিউড ট্রি-এর সমস্যা)
--------------------------------------------------
If you insert already-sorted data, the tree degenerates. (সাজানো ডেটা ঢোকালে Tree বিকৃত হয়ে যায়।)

Insert 10, 20, 30, 40, 50:

    [10]
       \
       [20]
          \
          [30]
             \
             [40]
                \
                [50]      <- this is just a Linked List! (এটি তো একটি Linked List!)

Balanced tree     -> height = log n -> O(log n)
Skewed tree       -> height = n     -> O(n)

- A BST guarantees NOTHING about balance on its own. (BST নিজে থেকে Balance-এর কোনো নিশ্চয়তা দেয় না।)
- Self-balancing trees (AVL, Red-Black) fix this by rotating nodes. (AVL বা Red-Black Tree ঘোরানোর মাধ্যমে এটি ঠিক করে।)
- This is why "O(log n)" is only the AVERAGE case. (এই কারণেই O(log n) শুধু গড় ক্ষেত্রে সত্য।)

--------------------------------------------------
Insertion (Insert কীভাবে হয়)
--------------------------------------------------
Compare with the current node and walk down until you find an empty spot. (বর্তমান Node-এর সাথে তুলনা করে খালি জায়গা না পাওয়া পর্যন্ত নিচে নামো।)

Insert 35 into the tree:      35 < 50 -> left
                              35 > 30 -> right
                              35 < 40 -> left -> empty, place it here

                [50]
               /    \
            [30]    [70]
           /    \
        [20]   [40]
               /
            [35]        <- new node (নতুন Node)

- New nodes are ALWAYS inserted as leaves. (নতুন Node সবসময় পাতা হিসেবেই বসে।)
- Duplicates are simply ignored in this implementation. (এই বাস্তবায়নে একই মান আবার এলে উপেক্ষা করা হয়।)

--------------------------------------------------
The Three Traversals - DFS (তিন ধরনের DFS ভ্রমণ)
--------------------------------------------------
                [50]
               /    \
            [30]    [70]

In-order   (Left -> Root -> Right) : 30, 50, 70   <- SORTED! (সাজানো!)
Pre-order  (Root -> Left -> Right) : 50, 30, 70
Post-order (Left -> Right -> Root) : 30, 70, 50

- In-order gives values in ASCENDING order - the BST's superpower. (In-order ছোট থেকে বড় ক্রমে দেয় - এটিই BST-এর সবচেয়ে বড় শক্তি।)
- Pre-order is used to COPY or serialize a tree (root comes first). (Pre-order দিয়ে Tree কপি বা Serialize করা হয়।)
- Post-order is used to DELETE a tree (children die before the parent). (Post-order দিয়ে Tree মুছে ফেলা হয় - সন্তান আগে, Parent পরে।)
- All three are O(n) because every node is visited once. (তিনটিই O(n), কারণ প্রতিটি Node একবার করে দেখা হয়।)

--------------------------------------------------
Level Order Traversal - BFS (স্তরভিত্তিক ভ্রমণ)
--------------------------------------------------
                [50]              <- Level 0
               /    \
            [30]    [70]          <- Level 1
           /    \
        [20]   [40]               <- Level 2

Output: 50, 30, 70, 20, 40

How it works with a queue: (Queue দিয়ে কীভাবে হয়:)

  queue = [50]           -> pop 50, push its children 30, 70
  queue = [30, 70]       -> pop 30, push 20, 40
  queue = [70, 20, 40]   -> pop 70
  queue = [20, 40]       -> pop 20, pop 40
  queue = []             -> done

- DFS uses a STACK (or recursion); BFS uses a QUEUE. (DFS-এ Stack বা Recursion, BFS-এ Queue লাগে।)
- BFS visits nodes level by level, left to right. (BFS স্তরে স্তরে, বাম থেকে ডানে ঘোরে।)

--------------------------------------------------
Deletion - The Three Cases (ডিলিটের তিনটি অবস্থা)
--------------------------------------------------
Case 1: Leaf node (no children) - just remove it. (পাতা - সরাসরি মুছে দাও।)

        [30]            [30]
       /       ->
    [20]              (removed)

Case 2: One child - the child takes the node's place. (একটি সন্তান - সন্তানই তার জায়গা নেয়।)

        [30]            [30]
       /       ->      /
    [20]            [15]
    /
 [15]

Case 3: Two children - the hard case. (দুইটি সন্তান - কঠিন অবস্থা।)

  1. Find the in-order SUCCESSOR = the smallest value in the right subtree.
     (ডান Subtree-এর সবচেয়ে ছোট মান খুঁজে বের করো।)
  2. Copy that value into the node being deleted. (সেই মানটি এই Node-এ বসাও।)
  3. Delete the successor from the right subtree (it has at most one child).
     (তারপর ডান Subtree থেকে সেই Node-টি মুছে দাও।)

        [50]                     [60]
       /    \                   /    \
    [30]    [70]      ->     [30]    [70]
            /                        /
         [60]                    (removed)

- Why the successor? Because it is the ONLY value that keeps the BST rule intact. (কেন Successor? কারণ একমাত্র সেই মানই BST-এর নিয়ম অক্ষুণ্ণ রাখে।)
- The in-order PREDECESSOR (largest in the left subtree) works equally well. (বাম Subtree-এর সবচেয়ে বড় মান দিয়েও একই কাজ হয়।)

--------------------------------------------------
Find Min and Max (সবচেয়ে ছোট ও বড় মান)
--------------------------------------------------
Min -> keep going LEFT until there is no left child. (যতক্ষণ বাম সন্তান আছে, বামে যেতে থাকো।)
Max -> keep going RIGHT until there is no right child. (যতক্ষণ ডান সন্তান আছে, ডানে যেতে থাকো।)

        [50]
       /    \
    [30]    [70]
   /            \
 [20] <- MIN    [80] <- MAX

- No comparisons are needed at all, just follow one direction. (কোনো তুলনার দরকার নেই, শুধু এক দিকে যেতে থাকো।)
- Cost = O(h) = O(log n) if balanced. (খরচ O(h); Balanced হলে O(log n)।)

--------------------------------------------------
BST vs Array vs Hash Table (পার্থক্য)
--------------------------------------------------
| Feature            | Sorted Array | BST (balanced) | Hash Table   |
|--------------------|--------------|----------------|--------------|
| Search             | O(log n)     | O(log n)       | O(1) average |
| Insert             | O(n)         | O(log n)       | O(1) average |
| Delete             | O(n)         | O(log n)       | O(1) average |
| Min / Max          | O(1)         | O(log n)       | O(n)         |
| Sorted output      | Free         | O(n) in-order  | Must sort    |
| Range queries      | Yes (fast)   | Yes (fast)     | No           |
| Ordered            | Yes          | Yes            | No           |

* Use a hash table for raw speed; use a BST when you also need ORDER. (শুধু গতির জন্য Hash Table; ক্রম দরকার হলে BST।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
BSTs (and their balanced variants) are used in:
- Database indexing (B-Trees / B+ Trees are generalizations)
- File system directory indexes
- Dictionaries and phonebooks (sorted lookup)
- Range queries (find all values between X and Y)
- Auto-complete and prefix suggestions
- Symbol tables in compilers
- Priority scheduling and ordered maps (C++ std::map, Java TreeMap)

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. The BST rule: left < node < right, recursively at every node.
2. Why search is O(log n) (Half the tree is discarded each step).
3. Why the worst case is O(n) (A skewed tree from sorted input).
4. That in-order traversal yields sorted output - the classic BST proof.
5. The three deletion cases, especially the successor trick for two children.
6. Why complexity depends on HEIGHT, not on node count.
7. That AVL / Red-Black trees exist to guarantee balance.
8. DFS needs a stack/recursion, BFS needs a queue.

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Thinking a BST is always O(log n).
✔ Only when balanced; sorted input makes it O(n).

❌ Checking only the immediate children when validating a BST.
✔ EVERY node in the left subtree must be smaller, not just the direct child.

❌ Thinking a binary tree and a binary search tree are the same.
✔ A binary tree only limits children to 2; a BST also enforces ordering.

❌ Picking any random node to replace a deleted node with two children.
✔ You must use the in-order successor (or predecessor) to preserve order.

❌ Forgetting that removal must RETURN the new subtree root.
✔ The parent's link has to be reassigned, e.g. self.left = self.left.remove(x).

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation          | Average  | Worst | Why?                        |
|--------------------|----------|-------|-----------------------------|
| Search             | O(log n) | O(n)  | Halves the tree; skew = list|
| Insert (add_child) | O(log n) | O(n)  | Walks down to a leaf spot   |
| Delete (remove)    | O(log n) | O(n)  | Search plus successor find  |
| Find Min / Max     | O(log n) | O(n)  | Follows one edge to the end |
| In/Pre/Post-order  | O(n)     | O(n)  | Visits every node once      |
| Level order (BFS)  | O(n)     | O(n)  | Visits every node once      |
| Calculate Sum      | O(n)     | O(n)  | Must touch every node       |
| Space              | O(n)     | O(n)  | One node per element        |
| Recursion Stack    | O(log n) | O(n)  | One frame per level         |

==================================================
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

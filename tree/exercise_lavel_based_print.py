"""
==================================================
Tree Exercise: Level Based Print (স্তরভিত্তিক প্রিন্ট) - Bilingual DSA Reference (10/10)
==================================================

The Problem (সমস্যাটি কী?)
--------------------------------------------------
- Build a location hierarchy: Earth -> Country -> State -> District -> City. (একটি অবস্থানভিত্তিক স্তরবিন্যাস তৈরি করো।)
- print(level) must display the tree ONLY up to the given depth. (print(level) শুধু নির্দিষ্ট গভীরতা পর্যন্ত Tree দেখাবে।)
- Deeper nodes must be cut off, not printed. (তার চেয়ে গভীরের Node গুলো বাদ যাবে।)

--------------------------------------------------
The Tree We Are Building (যে Tree টি বানাচ্ছি)
--------------------------------------------------

[Earth]                                 <- Level 0
 |__[Bangladesh]                        <- Level 1
 |    |__[Dhaka Division]               <- Level 2
 |    |    |__[Dhaka District]          <- Level 3
 |    |         |__[Dhaka City]         <- Level 4
 |    |__[Chittagong Division]
 |__[Pakistan]
 |__[Malaysia]

- Each level is a smaller administrative unit. (প্রতিটি স্তর একটি ছোট প্রশাসনিক এলাকা।)
- This is a General Tree: any number of children per node. (এটি General Tree: প্রতিটি Node-এর যত খুশি সন্তান থাকতে পারে।)

--------------------------------------------------
How Level Cutting Works (স্তর কেটে ফেলা কীভাবে কাজ করে)
--------------------------------------------------
Every node knows its own depth via get_level(). (প্রতিটি Node get_level() দিয়ে নিজের গভীরতা জানে।)

    if this node's level == the limit:
        stop -> do NOT recurse into children
    else:
        recurse into every child

print(1)                 print(3)
[Earth]                  [Earth]
 |__[Bangladesh]          |__[Bangladesh]
 |__[Pakistan]            |    |__[Dhaka Division]
 |__[Malaysia]            |    |    |__[Dhaka District]
                          |    ...

- The node itself is always printed; only its CHILDREN are cut. (Node নিজে সবসময় প্রিন্ট হয়, শুধু তার সন্তানরা বাদ যায়।)
- So print(k) shows every node whose level is <= k. (তাই print(k) সব Node দেখায় যাদের Level k বা তার কম।)
- The limit is passed DOWN unchanged to every child. (সীমাটি অপরিবর্তিতভাবে প্রতিটি সন্তানের কাছে পাঠানো হয়।)

* The cutoff check does not depend on the child, so it could be moved above the loop - same result, slightly clearer. (এই চেক সন্তানের উপর নির্ভর করে না, তাই লুপের আগেও রাখা যেত - ফল একই, পড়তে সহজ।)

--------------------------------------------------
Indentation Logic (ফাঁকা জায়গার হিসাব)
--------------------------------------------------
indent = " " * get_level() * 4      (৪ গুণ Level সমান ফাঁকা জায়গা।)
prefix = "|__" if the node has a parent else ""   (Root ছাড়া সবার আগে |__ বসে।)

Level 0 ->              Earth
Level 1 ->     |__Bangladesh
Level 2 ->         |__Dhaka Division

- Depth becomes visible purely through spacing. (শুধু ফাঁকা জায়গা দিয়েই গভীরতা বোঝা যায়।)
- The root has no parent, so it gets no prefix. (Root-এর Parent নেই, তাই তার আগে কিছু বসে না।)

--------------------------------------------------
This is DFS with a Depth Limit (গভীরতা-সীমাসহ DFS)
--------------------------------------------------
- Plain DFS goes as deep as the tree allows. (সাধারণ DFS যতদূর সম্ভব গভীরে যায়।)
- Depth-Limited DFS stops at a fixed depth. (Depth-Limited DFS নির্দিষ্ট গভীরতায় থেমে যায়।)
- BFS would print level by level instead, using a queue. (BFS এর বদলে Queue দিয়ে স্তরে স্তরে প্রিন্ট করত।)

DFS order  : Earth, Bangladesh, Dhaka Div, Dhaka Dist, Dhaka City, ...
BFS order  : Earth | Bangladesh, Pakistan, Malaysia | Dhaka Div, ...

- Iterative Deepening Search (used in game AI) is built on exactly this idea. (গেম AI-তে ব্যবহৃত Iterative Deepening এই ধারণার উপরেই তৈরি।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
Depth-limited tree printing is used in:
- `tree -L 2` style directory listings
- Collapsible file explorers and category menus
- Rendering only visible levels of a large DOM
- Location pickers (Country -> State -> City)
- Game AI search with a move-depth limit

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. That this is DFS with a depth limit, not BFS.
2. Why get_level() (O(h)) is what makes both indentation and cutting possible.
3. Why the limit must be forwarded in the recursive call.
4. How BFS with a queue would solve the same problem level by level.
5. That printing k levels costs O(number of nodes within those k levels).

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Forgetting to pass level=level to children.
✔ Children would reset to the default limit and print too much.

❌ Confusing "print up to level k" with "print only level k".
✔ This version prints every node whose level is <= k.

❌ Calling get_level() repeatedly inside a hot loop.
✔ Each call is O(h); store it in a variable when reused.

❌ Forgetting child.parent = self in add_child.
✔ get_level() would return 0 for everything and all cutting would break.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation       | Complexity | Why?                                  |
|-----------------|------------|---------------------------------------|
| add_child       | O(1)       | Appends to the children list          |
| get_level       | O(h)       | Walks up the parent chain             |
| print (full)    | O(n)       | Visits every node once                |
| print (level k) | O(n_k)     | Only nodes within the first k levels  |
| Space           | O(n)       | One node object per location          |
| Recursion Stack | O(h)       | One frame per level of depth          |

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

    def print(self, level=1):
        """Recursively print the tree structure"""
        indent = " " * self.get_level() * 4
        prefix = "|__" if self.parent else ""
        print(f"{indent}{prefix}{self.data}")

        tree_level = self.get_level()

        for child in self.children:
            if tree_level == level:
                break

            child.print(level=level)


def build_tree():
    """Build an expanded hierarchical world tree with multiple states, districts, and cities"""
    world = TreeNode("Earth")

    # --------------------
    # Bangladesh
    # --------------------
    bangladesh = TreeNode("Bangladesh")

    # Dhaka Division
    dhaka_div = TreeNode("Dhaka Division")
    dhaka_district = TreeNode("Dhaka District")
    dhaka_district.add_child(TreeNode("Dhaka City"))
    dhaka_district.add_child(TreeNode("Savar"))
    dhaka_district.add_child(TreeNode("Dhamrai"))

    narayanganj_district = TreeNode("Narayanganj District")
    narayanganj_district.add_child(TreeNode("Narayanganj City"))
    narayanganj_district.add_child(TreeNode("Rupganj"))

    dhaka_div.add_child(dhaka_district)
    dhaka_div.add_child(narayanganj_district)

    # Chittagong Division
    chittagong_div = TreeNode("Chittagong Division")
    chittagong_district = TreeNode("Chittagong District")
    chittagong_district.add_child(TreeNode("Chittagong City"))
    chittagong_district.add_child(TreeNode("Cox's Bazar"))

    comilla_district = TreeNode("Comilla District")
    comilla_district.add_child(TreeNode("Comilla City"))
    comilla_district.add_child(TreeNode("Daudkandi"))

    chittagong_div.add_child(chittagong_district)
    chittagong_div.add_child(comilla_district)

    bangladesh.add_child(dhaka_div)
    bangladesh.add_child(chittagong_div)
    world.add_child(bangladesh)

    # --------------------
    # Pakistan
    # --------------------
    pakistan = TreeNode("Pakistan")

    # Punjab Province
    punjab = TreeNode("Punjab Province")
    lahore_district = TreeNode("Lahore District")
    lahore_district.add_child(TreeNode("Lahore City"))
    lahore_district.add_child(TreeNode("Shahdara"))
    lahore_district.add_child(TreeNode("Cantt"))

    faisalabad_district = TreeNode("Faisalabad District")
    faisalabad_district.add_child(TreeNode("Faisalabad City"))
    faisalabad_district.add_child(TreeNode("Jaranwala"))

    punjab.add_child(lahore_district)
    punjab.add_child(faisalabad_district)

    # Sindh Province
    sindh = TreeNode("Sindh Province")
    karachi_district = TreeNode("Karachi District")
    karachi_district.add_child(TreeNode("Karachi City"))
    karachi_district.add_child(TreeNode("Korangi"))
    karachi_district.add_child(TreeNode("Gulshan"))

    hyderabad_district = TreeNode("Hyderabad District")
    hyderabad_district.add_child(TreeNode("Hyderabad City"))
    hyderabad_district.add_child(TreeNode("Latifabad"))

    sindh.add_child(karachi_district)
    sindh.add_child(hyderabad_district)

    pakistan.add_child(punjab)
    pakistan.add_child(sindh)
    world.add_child(pakistan)

    # --------------------
    # Malaysia
    # --------------------
    malaysia = TreeNode("Malaysia")

    selangor = TreeNode("Selangor State")
    kl_district = TreeNode("Kuala Lumpur District")
    kl_district.add_child(TreeNode("Kuala Lumpur City"))
    kl_district.add_child(TreeNode("Petaling Jaya"))
    kl_district.add_child(TreeNode("Shah Alam"))

    pj_district = TreeNode("Petaling District")
    pj_district.add_child(TreeNode("Subang Jaya"))
    pj_district.add_child(TreeNode("Puchong"))

    selangor.add_child(kl_district)
    selangor.add_child(pj_district)

    johor = TreeNode("Johor State")
    jb_district = TreeNode("Johor Bahru District")
    jb_district.add_child(TreeNode("Johor Bahru City"))
    jb_district.add_child(TreeNode("Pasir Gudang"))

    batu_pahat_district = TreeNode("Batu Pahat District")
    batu_pahat_district.add_child(TreeNode("Batu Pahat City"))
    batu_pahat_district.add_child(TreeNode("Kluang"))

    johor.add_child(jb_district)
    johor.add_child(batu_pahat_district)

    malaysia.add_child(selangor)
    malaysia.add_child(johor)
    world.add_child(malaysia)
    return world


if __name__ == "__main__":
    tree = build_tree()
    tree.print()
    tree.print(3)
    tree.print(4)

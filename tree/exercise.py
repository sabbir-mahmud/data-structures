r"""
==================================================
Tree Exercise: Organization Chart (ট্রি অনুশীলন) - Bilingual DSA Reference (10/10)
==================================================

The Problem (সমস্যাটি কী?)
--------------------------------------------------
- Build a company hierarchy using a General Tree. (General Tree দিয়ে একটি কোম্পানির স্তরবিন্যাস তৈরি করো।)
- Each node stores TWO values: name and designation. (প্রতিটি Node-এ দুইটি মান থাকে: name এবং designation।)
- print() must be able to show name only, designation only, or both. (print() শুধু নাম, শুধু পদবি, অথবা দুটোই দেখাতে পারবে।)

--------------------------------------------------
The Tree We Are Building (যে Tree টি বানাচ্ছি)
--------------------------------------------------

                      [CEO]
             /       /      \        \
        [CTO]     [COO]    [PM 1]   [PM 2]
        /   \      /   \     /   \      |
   [Lead][Lead] [HR][Ops][TL][TL]   [TL]
     |     |      |    |    |   |     |
  (Devs)(Devs) (Staff)(Staff)(Devs) (Devs)

- The root is the CEO (level 0). (Root হলো CEO, Level 0।)
- Every employee is a child of their manager. (প্রতিটি কর্মী তার ম্যানেজারের সন্তান।)
- Interns and developers are the leaves. (Intern ও Developer-রা হলো পাতা।)

--------------------------------------------------
Why a Multi-Field Node (একাধিক ফিল্ডের Node কেন)
--------------------------------------------------
+--------+-------------+--------+------------+
|  name  | designation | parent |  children  |
+--------+-------------+--------+------------+

- A tree node can carry as many fields as the problem needs. (সমস্যার প্রয়োজনে Node-এ যত খুশি ফিল্ড রাখা যায়।)
- Only parent and children define the STRUCTURE; the rest is payload. (গঠন ঠিক করে শুধু parent আর children; বাকিগুলো হলো ডেটা।)
- This is exactly how real systems store employee, file or category records. (আসল সিস্টেমে কর্মী, ফাইল বা ক্যাটাগরির তথ্য ঠিক এভাবেই রাখা হয়।)

--------------------------------------------------
How the Recursive print() Works (Recursive print কীভাবে চলে)
--------------------------------------------------
Step 1: Build the text based on the requested type. (কোন ধরন চাওয়া হয়েছে সেই অনুযায়ী লেখা তৈরি করো।)
Step 2: Indent using get_level() so depth is visible. (get_level() দিয়ে ফাঁকা জায়গা দাও, যাতে গভীরতা বোঝা যায়।)
Step 3: Print, then call print() on every child. (নিজে প্রিন্ট করো, তারপর প্রতিটি সন্তানের জন্য একই কাজ করো।)

CEO
 |__CTO
   |__Dev Lead
     |__Backend Developer

- The type argument is passed DOWN to every child. (type আর্গুমেন্টটি প্রতিটি সন্তানের কাছে পাঠাতে হয়।)
- Forgetting to pass it makes children fall back to the default. (না পাঠালে সন্তানরা Default মানেই ফিরে যাবে।)
- This is DFS: it finishes an entire branch before starting the next. (এটি DFS: একটি শাখা পুরো শেষ করে তারপর পরেরটিতে যায়।)

--------------------------------------------------
Real-World Applications (বাস্তব ক্ষেত্রে ব্যবহার)
--------------------------------------------------
This exact pattern (a node with payload + hierarchy) is used in:
- HR systems and org charts (কে কার অধীনে কাজ করে)
- Permission and role inheritance (a manager inherits a team's access)
- Bill of Materials in manufacturing (product -> parts -> sub-parts)
- Comment threads with replies
- Nested category trees in e-commerce
- Company reporting chains and approval workflows
- Any "who reports to whom" or "what contains what" model

--------------------------------------------------
Interview Tips (ইন্টারভিউ টিপস)
--------------------------------------------------
Always explain:
1. Why an org chart is a natural General Tree (Any number of reports per manager).
2. Why get_level() is used for indentation (It measures depth from the root).
3. Why printing is O(n) (Every node is visited exactly once).
4. Why the recursive parameter must be forwarded to children.
5. How you would extend this to search for an employee (DFS over all nodes, O(n)).

--------------------------------------------------
Common Mistakes (সাধারণ ভুল)
--------------------------------------------------
❌ Forgetting to pass type=type in the recursive call.
✔ Children would silently print in the default format.

❌ Forgetting child.parent = self inside add_child.
✔ get_level() would always return 0 and indentation would break.

❌ Naming a method print() and expecting the builtin.
✔ Inside the class, self.print() calls YOUR method, which shadows nothing globally but can confuse readers.

--------------------------------------------------
Complexity Summary
--------------------------------------------------
| Operation      | Complexity | Why?                                |
|----------------|------------|-------------------------------------|
| add_child      | O(1)       | Appends to the children list        |
| get_level      | O(h)       | Walks up the parent chain           |
| print (whole)  | O(n)       | Visits every node once              |
| Search a name  | O(n)       | No ordering rule exists             |
| Space          | O(n)       | One node object per employee        |

==================================================
"""


class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        count = 0

        parent = self.parent
        while parent:
            count += 1
            parent = parent.parent

        return count

    def print(self, type="both"):
        data = ""
        if type == "both":
            data = f"{self.name} ({self.designation})"
        elif type == "name":
            data = f"{self.name}"
        elif type == "designation":
            data = f"{self.designation}"
        else:
            print("Invalid type!")

        prefix = " " * self.get_level() + ("|__" if self.parent else "")

        print(prefix, data)

        if self.children:
            for child in self.children:
                child.print(type=type)


def build_tree():
    """Build an expanded company hierarchy tree with more leaf nodes"""
    # CEO
    ceo = TreeNode(name="Sabbir Mahmud", designation="CEO")

    # CTO subtree
    cto = TreeNode(name="Asif Mahmud", designation="CTO")
    dev_lead1 = TreeNode(name="Nabil", designation="Dev Lead")
    dev_lead1.add_child(TreeNode(name="Tariq", designation="Backend Developer"))
    dev_lead1.add_child(TreeNode(name="Farhan", designation="Frontend Developer"))
    dev_lead1.add_child(TreeNode(name="Rashed", designation="QA Engineer"))
    dev_lead1.add_child(TreeNode(name="Sabbir Khan", designation="Intern"))

    dev_lead2 = TreeNode(name="Salman", designation="Dev Lead")
    dev_lead2.add_child(TreeNode(name="Junaid", designation="Backend Developer"))
    dev_lead2.add_child(TreeNode(name="Rakib", designation="Frontend Developer"))
    dev_lead2.add_child(TreeNode(name="Sabbir Ahmed", designation="QA Engineer"))
    dev_lead2.add_child(TreeNode(name="Rafi", designation="Intern"))

    cto.add_child(dev_lead1)
    cto.add_child(dev_lead2)

    # COO subtree
    coo = TreeNode(name="Shaikh Ahmadulla", designation="COO")
    hr_head = TreeNode(name="Nadia", designation="HR Head")
    hr_head.add_child(TreeNode(name="Ayesha", designation="HR Executive"))
    hr_head.add_child(TreeNode(name="Rina", designation="Recruiter"))
    hr_head.add_child(TreeNode(name="Sara", designation="HR Intern"))

    ops_head = TreeNode(name="Fahim", designation="Operations Head")
    ops_head.add_child(TreeNode(name="Tanvir", designation="Operations Manager"))
    ops_head.add_child(TreeNode(name="Imran", designation="Logistics Manager"))
    ops_head.add_child(TreeNode(name="Rafiq", designation="Warehouse Staff"))

    coo.add_child(hr_head)
    coo.add_child(ops_head)

    # Project Manager 1 subtree
    project_manager1 = TreeNode(name="Arif", designation="Project Manager")
    team_lead1 = TreeNode(name="Mehedi", designation="Team Lead")
    team_lead1.add_child(TreeNode(name="Hassan Abdulla", designation="Backend"))
    team_lead1.add_child(TreeNode(name="Mr Abdulla", designation="Frontend"))
    team_lead1.add_child(TreeNode(name="Arif Islam", designation="QA"))
    team_lead1.add_child(TreeNode(name="Rana", designation="Intern"))

    team_lead2 = TreeNode(name="Abu Hassan", designation="Team Lead")
    team_lead2.add_child(TreeNode(name="Al Hadis", designation="QA"))
    team_lead2.add_child(TreeNode(name="Arafat Islam", designation="QA"))
    team_lead2.add_child(TreeNode(name="Arif Islam", designation="QA"))
    team_lead2.add_child(TreeNode(name="Sami", designation="Intern"))

    project_manager1.add_child(team_lead1)
    project_manager1.add_child(team_lead2)

    # Project Manager 2 subtree
    project_manager2 = TreeNode(name="Imran", designation="Project Manager")
    tm2_lead = TreeNode(name="Rafiqul", designation="Team Lead")
    tm2_lead.add_child(TreeNode(name="Nayeem", designation="Backend"))
    tm2_lead.add_child(TreeNode(name="Tanvir", designation="Frontend"))
    tm2_lead.add_child(TreeNode(name="Jewel", designation="QA"))
    tm2_lead.add_child(TreeNode(name="Sami", designation="Intern"))

    project_manager2.add_child(tm2_lead)

    # Assemble full hierarchy under CEO
    ceo.add_child(cto)
    ceo.add_child(coo)
    ceo.add_child(project_manager1)
    ceo.add_child(project_manager2)

    return ceo


if __name__ == "__main__":
    tree = build_tree()
    tree.print()
    tree.print(type="name")
    tree.print(type="designation")

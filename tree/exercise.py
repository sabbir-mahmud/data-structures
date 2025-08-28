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

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

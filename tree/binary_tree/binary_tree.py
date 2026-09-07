# binary tree


class BinaryTreeNode:

    __slots__ = ('data', 'left', 'right')

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None


class BinaryTree:

    def __init__(self):

        self.root = None


    # insert a new node into the binary tree
    def insert(self, data):

        new_node = BinaryTreeNode(data)

        # if tree is empty, new node becomes root
        if self.root is None:
            self.root = new_node
            return

        # use queue for level-order insertion
        queue = [self.root]

        while queue:

            current = queue.pop(0)

            # if left child is empty, insert here
            if current.left is None:
                current.left = new_node
                return

            # otherwise add left child to queue
            queue.append(current.left)

            # if right child is empty, insert here
            if current.right is None:
                current.right = new_node
                return

            # otherwise add right child to queue
            queue.append(current.right)


    # inorder traversal
    # left -> root -> right
    def inorder(self, node):

        if node is None:
            return

        self.inorder(node.left)

        print(node.data, end=" ")

        self.inorder(node.right)


    # preorder traversal
    # root -> left -> right
    def preorder(self, node):

        if node is None:
            return

        print(node.data, end=" ")

        self.preorder(node.left)

        self.preorder(node.right)


    # postorder traversal
    # left -> right -> root
    def postorder(self, node):

        if node is None:
            return

        self.postorder(node.left)

        self.postorder(node.right)

        print(node.data, end=" ")


    # level-order traversal
    # visit nodes level by level
    def level_order(self):

        if self.root is None:
            return

        queue = [self.root]

        while queue:

            current = queue.pop(0)

            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


    # search for a value
    def search(self, data):

        if self.root is None:
            return False

        queue = [self.root]

        while queue:

            current = queue.pop(0)

            if current.data == data:
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return False


    # calculate height of the binary tree
    def height(self, node):

        if node is None:
            return 0

        left_height = self.height(node.left)

        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


    # count total nodes
    def count_nodes(self, node):

        if node is None:
            return 0

        return (
            1
            + self.count_nodes(node.left)
            + self.count_nodes(node.right)
        )


    # count leaf nodes
    def count_leaf_nodes(self, node):

        if node is None:
            return 0

        # node without left and right child is a leaf
        if node.left is None and node.right is None:
            return 1

        return (
            self.count_leaf_nodes(node.left)
            + self.count_leaf_nodes(node.right)
        )


    # delete the deepest/rightmost node
    def delete_deepest(self, node):

        if node is None:
            return

        queue = [self.root]

        while queue:

            current = queue.pop(0)

            if current.left:

                if current.left is node:
                    current.left = None
                    return

                queue.append(current.left)

            if current.right:

                if current.right is node:
                    current.right = None
                    return

                queue.append(current.right)


    # delete a node from the binary tree
    def delete(self, data):

        if self.root is None:
            return

        # if root is the only node
        if (
            self.root.left is None
            and self.root.right is None
        ):

            if self.root.data == data:
                self.root = None

            return

        queue = [self.root]

        target = None
        deepest = None

        # find target and deepest node
        while queue:

            current = queue.pop(0)

            if current.data == data:
                target = current

            deepest = current

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        # target does not exist
        if target is None:
            return

        # replace target data with deepest node data
        target.data = deepest.data

        # remove deepest node
        self.delete_deepest(deepest)


# --------------------------------
# example
# --------------------------------

tree = BinaryTree()

tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)
tree.insert(70)


print("Inorder:")
tree.inorder(tree.root)
print()


print("Preorder:")
tree.preorder(tree.root)
print()


print("Postorder:")
tree.postorder(tree.root)
print()


print("Level Order:")
tree.level_order()
print()


print("Search 50:", tree.search(50))

print("Height:", tree.height(tree.root))

print("Total Nodes:", tree.count_nodes(tree.root))

print("Leaf Nodes:", tree.count_leaf_nodes(tree.root))


tree.delete(30)

print("After deleting 30:")
tree.level_order()
print()
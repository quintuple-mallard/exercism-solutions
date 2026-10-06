class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, node):
        if int(self.data) >= int(node.data):
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else: 
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def collapse(self):
        flat = []
        flat.append(self.data)
        l = self.left.collapse() if self.left is not None else []
        r = self.right.collapse() if self.right is not None else []
        return l + flat + r
    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for d in tree_data[1:]:
            self.root.insert(TreeNode(d))
    
    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.collapse()

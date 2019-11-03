from anytree import Node, RenderTree

jan = Node('Jan')
milosz = Node('Milosz', parent=jan)
michal = Node('Michal', parent=jan)
maciej = Node('Maciej', parent=jan)
emilka = Node('Emilka', parent=maciej)

for pre, fill, node in RenderTree(jan):
    print('{}{}'.format(pre, node.name))


# OR
# Tree has root, left and right branch
# And must have some 'name' or 'data'
# On branch (left or right) we can ascribe Tree object
# Simply clean python example:

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)


# Lets make tree where on left branches we will always have
# a EVEN (parzyste) numbers and on right ODD (nieparzyste) numbers
root = Tree('root')
root.left = Tree(0)
root.right = Tree(1)
root.left.left = Tree(2)
root.right.right = Tree(3)
root.left.left.left = Tree(4)
root.right.right.right = Tree(5)
print(root.right.right.right)
print('---')

# OR Tree with auto insert method. Add data from left to right, itd.


class Tree2:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree2(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree2(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

root2 = Tree2(8)
root2.insert(3)
root2.insert(10)
root2.insert(1)
root2.insert(6)
root2.insert(4)
root2.insert(7)
root2.insert(14)
root2.insert(13)

root2.print_tree()
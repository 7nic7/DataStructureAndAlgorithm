class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
            return
        cur = [self.root]
        while cur:
            father = cur.pop(0)
            if father.left is None:
                father.left = node
                return
            else:
                cur.append(father.left)
            if father.right is None:
                father.right = node
                return
            else:
                cur.append(father.right)

    def search_layer(self):
        """广度遍历"""
        if self.root is None:
            return
        cur = [self.root]
        print(self.root.elem, end='')
        while cur:
            father = cur.pop(0)
            if father.left is not None:
                print(father.left.elem, end='')
                cur.append(father.left)
            if father.right is not None:
                print(father.right.elem, end='')
                cur.append(father.right)

    def search_before(self, root):
        if root is None:
            return 
        print(root.elem, end='')
        self.search_before(root.left)
        self.search_before(root.right)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.search_layer()
    print()
    tree.search_before(tree.root)
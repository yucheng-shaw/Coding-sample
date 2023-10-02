class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if (self.leftChild is not None):
            children.append(self.leftChild)
        if(self.rightChild is not None):
            children.append(self.rightChild)
        return children


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)


preorder_list = []


def preorder(root):
    if root is not None:
        preorder_list.append(root.get())
        preorder(root.leftChild)
        preorder(root.rightChild)


def construct_tree(start, end):
    list = []
    node = Node(None)
    if start > end:
        list.append(None)
        return list
    for i in range(start, end + 1):
        leftSubtree = construct_tree(start, i-1)
        rightSubtree = construct_tree(i+1, end)
        for j in range(0, len(leftSubtree)):
            node.leftChild = leftSubtree[j]
            for k in range(0, len(rightSubtree)):
                node.rightChild = rightSubtree[k]
                new_node = Node(i)
                new_node.leftChild = node.leftChild
                new_node.rightChild = node.rightChild
                list.append(new_node)
    return list


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


with open('Input', 'r') as f:
    new = open('Output', 'w')
    for line in nonblank_lines(f):
        totalTreesFrom1toN = construct_tree(1, int(line.rstrip()))
        new.write(str(len(totalTreesFrom1toN)) + "\n")
        for i in range(0, len(totalTreesFrom1toN)):
            preorder(totalTreesFrom1toN[i])
            new.write(str(preorder_list) + "\n")
            preorder_list = []
    new.close()

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        # print(self.left, self.data, self.right, end='-')
        print(self.data, end='-')
        if self.right:
            self.right.printTree()

    def printTreeAdd(self):
        if self.left:
            self.left.printTree()
        print(self.left, self.data, self.right, end='-')
        # print(self.data, end='-')
        if self.right:
            self.right.printTree()
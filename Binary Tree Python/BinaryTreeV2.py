from node import Node

# unbalance
class BinaryTree(object):

    def __init__(self):
        self.root = Node(int(input("ROOT : ")))

    def rootData(self):
        cur = self.root
        return(cur.data)

    def insertRight(self, data):
        newData = Node(data)
        cur = self.root
        if cur.right is None:
            cur.right = newData
        else:
            newData.right = cur.right
            cur.right = newData
    
    def insertLeft(self, data):
        cur = self.root
        newData = Node(data)
        if cur.left is None:
            cur.left = newData
        else:
            newData.left = cur.left
            cur.left = newData

    def insert(self, data):
        newData = Node(data)
        cur = self.root
        # Jika data input lebih KECIL dari data pada current Node
        if data < cur.data:
            # jika data sebelah kiri root kosong maka akan diisi terlebih dahulu
            if cur.left is None:
                cur.left = newData
            else:
                while cur.left!=None:
                    cur = cur.left
                    if cur.data > data:
                        if cur.left is None:
                            cur.left = newData
                    if cur.data < data:
                        cur.right = newData
                        break
        # Jika data input lebih BESAR dari data pada current Node
        if data > cur.data:
            if cur.right is None:
                cur.right = newData
            else:
                while cur.right!=None:
                    cur = cur.right
                    if cur.data < data:
                        if cur.right is None:
                            cur.right = newData
                            break
                    if cur.data > data:
                        cur.left = newData
                        break

    def showData(self):
        cur = self.root
        return(cur.printTree())

    def showDataAdd(self):
        cur = self.root
        return(cur.printTreeAdd())

    def deleteAll(self):
        cur = self.root
        if cur.left is not None:
            cur.left = None
        if cur.right is not None:
            cur.right = None
        if cur.data is not None:
            cur.data = None
            self.__init__()

    def deleteElement(self, data):
        cur = self.root
        if cur.left is None and cur.right is None:
            cur.data = None
        else:
            if data < cur.data:
                if cur.left:
                    while cur.left!=None:
                        nodeChanger = cur
                        cur = cur.left
                        if data > cur.data:
                            if cur.right:
                                cur = cur.right
                                nodeChanger = nodeChanger.left
                                nodeChanger.left = nodeChanger.right
                                nodeChanger.right = None
                                return
                        if data == cur.data:
                            nodeChanger.left = cur.left
                            return
            if data > cur.data:
                if cur.right:
                    while cur.right!=None:
                        nodeChanger = cur
                        cur = cur.right
                        if data < cur.data:
                            if cur.left:
                                cur = cur.left
                                nodeChanger = nodeChanger.right
                                nodeChanger.right = nodeChanger.left
                                nodeChanger.left = None
                        if data == cur.data:
                            nodeChanger.right = cur.right
                            return

from node import Node

# Binary Tree dari objek ini membentuk data yang tidak seimbang
# Bentuk data dari struktur data tree program BinartyTreeV1.py

#                 _____ROOT_____
#   self.left--->/              \<---self.right
#            data                data < child of
#           /    \< left.right >/    \  v 
#       data     data       data      data > parent of
#      /    \   /    \     /    \    /    \   v
#   data  data NONE NONE  NONE NONE data  data > parent of leaf
#                                        /     \ v
#                  limit range input>  data    data < unlimited user input, leaf of data
#                                     /
#                                   NONE

# Example : 
# t.insertLeft(1)
# t.insertRight(9)
# t.insertLeft(1)
# t.insertRight(3)
# t.insertLeft(1)
# t.insertRight(6)
# t.insertChildOf(0, 7) < Menambah branch index 0 sebelah kiri

#                 _____ROOT_____
#   self.left--->/              \<---self.right
#            [ 1 ]               [ 6 ] < child of
#           /    \< left.right >/    \  v 
#       [ 1 ]    [ 7 ]        NONE    [ 3 ] > parent of
#      /     \   /     \               /    \   v
#   [ 1 ]  NONE NONE  NONE            NONE   [ 9 ] > parent of leaf  
#                                           /     \ v
#                    limit range input>  NONE    data < unlimited user input, leaf of data
#                                        

# unbalance
class BinaryTree(object):

    def __init__(self):
        self.root = Node('ROOT')

    def insertLeft(self, data):
        newData = Node(data)
        cur = self.root
        if cur.left is None:
            cur.left = newData
        else:
            newData.left = cur.left
            cur.left = newData

    def insertRight(self, data):
        newData = Node(data)
        cur = self.root
        if cur.right is None:
            cur.right = newData
        else:
            newData.right = cur.right
            cur.right = newData
    
    def printTree(self):
        leftData = []
        leftPos = []
        cur = self.root
        while cur.left:
            cur = cur.left
            leftData.append(cur.data)
            leftPos.append(cur.right)
            leftPos.append(cur.left)
        indexPrint = len(leftData)-1
        indexleft = 1
        indexright = 2
        while indexPrint > -1:
            print(leftPos[len(leftPos)-indexleft], leftData[indexPrint], leftPos[len(leftPos)-indexright], end='-')
            indexleft+=2
            indexright+=2
            indexPrint-=1
            # print(cur.left, cur.data, cur.right, end='-')
        cur = self.root
        print(cur.left, cur.data, cur.right, end='-')
        while cur.right:
            cur = cur.right
            # if cur.left:
            #     print(cur.left.data, end='-')
            print(cur.left, cur.data, cur.right, end='-')
        print('')

    def insertChildOf(self, index, data):
        newData = Node(data)
        cur = self.root
        curIndex = 0
        while cur!=None:
            cur = cur.left
            if index == curIndex:
                cur.right = newData
                break 
            curIndex+=1

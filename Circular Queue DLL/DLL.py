from node import Node

class DoubleLinkedList(object):

    def __init__(self):
        self.last = None

    def enqueue(self, data):
        newNode = Node(data)
        if (self.last == None):
            self.last = newNode
            newNode.next = self.last
            newNode.prev = self.last
        else:
            head = self.last.next
            self.last.next = newNode
            newNode.prev = self.last
            newNode.next = head
            head.prev = newNode

    def dequeue(self):
        if (self.last == None):
            print("List Masih kosong\n")
        elif (self.last.next == self.last):
            print("Data terhapus : ", self.last.data, "\n")
            self.last = None
        else:
            print("Data terhapus  : ", self.last.data, "\n")
            head = self.last.next
            cur = head
            while cur.next.next != head:
                cur = cur.next
            self.last = cur
            self.last.next = head
            head.prev = self.last

    def search(self, item):
        if (self.last == None):
            print("List masih kosong")
        else:
            head = self.last.next
            cur = head
            found = False
            while cur.next != head:
                if (cur.data == item):
                    found = True
                cur = cur.next
            if cur.data == item:
                found = True
            if (found):
                print("data ditemukan")
            else:
                print("data tidak ditemukan")

    def showDataForward(self):
        if (self.last == None):
            print("List masih kosong")
        else:
            head = self.last.next
            cur = head
            while cur.next != head:
                print(cur.dataend="> <")
                cur = cur.next

    def showDataBackward(self):
        if (self.last == None):
            print("List masih kosong\n")
        else:
            head = self.last.next
            cur = head
            while cur.next != head:
                cur = cur.next
            while cur != head:
                print(cur.data, end="> <")
                cur = cur.prev
            print(cur.data, "\n")

    def isEmpty(self):
        if self.last == None:
            return(True)
        else:
            return(False)

    def length(self):
        total = 0
        if self.last == None:
            return(total)
        else:
            total+=1
            head = self.last.next
            cur = head
            while cur.next!=head:
                cur = cur.next
                total+=1
            return(total)
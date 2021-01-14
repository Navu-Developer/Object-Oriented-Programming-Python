from node import Node

class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node()

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        newNode.prev = cur
        newNode.next = cur.next
        if cur.prev!=None:
            cur.next = newNode
        cur.next = newNode

    def Head(self):
        cur = self.head
        cur = cur.next
        return(cur.data)

    def Tail(self):
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        return(cur.data) 
    
    def prepend(self, data):
        self.addElement(0, data)

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            print("Node ditambahkan")
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        cur.prev = cur

    # tambah data pada index tertentu
    def addElement(self, index, data):
        if self.head is None:
            print("data anda masih kosong")
            return
        # if index == 0:
        #     self.prepend(data)
        else:
            cur = self.head
            curIndex = 0
            while cur!=None:
                if index == curIndex:
                    break
                cur = cur.next
                curIndex+=1
            if cur is None:
                print("index tidak ada")
            if cur!=None:
                newNode = Node(data)
                newNode.prev = cur
                newNode.next = cur.next
                if cur.prev!=None:
                    cur.next = newNode
                cur.next = newNode

    # Menampilkan data pada setiap node
    def showData(self):
        cur = self.head
        while cur!=None:
            # if cur.data==None:
            #     pass
            # else:
            print(cur.data, end=' -> <- ')
                # print(cur.prev, cur.data, cur.next)
            cur = cur.next
        print("NULL")

    def pop(self):
        cur = self.head
        while cur.next!=None:
            lastNode = cur
            cur = cur.next
        lastNode.next = cur.next
        return

    def isEmpty(self):
        cur = self.head
        if cur.next == None:
            return(True)
        else:
            return(False)

    def showData(self):
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            print(cur.data, end=' > ')
        print("\n")

    def length(self):
        total = 0
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            total+=1
        return(total)

dll = DoubleLinkedList()
dll.append("a")
dll.append("b")
dll.append(8)
dll.append(90)
dll.append("x")
dll.append(46)
print("tail : ",dll.Tail())
print("head : ",dll.Head())
dll.showData()
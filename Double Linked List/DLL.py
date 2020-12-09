from node import Node

class DoubleLinkedList():

    def __init__(self):
        self.head = Node()

    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            print("Node ditambahkan")
            return
        newNode.next = self.head
        newNode.prev = newNode
        self.head = newNode

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

    def addElement(self, index, data):
        if self.head is None:
            print("data anda masih kosong")
            return
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

    def showData(self):
        cur = self.head
        while cur!=None:
            if cur.data==None:
                pass
            else:
                print(cur.data, end=' -> ')
            cur = cur.next
        print("NULL")
    
    def length(self):
        total = -1
        cur = self.head
        while cur:
            cur = cur.next
            total+=1
        return(total)

    def deleteAtIndex(self, index):
        if index>=self.length():
            print("index tidak ada")
            return(None)
        curIndex = 0
        cur = self.head
        while cur:
            lastNode = cur
            cur = cur.next
            if curIndex == index+1:
                lastNode.next = cur.next
                return
            curIndex+=1
    
    def evenElement(self):
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            if int(cur.data)%2==0:
                print(cur.data, end=' > ')
            else:
                pass
        print("")

    def oddElement(self):
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            if int(cur.data)%2!=0:
                print(cur.data, end=' > ')
            else:
                pass
        print("")
    
    def aritmatika(self, assignment, index1, index2):
        num = []
        index = 0
        chance = 2
        if chance==2:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
                if index==index1:
                    print("angka 1 : ",cur.data)
                    num.append(cur.data)
                    chance-=1
                    index*=0
                    break
                index+=1
        if chance==1:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
                if index==index2:
                    print("angka 2 : ",cur.data)
                    num.append(cur.data)
                    chance-=1
                    break
                index+=1
        if assignment=="+":
            hasil = num[0]+num[1]
            return(hasil)
        if assignment=="-":
            hasil = num[0]-num[1]
            return(hasil)
        if assignment=="x":
            hasil = num[0]*num[1]
            return(hasil)
        if assignment==":":
            hasil = num[0]/num[1]
            return(hasil)

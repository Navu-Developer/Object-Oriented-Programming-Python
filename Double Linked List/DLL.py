from node import Node

class DoubleLinkedList():

    # Inisialisasi sebuah Double Linked List
    def __init__(self):
        self.head = Node()

    # Fungsi tambah depan
    def prepend(self, data):
        self.addElement(0, data)

    # Fungsi tambah belakang
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
    
    # panjang data sebuah node
    def length(self):
        total = -1
        cur = self.head
        while cur:
            cur = cur.next
            total+=1
        return(total)

    # hapus data pada index
    def deleteAtIndex(self, index):
        if index>=self.length():
            print("index tidak ada")
            return(None)
        curIndex = 0
        cur = self.head
        # if index == 0:
        #     if self.head is None:
        #         return
        #     else:
        #         cur = cur.prev
        #         cur.prev = None
        while cur:
            lastNode = cur
            cur = cur.next
            if curIndex == index+1:
                lastNode.next = cur.next
                return
            curIndex+=1
    
    # menampilkan data genap
    def evenElement(self):
        cur = self.head
        while cur!=None:
            if cur.data==None:
                pass
            else:
                if int(cur.data)%2==0:
                    print(cur.data)
            cur = cur.next
        print("")

    # menampilkan data ganjil
    def oddElement(self):
        cur = self.head
        while cur!=None:
            if cur.data==None:
                pass
            else:
                if int(cur.data)%2!=0:
                    print(cur.data)
            cur = cur.next
        print("")
    
    # fungsi menjalankan operasi aritmatika pada node dengan data
    # data harus integer
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
                    num.append(int(cur.data))
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
                    num.append(int(cur.data))
                    chance-=1
                    break
                index+=1
        if (type(num[0]) or type(num[1])) is str:
            print("salah satu data adalah string")
            skip = input()
            pass
        else:
            if assignment=="+":
                hasil = num[0]+num[1]
                return(hasil)
            if assignment=="-":
                hasil = num[0]-num[1]
                return(hasil)
            if assignment=="x":
                hasil = num[0]*num[1]
                return(hasil)
            if assignment=="//":
                hasil = num[0]//num[1]
                return(hasil)
    
    # Mendapatkan nilai pada index node tertentu
    def getDataValue(self, index):
        cur = self.head
        curIndex = 0
        while cur:
            if cur.data is None:
                pass
            else:
                if index == curIndex:
                    return(cur.data)
                    break
                curIndex+=1
            cur = cur.next

    # Mendapatkan jumlah seluruh data integer
    def sumData(self):
        total = 0
        cur = self.head
        while cur:
            if cur.data == None:
                pass
            else:
                if type(cur.data)!=int:
                    pass
                else:
                    total+=cur.data
            cur = cur.next
        return(total)

# d = DoubleLinkedList()
# d.append(0)
# d.append(2523)
# d.append(62342)
# d.append(562)
# d.append(245)
# d.addElement(1,9)
# d.deleteAtIndex(-1)
# print(d.getDataValue(0))
# d.showData()

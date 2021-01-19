class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():

    # Inisialisasi sebuah Double Linked List
    def __init__(self):
        self.head = Node()

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

    def showData(self):
        cur = self.head
        while cur!=None:
            print(cur.data, end=' -> <- ')
            cur = cur.next
        print("NULL")

    def addElement(self, index, data):
        if self.head is None:
            print("data anda masih kosong")
            return
        else:
            cur = self.head
            curIndex = 0
            while cur.next!=None:
                cur = cur.next
                if int(cur.data)%2==0:
                    curIndex+=1
                if index == curIndex:
                    if cur is None:
                        print("index tidak ada")
                    if cur!=None:
                        newNode = Node(data)
                        newNode.prev = cur
                        newNode.next = cur.next
                        if cur.prev!=None:
                            cur.next = newNode
                        cur.next = newNode

    def length(self):
        total = 0
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
            if curIndex == index:
                lastNode.next = cur.next
                return
            curIndex+=1

def main():
    DLL.append(10)
    DLL.append(15)
    DLL.append(20)
    DLL.append(25)
    DLL.showData()
    indexGenap = int(input("Tambahkan data setelah node genap ke : "))
    data = int(input("Isikan data yang akan ditambahkan : "))
    DLL.addElement(indexGenap, data)
    DLL.showData()
    print("setelah hapus diawal data")
    DLL.deleteAtIndex(0)
    DLL.showData()

if __name__ == "__main__":
    DLL = DoubleLinkedList()
    main()
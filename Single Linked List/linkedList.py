from nodeLib import Node
from termcolor import colored

class linkedList(object):

    # Inisialisasi sebuah head sebagai Node
    def __init__(self):
        self.head = Node()

    # untuk menambahkan data dari depan
    def prepend(self, data):
        newData = Node(data)
        newData.next = self.head
        self.head = newData

    def append(self, data): # untuk menambahkan data
        # Node baru sebagai class node (class node)
        newData = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = newData

    def length(self): # untuk mengetahui panjang data
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return(total)

    def display(self): # membuat display berupa list
        cur = self.head
        print("Head ==> ", end='')
        while cur!=None:
            print(cur.data, end=' -> ')
            cur = cur.next
        print("Null")

    def search(self, index): # untuk mencari data
        if index>self.length():
            print(colored("ERR : index out of range!","red"))
            return(None)
        curIndex = 0
        cur = self.head
        while True:
            cur = cur.next
            if curIndex == index: 
                return(cur.data)
            curIndex+=1
    
    def delete(self, index): # untuk menghapus data berdasarkan index
        if index>=self.length():
            print(colored("ERR : index out of range!","red"))
            return(None)
        curIndex = 0
        cur = self.head
        while True:
            lastNode = cur
            cur = cur.next
            if curIndex == index:
                lastNode.next = cur.next
                return
            curIndex+=1
        
    def deleteElem(self, data): # Menghapus data berdasarkan elemen
        if self.head is None:
            return None
        
        else:
            cur = self.head
            prev = None
            while cur.data != data and cur.next is not None:
                prev = cur
                cur = cur.next
            
            if cur.data == data:
                if cur == self.head:
                    if cur.next is None:
                        self.head = None
                    else:
                        self.head = cur.next
                else:
                    if cur.next is None:
                        prev.next = None
                    else:
                        prev.next = cur.next
            else:
                return None
        
    def sort(self): # untuk mensorting data linked list dari terkecil
        newList = []
        cur = self.head
        while cur:
            if cur.data!=None:
                newList.append(int(cur.data))
            else:
                pass
            cur = cur.next
        newList = sorted(newList)
        return(newList)

    def odd(self): # Menampung data linked list bernilai ganjil
        dataGanjil = []
        cur = self.head
        while cur:
            if cur.data!=None:
                if (int(cur.data)%2) != 0:
                    dataGanjil.append(cur.data)
            cur = cur.next
        dataGanjil = sorted(dataGanjil)
        return(dataGanjil)
    
    def even(self): #Menampung data linked list bernilai genap
        dataGanjil = []
        cur = self.head
        while cur:
            if cur.data != None:
                if (int(cur.data)%2) == 0:
                    dataGanjil.append(cur.data)
            cur = cur.next
        dataGanjil = sorted(dataGanjil)
        return(dataGanjil)
    
    def getDataAsList(self): # Menampung data linked list kedalam list
        urList = []
        cur = self.head
        while cur:
            if cur.data != None:
                urList.append(cur.data)
            cur = cur.next
        return(urList)
    
    def getSmallestIndex(self): # untuk menampung indeks elemen terkecil
        urList = self.getDataAsList()
        small = min(urList)
        print(small)
        cur = self.head
        curIndex = 0
        while(cur):
            if(cur.data == small):
                break
            cur = cur.next
            curIndex += 1
        return(curIndex)
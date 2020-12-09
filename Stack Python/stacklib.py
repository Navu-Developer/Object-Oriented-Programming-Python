from collections import deque

class stackAlgorithm(object):

    def __init__(self, items=None):
        self.items = deque()

    def tambah_data(self, data): # menambahkan data
        L = self.items
        L.append(data)

    def hapus_data(self): # menghapus data
        L = self.items
        L.pop()
    
    def panjang_data(self): # panjang data
        L = self.items
        return len(L)

    def tampilkan_data(self): # menampilkan data
        return(self.items)

    def getElemIndex(self, elems): # Mencari index berdasarkan elemen
        L = self.items
        i = 0
        index = L[i]
        while i < sA.length():
            for item in index:
                if item == elems:
                    break
                i+=1
            return(i)

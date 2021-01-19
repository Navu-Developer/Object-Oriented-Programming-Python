class QueueList(object):
    def __init__(self):
        self.item = []

    def enqueue(self, data):
        L = self.item
        L.append(data)

    def dequeue(self):
        L = self.item
        L.pop(0)

    def length(self):
        return(len(self.item))

    def showData(self):
        return(self.item)

    def kelipatanTiga(self):
        Three = []
        L = self.item
        index = 0
        for _ in L:
            if L[index]%3==0:
                Three.append(L[index])
            else:
                pass
            index+=1
        return(Three)
    
    def totalKelipatanTiga(self):
        L = self.kelipatanTiga()
        return(len(L))

    def jumlahElemenKelipatanTigaGenap(self):
        KelipatanTigaGenap = []
        L = self.kelipatanTiga()
        index = 0
        for _ in L:
            if L[index]%2==0:
                KelipatanTigaGenap.append(L[index])
            else:
                pass
            index+=1
        return(sum(KelipatanTigaGenap))

    def maxKelipatanTiga(self):
        return(max(self.kelipatanTiga()))

    def maksimumKedua(self):
        L = self.kelipatanTiga()
        L.sort()
        index = len(L)-2
        return(L[index])


def main():
    repeat = str(input("Inputkan banyak Queue list : "))
    for i in range(int(repeat)):
        data = int(input("Input Elemen ke {} : ".format(i+1)))
        Q.enqueue(data)
    print(Q.showData())
    print("Output Elemen Kelipatan 3 : ",Q.kelipatanTiga())
    print("Banyak Elemen Kelipatan 3 : ",Q.totalKelipatanTiga())
    print("Jumlah Elemen Kelipatan 3 Genap : ",Q.jumlahElemenKelipatanTigaGenap())
    print("Nilai maksimum List Kelipatan 3 : ",Q.maxKelipatanTiga())
    print("Nilai maksimum kedua list kelipatan 3 : ",Q.maksimumKedua())
if __name__ == "__main__":
    Q = QueueList()
    main()
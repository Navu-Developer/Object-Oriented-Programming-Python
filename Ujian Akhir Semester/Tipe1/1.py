class StackList(object):
    def __init__(self):
        self.item = []

    def append(self, data):
        L = self.item
        L.append(data)
    
    def length(self):
        return(len(self.item))

    def erase(self):
        L = self.item
        L.pop(self.length()-1)

    def showData(self):
        return(self.item)

    def highest(self):
        L = self.item
        return(max(L))

    def smallest(self):
        L = self.item
        return(min(L))

    def totalHighestSmallest(self):
        total = self.highest() + self.smallest()
        return(total)

    def checkIfOdd(self):
        if self.totalHighestSmallest()%2==0:
            return("bilangan genap kelipatan 2")
        if self.totalHighestSmallest()%2!=0:
            return("ganjil bukan kelipatan 3")

S = StackList()
S.append(2)
S.append(6)
S.append(3)
S.append(7)
S.append(4)
S.append(9)
S.append(1)
S.append(10)
S.append(22)
S.append(4)
print("teratas : ",S.highest())
print("terkecil : ",S.smallest())
print("total nilai atas bawah : ",S.totalHighestSmallest())
print("Termasuk bilangan : ",S.checkIfOdd())
print(S.showData())
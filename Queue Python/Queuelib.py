from collections import deque

class queueAlgorithm(object):

    def __init__(self, items=None):
        self.items = deque()

    def append(self, data):
        L = self.items
        L.append(data)

    def erase(self):
        L = self.items
        L.popleft()

    def showData(self):
        return(self.items)

    def length(self):
        return(len(self.items))
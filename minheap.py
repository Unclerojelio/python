''' MinHeap demo
    Roger Banks
    01 Jan 2021
'''

import random

class minIntHeap():
    def __init__(self):
        self.items = []

    def getLeftChildIndex(self, i):
        return 2*i+1
    def getRightChildIndex(self, i):
        return 2*i+2
    def getParentIndex(self, i):
        return (i-1)//2
    def hasLeftChild(self, i):
        return self.getLeftChildIndex(i) < len(self.items)
    def hasRightChild(self, i):
        return self.getRightChildIndex(i) < len(self.items)
    def hasParent(self,i):
        return i > 0
    def leftChild(self, i):
        return self.items[self.getLeftChildIndex(i)]
    def rightChild(self, i):
        return self.items[self.getRightChildIndex(i)]
    def getParent(self, i):
        return self.items[self.getParentIndex(i)]

    def swap(self, i, j):
        temp = self.items[i]
        self.items[i] = self.items[j]
        self.items[j] = temp

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]

    def poll(self):
        if len(self.items) == 0:
            return None
        item = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.heapifyDown()
        return item

    def add(self, item):
        self.items.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.items)-1
        while self.hasParent(index) and self.getParent(index) > self.items[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)

            if self.items[index] < self.items[smallerChildIndex]:
                return
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    def isEmpty(self):
        return len(self.items) == 0


heap = minIntHeap()
# heap.add(5)
# heap.add(4)
# heap.add(3)
# heap.add(2)
# heap.add(1)

for i in range(25):
    heap.add(random.randint(1,100))

while not heap.isEmpty():
    print(heap.poll())

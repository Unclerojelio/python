import random
import timeit

def swap(theList, a, b):
    temp = theList[a]
    theList[a] = theList[b]
    theList[b] = temp

def insert(theList, insertIndex):
    index = insertIndex - 1
    while (theList[insertIndex] < theList[index]) & (index >= 0) & (insertIndex >= 0):
        temp = theList[insertIndex]
        theList[insertIndex] = theList[index]
        theList[index] = temp
        index -= 1
        insertIndex -= 1

def bubble_sort(theList):
    notSorted = True
    while notSorted:
        notSorted = False
        for index in range(1, len(theList)):
            if theList[index] < theList[index-1]:
                swap(theList, index, index-1)
                notSorted = True

def selection_sort(theList):
    min = 0
    unsorted = 1
    while unsorted < len(theList):
        for index in range(unsorted, len(theList)):
            if theList[min] > theList[index]:
                min = index
        swap(theList, unsorted-1, min)
        min = unsorted
        unsorted += 1

def insertion_sort(theList):
    notSorted = True
    index = 0
    while notSorted:
        if theList[index] > theList[index+1]:
            insert(theList, index+1)
        index += 1
        if index == len(theList)-1:
            notSorted = False

def merge_sort(theList):
    print "TBD"

def main():
    randomList = random.sample(xrange(1, 101), 50)
    print randomList

    theList = randomList[:]
    bubble_sort(theList)
    print "Bubble sort: "
    print theList

    theList = randomList[:]
    selection_sort(theList)
    print "Selection sort: "
    print theList

    theList = randomList[:]
    insertion_sort(theList)
    print "Insertion sort: "
    print theList

    theList = randomList[:]
    merge_sort(theList)
    print "Merge sort: "
    print theList

if  __name__ =='__main__':
    main()
    #print timeit.timeit("selection_sort()","from __main__ import selection_sort",number=10000)
#Selection sort algorithm
"""" Concept behind selection sort
We have an array of unsorted elements which have to be sorted 
1. Start by having first element at 0th index as min elemeent
2.Compare the element with next element
3.If next elemnt is smaller set the min element to that elemnt
4.Traverse till end of array
5.Plcae that element minimum at the beginning of array after each iteration
6.Repeat iteraition till complete array is sorted
"""
#Selection sort

def selectionSort(nlist):
    for fillslot in range (len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1,fillslot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos=location

        temp= nlist[fillslot]
        nlist[fillslot]=nlist[maxpos]
        nlist[maxpos]=temp
nlist = [10,345,45,55]
selectionSort(nlist)
print(nlist)


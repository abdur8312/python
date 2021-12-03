def mergeSort(ListValues):
    if (len(ListValues)) > 1:
        mid = len(ListValues) // 2
        left = ListValues[:mid]
        right = ListValues[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        lengthL=len(left)
        lengthR=len(right)
        while i < lengthL and j < lengthR:
            if left[i] <= right[j]:
              ListValues[k] = left[i]
              i += 1
            else:
                ListValues[k] = right[j]
                j += 1
            k += 1
        while i < lengthL:
            ListValues[k] = left[i]
            i += 1
            k += 1
        while j < lengthR:
            ListValues[k]=right[j]
            j += 1
            k += 1
    return myList
myList = [1,2,5,4,3,6,8,10]
mergeSort(myList)
print(myList)
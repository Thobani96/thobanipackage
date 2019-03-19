def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    bubbled_items = items.copy() # Making sure that the new list is of the same length as items
    for i in range(len(bubbled_items)):
        for j in range(len(bubbled_items)-1-i):
            if bubbled_items[j] > bubbled_items[j+1]:
                bubbled_items[j], bubbled_items[j+1] = bubbled_items[j+1], bubbled_items[j]

    return bubbled_items



def merge_sort(items):
    """ Return array of items, sorted in ascending order """
    if len(items) >1:
        mid = len(items)//2 #Finding the mid of the array
        L = items[:mid] # Dividing the array elements
        R = items[mid:] # into 2 halves

        merge_sort(L) # Sorting the first half
        merge_sort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                items[k] = L[i]
                i+=1
            else:
                items[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            items[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            items[k] = R[j]
            j+=1
            k+=1
    return items



def quick_sort(items):
    """ Return array of items, sorted in ascending order """
    return quick_sort([i for i in items[1:] if i <= items[0]]) + [items[0]] \
        + quick_sort([i for i in items[1:] if i >= items[0]]) if items else []

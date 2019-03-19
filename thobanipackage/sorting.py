def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    bubbled_items = items.copy() # Making sure that the new list is of the same length as items
    for i in range(len(bubbled_items)):
        for j in range(len(bubbled_items)-1-i):
            if bubbled_items[j] > bubbled_items[j+1]:
                bubbled_items[j], bubbled_items[j+1] = bubbled_items[j+1], bubbled_items[j]

    return bubbled_items



def merge_sort(items):
   '''Return array of items, sorted in ascending order'''
   len_sort = len(items)
   # Base case. A list of size 1 is sorted.

   if len_sort == 1:
       return items
   # Recursive case. Find midpoint of list
   mid_point = int(len_sort / 2)

   i1 = merge_sort(items[:mid_point]) # divide list into two halves
   i2 = merge_sort(items[mid_point:]) # call merge_sort function on each half of list

   return merge(i1, i2)



def quick_sort(items):
    """ Return array of items, sorted in ascending order """
    return quick_sort([i for i in items[1:] if i <= items[0]]) + [items[0]] \
        + quick_sort([i for i in items[1:] if i >= items[0]]) if items else []

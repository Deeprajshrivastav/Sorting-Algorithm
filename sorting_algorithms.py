
# Bubble sort
def bubble_sort(List):
    length = len(List)
    for i in range(len(List)):
        for j in range(length-1):
            if (List[j] > List[j + 1]):
                List[j], List[j + 1] = List[j + 1], List[j]
        length = length - 1   
    return List 

# insertition sort
def insert_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while(j >= 0 and list[j] > temp):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = temp
    return list



# selection sort
def selection_sort(list):
    for i in range(0, len(list)):
        for x in range(0, len(list)):
            if list[i] < list[x]:
                list[i], list[x] = list[x], list[i]     
    return list

List = [41111,6,300,65,32,681,5434,000, 235.1,75,234,765,35,462,711]   

print(bubble_sort(List))
print(insert_sort(List))
print(selection_sort(List))

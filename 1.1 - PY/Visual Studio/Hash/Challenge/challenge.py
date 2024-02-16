class Node:
    def __init__(self, data):
        #Store the value for the node
        self.value = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = None
        self.length = 1

class Stack:
    def __init__(self):
        #Initially there won't be any node at the top of the stack
        self.top = None
        # Initially there will be zero elements in the stack
        self.size = 0
        self.head = None
        self.items = []
    
    def top_empty(self):
        return self.top == None
    
    def push(self, data):
        if not self.top_empty():
            if self.head == None:
                self.head = Node(data)
                self.top =  True
            self.items.append(Node(data))
            self.size += 1
    
    def pop(self):
        if not self.top_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

array = [6, 2, 9, 7, 4, 8]
def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    return array
array = selectionSort(array)
print(array)

my_list = [6, 2, 9, 7, 4, 8]
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step -1
        while j >= 0 and key < array[j]:
            array[j +1] = array[j]
            j = j-1
        array[j+1] = key
    return array
array = insertionSort(my_list)
print(array)

arr = [4, 6, 2, 7, 1, 9, 5]
def quickSort(array):
    stack = [(0, len(arr) -1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index-1))
            stack.append((pivot_index+1, high))
    return array
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
array = quickSort(arr)
print(array)
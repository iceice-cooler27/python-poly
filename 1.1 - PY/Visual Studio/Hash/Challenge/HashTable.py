
class HashTable:
    #Initialsing
    def __inti__(self, size):
        self.size = size
        # [] = list
        # [None] * size = list of size "size" with all values as None
        self.table = [None] * size

    def hash_function(self, key):
        # hash() is a built-in function in Python that returns the hash value of an object
        # hash value represents the input data (strings / number)
        return hash(key) % self.size

    def insert(self, key, value):
        # passing through key to hash_function to get index
        index = self.hash_function(key)
        if self.table[index] is None:
            # if the index is empty, creating an empty list 
            self.table[index] = []
        # (key, value) = tuple
        self.table[index].append((key, value))

    def remove(self, key):
        index = self.hash_function(key)
        # if the index is empty
        if self.table[index] is None:
            #KeyError is Python exception thrown when a key is not found
            raise KeyError(key)
        # if the index is not empty
        # loop through the list at the index
        for i in range(len(self.table[index])):
            # if key is found
            if self.table[index][i][0] == key:
                # remove the key
                self.table[index].pop(i)
                return
        # if key not found
        raise KeyError(key)
    
    def print_table(self):
        print(self.table)

    hash_table = HashTable(10)
    hash_table.insert("hello", 1)
    hash_table.print_table()

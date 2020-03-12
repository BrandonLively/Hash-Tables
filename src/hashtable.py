# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        current_node = self.storage[self._hash_mod(key)]
        if current_node == None:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
        else:
            while current_node.next is not None:
                if current_node.key == key:
                    current_node.value = value
                    return
                current_node = current_node.next
            if current_node.key == key:
                current_node.value = value
            else:
                current_node.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        current_node = self.storage[self._hash_mod(key)]
        if current_node is not None:
            if current_node.key == key:
                self.storage[self._hash_mod(key)] = current_node.next
                return
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.key == key:
                    self.storage[self._hash_mod(key)] = current_node.next
                    return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        current_node = self.storage[self._hash_mod(key)]
        if current_node is not None:
            if current_node.key == key:
                return current_node.value
            while current_node.next is not None:
                current_node = current_node.next
                if current_node.key == key:
                    return current_node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in
        '''
        temp = copy = self.storage
        self.storage = [None] * len(range(len(temp))) * 2
        self.capacity = len(self.storage)

        counter = 0
        while counter < len(temp):
            current_node = temp[counter]
            if current_node is not None:
                self.insert(current_node.key, current_node.value)
                while current_node.next is not None:
                    self.insert(current_node.next.key, current_node.next.value)
                    current_node = current_node.next
            counter += 1


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap():
    def __init__(self, size = 8):
        self.size = size    
        self.table = [None] * size  
        self.count = 0

    def _hash(self,key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        idx = self._hash(key)
        head = self.table[idx]

        curr = head 
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        new_node = Node(key,value)
        new_node.next = head
        self.table[idx] = new_node
        self.count +=1 
        

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]

        while curr :
            if curr.key == key :
                return curr.value
            curr = curr.next

        return None

    def delete(self, key):
        idx = self._hash(key)
        curr = self.table[idx]

        prev = None
        while curr:
            if curr.key == key:
                if not prev:
                    self.table[idx] = curr.next
                else :
                    prev.next = curr.next

                self.count -=1
                return True
            prev = curr
            curr = curr.next

        return False




# Define a simple test function
def test_hash_table():
    
    ht = HashMap()
    # Insert values
    ht.insert("apple", 5)
    ht.insert("grape", 9)
    ht.insert("apple", 10)  # update
    
    # Test retrieval
    assert ht.get("apple") == 10, "Test failed: apple should be 10"
    assert ht.get("grape") == 9, "Test failed: grape should be 9"
    
    # Test deletion
    ht.delete("apple")
    assert ht.get("apple") is None, "Test failed: apple should be None after deletion"
    
    print("All tests passed!")

# Run the test
test_hash_table()
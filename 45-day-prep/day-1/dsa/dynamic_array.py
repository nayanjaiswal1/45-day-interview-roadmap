
class DynamicArray():
    def __init__(self):
        self.capacity = 1 
        self.size =  0
        self.arr = [None] * self.capacity

    def _resize(self):
        self.capacity *=2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.arr[i]

        self.arr = new_array

    def push(self, value):

        if self.size == self.capacity :
            self._resize()

        self.arr[self.size] = value
        self.size += 1


    def get(self, idx):
        if idx < 0 or idx >= self.size :
            return None
 
        return self.arr[idx]
    
    def pop(self):

        if self.size == 0:
            return None

        self.size -= 1
        val = self.arr[self.size]
        self.arr[self.size] = None

        return val
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.arr[:self.size])
    














# Simple test for DynamicArray
def test_dynamic_array():
    arr = DynamicArray()
    
    # Push elements
    arr.push(1)
    arr.push(2)
    arr.push(3)
    
    # Test length
    assert len(arr) == 3, "Length should be 3"
    
    # Test get
    assert arr.get(0) == 1, "Index 0 should be 1"
    assert arr.get(1) == 2, "Index 1 should be 2"
    assert arr.get(2) == 3, "Index 2 should be 3"
    assert arr.get(3) is None, "Out of bounds index should be None"
    
    # Test pop
    assert arr.pop() == 3, "Pop should return 3"
    assert arr.pop() == 2, "Pop should return 2"
    assert arr.pop() == 1, "Pop should return 1"
    assert arr.pop() is None, "Pop from empty should return None"
    
    print("All tests passed for DynamicArray!")

# Run the test
test_dynamic_array()
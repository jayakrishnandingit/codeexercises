class MinHeap(object):
    def __init__(self, arr=[]):
        self.heap = arr
        for i in range(len(self.heap) - 1, -1, -1):
            self.heapify(i)
    
    def _get_parent(self, idx):
        # return parent index
        return (idx-1)//2
    
    def _get_left(self, idx):
        return (2*idx) + 1

    def _get_right(self, idx):
        return (2*idx) + 2
        
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1
    
        if len(self.heap) > 0:
            # bubble up. check parent and current element to maintain heap property.
            parent_idx = self._get_parent(idx)
            while parent_idx >= 0 and self.heap[parent_idx] > data:
                self.swap(parent_idx, idx)
                parent_idx = self._get_parent(parent_idx)
                
    def print_me(self):
        print(self.heap)
    
    def heapify(self, idx):
        """bubble down the elem at idx and maintain heap property in the array."""
        left_child = self._get_left(idx)
        right_child = self._get_right(idx)
        
        smallest = idx
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[idx]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
            
        if smallest != idx:
            self.swap(idx, smallest)
            self.heapify(smallest)
    
    def extract(self):
        """"Extract the minimum."""
        if len(self.heap) == 0:
            return None

        self.swap(0, -1)
        ret_value = self.heap.pop()
        if len(self.heap) > 1:
            self.heapify(0)
        return ret_value

    def delete(self, data):
        pass
    
min_heap_obj = MinHeap([6, 5, 4, 3, 10])
# min_heap_obj.insert(2)
min_heap_obj.print_me()
# min_val = min_heap_obj.extract()
# print "Min value: ", min_val
# min_val = min_heap_obj.extract()
# print "Min value: ", min_val
# min_val = min_heap_obj.extract()
# print "Min value: ", min_val
# min_val = min_heap_obj.extract()
# print "Min value: ", min_val
# min_val = min_heap_obj.extract()
# print "Min value: ", min_val
# min_val = min_heap_obj.extract()
# print "Min value: ", min_val
# min_heap_obj.print_me()

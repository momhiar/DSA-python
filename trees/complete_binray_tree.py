class CompleteBinaryTree:
    def __init__(self):
        self.tree = []
    def insert(self, value):
        self.tree.append(value)
    def get_parent(self, index):
        if index == 0:
            return None # since root has no parent 
        return (index-1) // 2
    def get_left_child(self, index):
        left = 2* index + 1
        return left if left < len(self.tree) else None
    def get_right_child(self, index):
        right = 2*index +2
        return right if right < len(self.tree) else None
    def get_leve_order(self):
        return self.tree.copy()
    def __str__(self):
        return str(self.tree)
    def visualize(self):
        if not self.tree:
            print("Empty tree")
            return
        level = 0
        level_size = 1
        i = 0
        while i < len(self.tree):
            nodes = []
            for _ in range(level_size):
                if i < len(self.tree):
                    nodes.append(str(self.tree[i]))
                    i += 1
                else:
                    break
                
            print(f"Level {level}: {' '.join(nodes)}")
            level += 1
            level_size *= 2
                
# Create a complete binary tree
cbt = CompleteBinaryTree()

# Insert elements
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elem in elements:
    cbt.insert(elem)

# Print the tree
print("Tree array representation:", cbt)
print("\nTree structure visualization:")
cbt.visualize()

# Access some nodes
print("\nNode relationships:")
print(f"Parent of node at index 4: {cbt.get_parent(4)} (value: {cbt.tree[cbt.get_parent(4)] if cbt.get_parent(4) is not None else 'None'})")
print(f"Left child of node at index 2: {cbt.get_left_child(2)} (value: {cbt.tree[cbt.get_left_child(2)] if cbt.get_left_child(2) is not None else 'None'})")
print(f"Right child of node at index 1: {cbt.get_right_child(1)} (value: {cbt.tree[cbt.get_right_child(1)] if cbt.get_right_child(1) is not None else 'None'})")




class MinHeap(CompleteBinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        super().insert(value)
        self._heapify_up(len(self.tree) - 1)
        
    def _heapify_up(self, index):
        while index > 0:
            parent_idx = self.get_parent(index)
            if  self.tree[index] < self.tree[parent_idx]:
                self.tree[index], self.tree[parent_idx] = self.tree[parent_idx], self.tree[index]
                index = parent_idx
            else:
                break
    def extract_min(self):
        if len(self.tree) == 0:
            return None
        min_val = self.tree[0]
        last_val = self.tree.pop()
        if len(self.tree) > 0:
            self.tree[0] = last_val
            self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, index):
        smallest = index
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        
        if left is not None and left < len(self.tree) and self.tree[left] < self.tree[smallest]:
            smallest = left
        if right is not None and right < len(self.tree) and self.tree[right] < self.tree[smallest]:
            smallest = right
        if not smallest == index:
            self.tree[index] , self.tree[smallest] = self.tree[smallest], self.tree[index]
            self._heapify_down(smallest)
            
    def get_min(self):
        """Return the minimum element without removing it"""
        return self.tree[0] if len(self.tree) > 0 else None
        
heap = MinHeap()

# Insert elements
elements = [5, 3, 8, 1, 9, 2, 6]
for elem in elements:
    heap.insert(elem)

print("Heap after insertions:")
print(heap)
print("\nVisualization:")
heap.visualize()

# Extract min elements
print("\nExtracting elements:")
while len(heap.tree) > 0:
    print(f"Extracted: {heap.extract_min()}, Remaining: {heap}")
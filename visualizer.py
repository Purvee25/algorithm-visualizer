class SortVisualizer:
    def __init__(self):
        self.steps = []

    def _record(self, arr, highlight=None):
        self.steps.append({"array": arr[:], "highlight": highlight or []})

    def bubble_sort(self, arr):
        self.steps = []
        a = arr[:]
        n = len(a)
        for i in range(n):
            for j in range(n - i - 1):
                self._record(a, [j, j+1])
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        self._record(a)
        return self.steps

    def quicksort(self, arr):
        self.steps = []
        a = arr[:]
        self._quicksort_helper(a, 0, len(a)-1)
        self._record(a)
        return self.steps

    def _quicksort_helper(self, a, low, high):
        if low < high:
            pi = self._partition(a, low, high)
            self._quicksort_helper(a, low, pi-1)
            self._quicksort_helper(a, pi+1, high)

    def _partition(self, a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            self._record(a, [j, high])
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[high] = a[high], a[i+1]
        return i + 1

    def merge_sort(self, arr):
        self.steps = []
        a = arr[:]
        self._merge_sort_helper(a, 0, len(a)-1)
        self._record(a)
        return self.steps

    def _merge_sort_helper(self, a, l, r):
        if l < r:
            m = (l + r) // 2
            self._merge_sort_helper(a, l, m)
            self._merge_sort_helper(a, m+1, r)
            self._merge(a, l, m, r)

    def _merge(self, a, l, m, r):
        left = a[l:m+1]
        right = a[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            self._record(a, [k])
            if left[i] <= right[j]:
                a[k] = left[i]; i += 1
            else:
                a[k] = right[j]; j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]; i += 1; k += 1
        while j < len(right):
            a[k] = right[j]; j += 1; k += 1

class GraphVisualizer:
    def __init__(self):
        self.steps = []

    def bfs(self, graph, start):
        self.steps = []
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            self.steps.append({"visited": node, "queue": queue[:]})
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return self.steps

    def dfs(self, graph, start):
        self.steps = []
        visited = set()
        self._dfs_helper(graph, start, visited)
        return self.steps

    def _dfs_helper(self, graph, node, visited):
        visited.add(node)
        self.steps.append({"visited": node, "stack_depth": len(visited)})
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                self._dfs_helper(graph, neighbor, visited)

if __name__ == "__main__":
    sv = SortVisualizer()
    steps = sv.quicksort([5, 3, 8, 1, 9, 2, 7, 4])
    print(f"Quicksort: {len(steps)} steps, final: {steps[-1]['array']}")
    gv = GraphVisualizer()
    graph = {"A": ["B","C"], "B": ["D","E"], "C": ["F"], "D": [], "E": [], "F": []}
    bfs_steps = gv.bfs(graph, "A")
    print(f"BFS: {[s['visited'] for s in bfs_steps]}")

from visualizer import SortVisualizer, GraphVisualizer

def test_bubble_sort():
    sv = SortVisualizer()
    steps = sv.bubble_sort([3, 1, 2])
    assert steps[-1]["array"] == [1, 2, 3]

def test_quicksort():
    sv = SortVisualizer()
    steps = sv.quicksort([5, 3, 8, 1])
    assert steps[-1]["array"] == [1, 3, 5, 8]

def test_bfs():
    gv = GraphVisualizer()
    graph = {"A": ["B", "C"], "B": [], "C": []}
    steps = gv.bfs(graph, "A")
    visited = [s["visited"] for s in steps]
    assert visited == ["A", "B", "C"]

if __name__ == "__main__":
    test_bubble_sort()
    test_quicksort()
    test_bfs()
    print("All tests passed!")

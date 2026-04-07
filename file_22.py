class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, a, b):
        self.nodes.setdefault(a, []).append(b)

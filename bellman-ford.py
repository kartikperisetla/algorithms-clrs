__author__ = 'Kartik Perisetla(kperisetla@cmu.edu)'

class Graph:
    class Vertex:
        def __init__(self):
            self.key  = -9999
            self.parent = None

    class Edge:
        def __init__(self, fromNode, toNode, weight):
            self.source = fromNode
            self.dest = toNode
            self.weight = weight


    def __init__(self):
        # collection of edges
        self.E = []
        # collection of vertices
        self.V = []
        # holding source node
        self.source = None

    def add_source(self, sourceNode):
        self.source = sourceNode

    def get_source(self):
        return self.source


# class to apply bellman ford algorithm for finding single source shortest
# path in a directed graph with negative edges
class BellmanFord(object):

    def init_single_source(self, graph):
        for v in self.V:
            v.key = -9999
            v.parent = None

        graph.get_source().key = 0

    def relax(self, edge):
        if edge.dest.key > edge.source.key + edge.weight:
            edge.dest.key = edge.source.key + edge.weight
            edge.dest.parent = edge.source

    def execute(self, graph):

        for i in range(len(graph.V)):
            for edge in graph.E:
                self.relax(edge)
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end, dist in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append((end, dist))
            else:
                self.graph_dict[start] = [(end, dist)]
        
    



for line in f:
    l_list = line.split()
    loc1 = l_list[0]
    loc2 = l_list[2]
    dist = l_list[4]
    print(loc1, loc2, dist)


import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input.txt'), 'r')

class Graph:
    def __init__(self, edges):
        self.edges = edges                      # edges argument should be list of tuples
        self.graph_dict = {}
        for start, end, dist in edges:          # refers to the tuple locations in the list
            if start in self.graph_dict:
                self.graph_dict[start].append((end, dist))
            else:
                self.graph_dict[start] = [(end, dist)]
        self.unique_locs = list(self.graph_dict.keys())
        self.paths = []
        print("Graph Dict:", self.graph_dict)


    def find_shortest(self, start, path=[0]):
        if len(path) == len(self.unique_locs)+1:
            return path

        for node, dist in self.graph_dict[start]:
            if node not in path:
                next_path = path + [node]
                next_path[0] = next_path[0] + dist
                result = self.find_shortest(node, next_path)
                if result is not None:
                    self.paths.append(result)

routes = []
for line in f:
    l_list = line.split()
    loc1 = l_list[0]
    loc2 = l_list[2]
    dist = int(l_list[4])
    routes.append((loc1, loc2, dist))
    routes.append((loc2, loc1, dist))

route_graph = Graph(routes)
print(route_graph.unique_locs, len(route_graph.unique_locs))
print('\n')

for loc in route_graph.unique_locs:
    route_graph.find_shortest(loc, path=[0, loc])

print(min(p[0] for p in route_graph.paths))
        


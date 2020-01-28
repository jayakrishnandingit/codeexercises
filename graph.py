class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # {<Vertex object>: weight, <Vertex object2>: weight2}
        
    def add_neighbor(self, v, weight=0):
        if v not in self.neighbors:
            self.neighbors.update({v: weight})
            return True
        raise Exception("%s is already a neighbor." % v)
            
    def __repr__(self):
        return '%s' % self.name


class Graph(object):
    def __init__(self):
        self.vertices = {}  # {'bilaspur': <Vertex object of bilaspur>}
        
    def add_vertex(self, name):
        if name not in self.vertices:
            vertex = Vertex(name)
            self.vertices.update({name: vertex})
        else:
            print("%s already exists." % name)
            vertex = self.vertices.get(name)
        return vertex

    def add_edge(self, v1, v2, weight=0):
        v1.add_neighbor(v2, weight)
        
    def dfs(self, v):
        stack = [v]
        visited = set([v])
        while stack:
            v = stack.pop()
            print(v)
            for each in v.neighbors:
                if each not in visited:
                    visited.add(each)
                    stack.append(each)
    
    def bfs(self, v):
        queue = [v]
        visited = set([v])
        while queue:
            v = queue.pop(0)
            print(v)
            for each in v.neighbors:
                if each not in visited:
                    visited.add(each)
                    queue.append(each)


if __name__ == '__main__':
    graph = Graph()
    rama = graph.add_vertex('Rama')
    ella = graph.add_vertex('Ella')
    katie = graph.add_vertex('Katie')
    bob = graph.add_vertex('Bob')
    graph.add_edge(rama, ella)
    graph.add_edge(rama, katie)
    graph.add_edge(rama, bob)
    graph.add_edge(ella, bob)
    lee = graph.add_vertex('Lee')
    swati = graph.add_vertex('Swati')
    graph.add_edge(katie, lee)
    graph.add_edge(katie, swati)
    sam = graph.add_vertex('Sam')
    tom = graph.add_vertex('Tom')
    graph.add_edge(bob, sam)
    graph.add_edge(bob, tom)
    graph.add_edge(bob, lee)
    zahir = graph.add_vertex('Zahir')
    arun = graph.add_vertex('Arun')
    graph.bfs(rama)

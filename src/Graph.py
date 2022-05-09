class Vertex:
    def __init__(self,id:int):
        self.type = "Test"
        self.id = id
    def getType(self):
        print(self.type)

class Graph:
    def __init__(self,size):
        self.vertex = []
        self.adj_matrix = []

        # Initializing Adjacency Matrix
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size
    def add_edge(self,v1:Vertex,v2:Vertex):
        if v1.id == v2.id:
            print("Connecting same vertex")
            return False
        self.adj_matrix[v1.id][v2.id] = 1
        self.adj_matrix[v2.id][v1.id] = 1
        return True
    def add_vertex(self):
        new_Vertex = Vertex(len(self.vertex))
        self.vertex.append(new_Vertex)
        return new_Vertex
    def print_matrix(self):
        for row in self.adj_matrix:
            print(row)


if __name__ == '__main__':
    test = Graph(5)
    v1 = test.add_vertex()
    v2 = test.add_vertex()
    v3 = test.add_vertex()
    v4 = test.add_vertex()
    v5 = test.add_vertex()
    v6 = test.add_vertex()
    test.add_edge(v1,v2)
    test.add_edge(v2, v4)
    test.add_edge(v5, v6)
    test.add_edge(v1, v6)
    test.add_edge(v1, v4)
    test.add_edge(v4, v6)
    test.print_matrix()
    print(v1.type)

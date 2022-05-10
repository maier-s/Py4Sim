class Vertex:
    def __init__(self,id:int,container=None):
        self.container = container
        self.id = id
    def getContainer(self):
        return self.container

class Graph:
    def __init__(self,size:int = 0):
        self.vertex = []
        self.adj_matrix = []

        # Initializing Adjacency Matrix
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size
    def add_edge(self,v1:Vertex,v2:Vertex,weight:int = 1):
        if v1.id == v2.id:
            print("Connecting same vertex")
            return False
        self.adj_matrix[v1.id][v2.id] = weight
        # Uncomment the following line to get undirected graph
        #self.adj_matrix[v2.id][v1.id] = weight
        return True
    def add_vertex(self,containter=None):
        new_Vertex = Vertex(len(self.vertex),containter)
        self.vertex.append(new_Vertex)
        self.__appendAdjMatrix__()
        return new_Vertex
    def print_matrix(self):
        print("Adjacency Matrix")
        for row in self.adj_matrix:
            print(row)

    def __appendAdjMatrix__(self):
        # Adding new column
        for row in self.adj_matrix:
            row.append(row[-1])
        # Adding new row
        if self.size == 0:
            self.adj_matrix.append([0])
        else:
            self.adj_matrix.append([0]*len(self.adj_matrix[0]))
        self.size = self.size + 1

    def neighbour(self,v:Vertex):
        adj_row = self.adj_matrix[v.id]
        neighbour = set()
        for idx,vertex in enumerate(adj_row):
            if vertex > 0:
                neighbour.add(idx)
        return neighbour



if __name__ == '__main__':
    test = Graph()
    v1 = test.add_vertex()
    print(test.size)
    v2 = test.add_vertex()
    v3 = test.add_vertex()
    v4 = test.add_vertex()
    print(test.size)
    v5 = test.add_vertex()
    v6 = test.add_vertex()
    print(test.size)
    test.add_edge(v1,v2)
    test.add_edge(v2, v4)
    test.add_edge(v5, v6)
    test.add_edge(v1, v6)
    test.add_edge(v1, v4)
    test.add_edge(v4, v6)
    print(test.neighbour(v1))
    test.print_matrix()

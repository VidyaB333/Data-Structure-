class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, numVertex):
        self.numVertex = numVertex
        self.adj_l = [[] for i in range(self.numVertex)]

    def add_vertex(self, i, U):
        if 0 <= i < len(self.adj_l):  # & (not self.adj_l[i])
            #print('{} is added at {} position'.format(U, i))
            new_vertex = Node(U)
            self.adj_l[i] = new_vertex
            #print(self.adj_l[i].data)

    def add_edge(self, U, V):
        index = None
        for i in range(len(self.adj_l)):
            if self.adj_l[i].data == U:
                index = i
        temp = self.adj_l[index]
        new_edge = Node(V)
        #print(temp.next)
        new_edge.next = temp.next
        temp.next = new_edge
        #print(temp.next.data)

    def neighbors(self, U):
        neigh_l = []
        for i in range(len(self.adj_l)):
            if self.adj_l[i].data == U:
                temp = self.adj_l[i]
                while temp.next:
                    temp = temp.next
                    neigh_l.append(temp.data)
                # print(neigh_l)
                return neigh_l


    def DFS(self, visited, vertex_set, DFS_l, start):
        v = self.graph_info()
        visited[v.index(start)] =1

        neighbor = self.neighbors(start)
        print('neighbor of {} : {}'.format(start, neighbor))
        for i in range(len(neighbor)):
            if visited[v.index(neighbor[i])] ==1:
                print('{} is already visited'.format(neighbor[i]))
                if i == len(neighbor)-1:
                    print('{} is out of stack '.format(vertex_set[-1]))
                    vertex_set.pop()
            else:
                if neighbor[i] in vertex_set:
                    print('{} in stack'.format(neighbor[i]))
                    pass
                else:
                    vertex_set.append(neighbor[i])
                    print('{} Added in stack'.format(neighbor[i]))
                    DFS_l.append(neighbor[i])

                    self.DFS(visited, vertex_set, DFS_l,neighbor[i])

        return  DFS_l

    def graph_info(self):
        Vertex_l = []
        for i in range(len(self.adj_l)):
            Vertex_l.append(self.adj_l[i].data)
        return Vertex_l


obj = Graph(10)

print(obj.numVertex)
print(obj.adj_l)
obj.add_vertex(0, 'a')
obj.add_vertex(1, 'b')
obj.add_vertex(2, 'c')
obj.add_vertex(3, 'd')
obj.add_vertex(4, 'e')
obj.add_vertex(5, 'f')
obj.add_vertex(6, 'g')
obj.add_vertex(7, 'k')
obj.add_vertex(8, 'h')
obj.add_vertex(9, 'i')
print(obj.graph_info())
obj.add_edge('a', 'd')
obj.add_edge('a', 'c')
obj.add_edge('a', 'b')
obj.add_edge('b', 'a')
obj.add_edge('b', 'f')
obj.add_edge('b', 'e')
obj.add_edge('c', 'a')
obj.add_edge('c', 'g')
obj.add_edge('c', 'f')
obj.add_edge('d', 'a')
obj.add_edge('d', 'k')
obj.add_edge('e', 'b')
obj.add_edge('f', 'c')
obj.add_edge('f', 'b')
obj.add_edge('f', 'i')
obj.add_edge('f', 'h')
obj.add_edge('g', 'c')
obj.add_edge('g', 'i')
obj.add_edge('k', 'd')
obj.add_edge('h', 'f')
obj.add_edge('i', 'g')
obj.add_edge('i', 'f')

Vertex_l = obj.graph_info()
for i in Vertex_l:
    pass
    #print('for {}, neighbors :{}'.format(i, obj.neighbors(i)))

visited = [0 for i in range(obj.numVertex)]
print(visited)
start_vertex = 'e'
vertex_set = [start_vertex]
DFS_l = [start_vertex]
DFS_l = obj.DFS( visited, vertex_set, DFS_l, start_vertex)
print('DFS Traversal: ',DFS_l)
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

    def BFS(self, visited, V_under_cons,BFS_list, start):

        BFS_list.append(start)

        #List of all Vertices
        Vertices_list = self.graph_info()

        start_index = (Vertices_list.index(start))
        #print('Start Node for BFS : {} and index : {}'.format( start, start_index))

        #Vertex at start_index has traversed
        visited[start_index] = 1

        #neighbors to add in queue for BFS Traversal
        neighbors = self.neighbors(start)
        #print('neighbors for {} are {}'.format(start, neighbors))
        for i in neighbors:
            index_= Vertices_list.index(i)
            #print(i, index_)
            if visited[index_]==1:
                #print('Vertex is alredy visited')
                pass
            elif visited[index_] !=1:
                if i in V_under_cons:
                    #print('Vertex not visited yet but in the list of vertex consideration')
                    pass
                else:
                    #print('Vertex not visited yet and not in the list of vertex consideration.. so added')
                    V_under_cons.append(i)
                    #print(V_under_cons)

        V_under_cons.pop(0)
        #print('Vertex to consider: ', V_under_cons)

        for i in V_under_cons:
            self.BFS(visited, V_under_cons,BFS_list, i)
        return BFS_list


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
obj.add_edge('a', 'b')
obj.add_edge('a', 'c')
obj.add_edge('a', 'd')
obj.add_edge('b', 'e')
obj.add_edge('b', 'f')
obj.add_edge('b', 'a')
obj.add_edge('c', 'f')
obj.add_edge('c', 'g')
obj.add_edge('c', 'a')
obj.add_edge('d', 'k')
obj.add_edge('d', 'a')
obj.add_edge('e', 'b')
obj.add_edge('f', 'h')
obj.add_edge('f', 'i')
obj.add_edge('f', 'b')
obj.add_edge('f', 'c')
obj.add_edge('g', 'i')
obj.add_edge('g', 'c')
obj.add_edge('k', 'd')
obj.add_edge('h', 'f')
obj.add_edge('i', 'f')
obj.add_edge('i', 'g')

Vertex_l = obj.graph_info()
for i in Vertex_l:
    pass
    #print('for {}, neighbors :{}'.format(i, obj.neighbors(i)))

#For boolean checking for cyclic graphs
visited = [0 for i in range(obj.numVertex)]
start_vertex = 'a'

#This is going to be queue, Vertices are going to add or removed as per the traversal
V_under_cons = [start_vertex]

#List for BFS Traversal
BFS_list =[]

Traversal = obj.BFS(visited, V_under_cons, BFS_list, start_vertex)
print('BFS Traversal of Graph : ', Traversal)

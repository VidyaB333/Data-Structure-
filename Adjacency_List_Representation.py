class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, NumVertix):
        self.NumVertix = NumVertix
        self.Adjacency_L = [[] * NumVertix for i in range(NumVertix)]

    def Info(self):
        print('No of Vertices: ', self.NumVertix)
        print('Adjacency List: ', self.Adjacency_L)
        for i in range(self.NumVertix):
            v = self.Adjacency_L[i]
            # print(type(v))

    def add_edge(self, i, edge_vertex):
        print('Adding edge vertex at the start of LL')
        New_Vertex = Node(edge_vertex)
        print('New Vertex: ', New_Vertex.data)
        # print(New_Vertex)
        if not self.Adjacency_L[i]:
            print('Inside if block... First Vertex')
            self.Adjacency_L[i] = New_Vertex
        else:
            # print('In else block.. not first block')
            temp = self.Adjacency_L[i]
            # print(temp.data)

            New_Vertex.next = temp.next
            temp.next = New_Vertex

    def add_vertex(self, i, Vertex):
        if (0 <= i < self.NumVertix) & (not self.Adjacency_L[i]):
            Vertex_Node = Node(Vertex)
            self.Adjacency_L[i] = Vertex_Node
            print('Added Vertex at {} position : {}'.format(i, Vertex_Node.data))

    def remove_vertex(self, U):

        for i in range(self.NumVertix):
            if U == self.Adjacency_L[i].data:
                print(self.Adjacency_L.pop(i))
                print('popped')
                break

    def remove_edge(self, U, V):
        index = None
        prev = None
        for i in range(len(self.Adjacency_L)):
            if self.Adjacency_L[i].data == U:
                index = i
                break
        print('{} occurs at {} index'.format(U, index))

        # Traversing the ith LL to remove edge
        temp = self.Adjacency_L[index]
        while temp:
            print(temp.data)
            if temp.data == V:
                prev.next = temp.next
            prev = temp
            temp = temp.next

    def adjacency_check(self, U, V):
        # Finding Index of U in Adjecency list
        index = None
        for j in range(self.NumVertix):
            if U == self.Adjacency_L[j].data:
                index = j
                print('index of {} is {}'.format(U, index))

        # Traversing LL at given index
        temp = self.Adjacency_L[index]
        while temp:
            print(temp.data)
            if temp.data == V:
                print('{} and {} are adject to each other'.format(U, V))
                return True
            temp = temp.next
        print('{} and {} are not adject to each other'.format(U, V))
        return False

    def View_graph(self):
        print('View Graph')
        for i in range(len(self.Adjacency_L)):
            if not self.Adjacency_L[i]:
                print('%d index is empty' % i)
                return
            else:
                print('%d index not empty' % i)
                temp = self.Adjacency_L[i]
                while temp:
                    print('Vertex: ', temp.data)
                    temp = temp.next
        print('Done with displaying the vertices')

    def neighbors(self, U):
        index = None
        for i in range(self.NumVertix):
            if U == self.Adjacency_L[i].data:
                index = i

        # Neighbors for vertix
        temp = self.Adjacency_L[index]
        l_neigh = []
        while temp.next:
            temp = temp.next
            l_neigh.append(temp.data)

        return l_neigh


obj = Graph(4)
obj.Info()

obj.add_vertex(0, 'a')
obj.add_vertex(2, 'c')
obj.add_vertex(1, 'b')
obj.add_vertex(3, 'd')
# obj.add_vertex(2, 'a')
obj.Info()
# obj.View_graph()

print('adding edges')
obj.add_edge(0, 'c')
obj.add_edge(0, 'd')
obj.add_edge(0, 'b')
obj.add_edge(1, 'd')
obj.add_edge(1, 'c')
obj.add_edge(2, 'd')
obj.add_edge(2, 'a')
obj.add_edge(3, 'a')
obj.add_edge(3, 'c')
obj.Info()

print(obj.adjacency_check('a', 'c'))
print(obj.adjacency_check('d', 'b'))
obj.View_graph()

print('Checking Neighbors')
print(obj.neighbors('a'))
print(obj.neighbors('c'))
obj.remove_vertex('c')
obj.View_graph()

obj.remove_edge('a', 'd')
obj.remove_edge('d', 'a')
obj.View_graph()

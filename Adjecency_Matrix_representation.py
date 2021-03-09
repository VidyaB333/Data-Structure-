import numpy as np


class Graph:
    def __init__(self, No_of_Vertices):
        self.No_of_Vertices = No_of_Vertices
        self.Vertices_list = No_of_Vertices * [0]
        self.Matrix = [[0] * No_of_Vertices for i in range(No_of_Vertices)]

    def Vertices(self, i, Vertex):
        self.Vertices_list[i] = Vertex

    def Set_Edges(self, a, b, wt):
        a = self.Vertices_list.index(a)
        b = self.Vertices_list.index(b)
        # print(a, b)
        self.Matrix[a][b] = wt
        self.Matrix[b][a] = wt

    def Get_Edges(self):
        Edges = []
        for i in range(self.No_of_Vertices):
            for j in range(self.No_of_Vertices):
                if self.Matrix[i][j] != 0:
                    Edges.append((self.Vertices_list[i], self.Vertices_list[j], self.Matrix[i][j]))
        return Edges

    def Info(self):
        print('Vertices list: ', self.Vertices_list)
        print('No of Vertices: ', self.No_of_Vertices)
        print('Adjecency_m: ', self.Matrix)
        print('No of Edges: ', len(self.Get_Edges()))


graph_obj = Graph(4)
graph_obj.Vertices(2, 'C')
graph_obj.Vertices(3, 'D')
graph_obj.Vertices(0, 'A')
graph_obj.Vertices(1, 'B')
graph_obj.Set_Edges('A', 'D', 13)
graph_obj.Set_Edges('D', 'B', 12)
graph_obj.Set_Edges('A', 'B', 3)
graph_obj.Set_Edges('B', 'D', 9)
graph_obj.Set_Edges('C', 'A', 5)
graph_obj.Info()
print(graph_obj.Get_Edges())

"""
matrix = np.array([[0, 1, 0, 0, 1],
                   [1, 0, 1, 1, 1],
                   [0, 1, 0, 1, 0],
                   [0, 1, 1, 0, 1],
                   [1, 1, 0, 1, 0]])
print(matrix)
a =2; b=2
matrix[a][b]
print()
if matrix[a][b] != 0:
    print('Vertix starting from {} to {} do exists'.format(a,b))
else:
    print('Vertix starting from {} to {} doesnot exists'.format(a, b))
"""

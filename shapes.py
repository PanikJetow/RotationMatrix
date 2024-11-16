import numpy as np

class Shape:
    def __init__(self, shape, start_coord=[0,0,0], edge_length = 10):
        if shape == "CUBE":
            self.buildCube(start_coord, edge_length)
                           
    def buildCube(self, start_coord, edge_length):
        try:
            vectors = [[edge_length,0,0],[0,edge_length,0],[0,0,edge_length]]
            self.vertices = []
            self.vertices.append(np.array(start_coord))
            self.vertices.append(np.array(start_coord) + np.array(vectors[0]))
            self.vertices.append(np.array(start_coord) + np.array(vectors[0]) + np.array(vectors[1]))
            self.vertices.append(np.array(start_coord) + np.array(vectors[1]))
            self.vertices.append(np.array(start_coord) + np.array(vectors[2]))
            self.vertices.append(np.array(start_coord) + np.array(vectors[0]) + np.array(vectors[2]))
            self.vertices.append(np.array(start_coord) + np.array(vectors[0]) + np.array(vectors[1]) + np.array(vectors[2]))
            self.vertices.append(np.array(start_coord) + np.array(vectors[1]) + np.array(vectors[2]))
            self.vertices = np.array(self.vertices)
            return self
        except Exception as exception:
            print(exception)
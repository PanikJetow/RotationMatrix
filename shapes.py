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

    def rotate(self, a = 0, b = 0, c = 0) -> np.ndarray:
        a = np.deg2rad(a)
        b = np.deg2rad(b)
        c = np.deg2rad(c)
        sina = np.sin(a); cosa = np.cos(a); sinb = np.sin(b); cosb = np.cos(b); sinc = np.sin(c); cosc = np.cos(c)

        R = np.array([[cosa * cosb, cosa * sinb * sinc - sina * cosc, cosa * sinb * cosc + sina * sinc], [sina * cosb, sina * sinb * sinc + cosa * cosc, sina * sinb * cosc - cosa * sinc], [-sinb, cosb * sinc, cosb * cosc]])
        self.vertices = np.dot(self.vertices, R)
        return self
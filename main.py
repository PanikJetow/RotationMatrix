import numpy as np

def main():
	shape_vertices = (buildCube([0,0,0], 20))
	print(shape_vertices)
	print(rotate(shape_vertices, 0, 180, 0))
	return 0

def buildCube(start_coord, edge_length):
	try:
		vectors = [[edge_length,0,0],[0,edge_length,0],[0,0,edge_length]]
		cube = []
		cube.append(np.array(start_coord))
		cube.append(np.array(start_coord) + np.array(vectors[0]))
		cube.append(np.array(start_coord) + np.array(vectors[0]) + np.array(vectors[1]))
		cube.append(np.array(start_coord) + np.array(vectors[1]))

		cube.append(np.array(start_coord) + np.array(vectors[2]))
		cube.append(np.array(start_coord) + np.array(vectors[0]) + np.array(vectors[2]))
		cube.append(np.array(start_coord) + np.array(vectors[0]) + np.array(vectors[1]) + np.array(vectors[2]))
		cube.append(np.array(start_coord) + np.array(vectors[1]) + np.array(vectors[2]))

		return np.array(cube)
	except Exception as exception:
		print(exception)
		#if len(start_coord) != 3:
		#	print(f"Error: start_coord must be a list of 3 integers, not {type(start_coord)}")
		#	return None
		#elif edge_length < 0 or type(edge_length) != int:
		#	print(f"Error: edge_length must be a positive integer, not {type(edge_length)}")

def rotate(vertices, a = 0, b = 0, c = 0):
	a = np.deg2rad(a)
	b = np.deg2rad(b)
	c = np.deg2rad(c)
	sina = np.sin(a); cosa = np.cos(a); sinb = np.sin(b); cosb = np.cos(b); sinc = np.sin(c); cosc = np.cos(c)

	R = np.array([[cosa * cosb, cosa * sinb * sinc - sina * cosc, cosa * sinb * cosc + sina * sinc], [sina * cosb, sina * sinb * sinc + cosa * cosc, sina * sinb * cosc - cosa * sinc], [-sinb, cosb * sinc, cosb * cosc]])
	rotated = np.dot(vertices, R)
	return rotated


if __name__ == "__main__":
	main()

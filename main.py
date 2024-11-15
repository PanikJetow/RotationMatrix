import math

def main():
	print(buildCube([1,1,1], 10))
	return 0

def buildCube(start_coord, edge_length):
	try:
		cube = []
		for x1 in range(start_coord[0], start_coord[0] + edge_length):
			for x2 in range(start_coord[1], start_coord[1] + edge_length):
				for x3 in range(start_coord[2], start_coord[2] + edge_length):
					cube.append([x1, x2, x3])
		return cube
	except:
		if len(start_coord) != 3:
			print(f"Error: start_coord must be a list of 3 integers, not {type(start_coord)}")
			return None
		elif edge_length < 0 or type(edge_length) != int:
			print(f"Error: edge_length must be a positive integer, not {type(edge_length)}")

if __name__ == "__main__":
	main()
test
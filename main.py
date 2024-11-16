import numpy as np
import pygame
import shapes

def main():
	pygame.init()
	screen = pygame.display.set_mode((1920, 1080))
	clock = pygame.time.Clock()
	running = True
	dt = 0
	cube = shapes.Shape("CUBE")
	cube = rotate(cube, 0, 0, 0)
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

    # fill the screen with a color to wipe away anything from last frame
		screen.fill("black")
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			rotate(cube, 0, 10 * dt)
		if keys[pygame.K_a]:
			rotate(cube, 10 * dt)
		if keys[pygame.K_s]:
			rotate(cube, 0, -10 * dt)
		if keys[pygame.K_d]:
			rotate(cube, -10 * dt)

		for i in cube.vertices:
			print(i)
			pygame.draw.circle(screen, "red", (1920/2 + i[1] * 5, 1080/2 + i[2] * 5), 1)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

	pygame.quit()
	return 0

def rotate(shape_object: np.ndarray, a = 0, b = 0, c = 0) -> np.ndarray:
	a = np.deg2rad(a)
	b = np.deg2rad(b)
	c = np.deg2rad(c)
	sina = np.sin(a); cosa = np.cos(a); sinb = np.sin(b); cosb = np.cos(b); sinc = np.sin(c); cosc = np.cos(c)

	R = np.array([[cosa * cosb, cosa * sinb * sinc - sina * cosc, cosa * sinb * cosc + sina * sinc], [sina * cosb, sina * sinb * sinc + cosa * cosc, sina * sinb * cosc - cosa * sinc], [-sinb, cosb * sinc, cosb * cosc]])
	shape_object.vertices = np.dot(shape_object.vertices, R)
	return shape_object


if __name__ == "__main__":
	main()

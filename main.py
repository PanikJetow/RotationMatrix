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




if __name__ == "__main__":
	main()

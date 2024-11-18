import pygame
import random
from constants import *

mole_image = pygame.image.load('mole.png')
screen = pygame.display.set_mode((640, 512))

def draw_mole(screen, x , y):
    screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

def draw_grid():
    # draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (1, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    for i in range(0, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def move_mole(event):
    if event.type == pygame.MOUSEBUTTONUP:
        row_range = random.randrange(0, WIDTH , SQUARE_SIZE)
        column_range = random.randrange(0, HEIGHT, SQUARE_SIZE)
        draw_mole(screen, row_range, column_range)
        pygame.display.flip()
        return row_range, column_range

def main():
    try:
        pygame.init()
        clock = pygame.time.Clock()
        mole_x = 0
        mole_y = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mole_x , mole_y = move_mole(event)

            screen.fill("light green")
            draw_grid()
            draw_mole(screen, mole_x, mole_y)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

#Do this once you are done with the whole thing
#git add .
#git commit -m "Hello"
#git push
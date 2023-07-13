import pygame
import time
from game import Game
from pygame import mixer
pygame.init()
win = pygame.display.set_mode((800, 800))
# Size 800x800 so that the cube is 100x100
pygame.display.set_caption("Шашки")
mixer.music.load("song.mp3")
mixer.music.play(-1)
def get_pos_from_mouse(position):
    x, y = position
    row = y // 100
    column = x // 100
    return row, column
def main():
    game = Game(win)
    g = True
    while g:
        if game.winner() != None:
            time.sleep(10)
            main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g = False
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                row, column = get_pos_from_mouse(position)
                game.select_checker(row, column)
        game.update_board()
    pygame.quit()


main()

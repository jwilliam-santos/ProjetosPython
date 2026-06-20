#IMPORTS
from src import Game
import pygame
import sys
from src.game import Game

def main():
  
    pygame.init()
    pygame.mixer.init() #

  
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong 2.0")
    
  
    clock = pygame.time.Clock()

    game = Game(screen)

    
    running = True
    while running:
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.handle_input()

     
        game.update()

        game.draw()

        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
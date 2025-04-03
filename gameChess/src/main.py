import pygame
import sys
from components.chessboard import Chessboard

def main():
    pygame.init()
    
    WINDOW_SIZE = (640, 640)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Chess Game")
    
    chessboard = Chessboard(screen)
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    chessboard.handle_click(event.pos)
        
        screen.fill((255, 255, 255))
        chessboard.draw()
        
        if chessboard.is_game_over():
            result = chessboard.get_game_result()
            text = font.render(result, True, (0, 0, 0))
            text_rect = text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
            screen.blit(text, text_rect)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 
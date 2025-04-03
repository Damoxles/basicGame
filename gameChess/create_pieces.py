import pygame
import os

def create_piece_image(symbol, color):
    size = 200
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    if color == 'w':
        piece_color = (255, 255, 255)
        background_color = (0, 0, 0)
    else:
        piece_color = (0, 0, 0)
        background_color = (255, 255, 255)
    
    if symbol.lower() == 'p':
        pygame.draw.circle(surface, background_color, (size//2, size//2), size//4)
        pygame.draw.circle(surface, piece_color, (size//2, size//2), size//4)
        pygame.draw.circle(surface, background_color, (size//2, size//3), size//6)
        pygame.draw.circle(surface, piece_color, (size//2, size//3), size//6)
    elif symbol.lower() == 'r':
        pygame.draw.rect(surface, background_color, (size//4, size//4, size//2, size//2))
        pygame.draw.rect(surface, piece_color, (size//4, size//4, size//2, size//2))
        pygame.draw.rect(surface, background_color, (size//3, size//6, size//3, size//6))
        pygame.draw.rect(surface, piece_color, (size//3, size//6, size//3, size//6))
    elif symbol.lower() == 'n':
        points = [(size//4, size//2), (size//2, size//4), (3*size//4, size//2), (size//2, 3*size//4)]
        pygame.draw.polygon(surface, background_color, points)
        pygame.draw.polygon(surface, piece_color, points)
    elif symbol.lower() == 'b':
        pygame.draw.circle(surface, background_color, (size//2, size//2), size//3)
        pygame.draw.circle(surface, piece_color, (size//2, size//2), size//3)
        pygame.draw.polygon(surface, background_color, [(size//2, size//4), (3*size//4, size//2), (size//2, 3*size//4), (size//4, size//2)])
        pygame.draw.polygon(surface, piece_color, [(size//2, size//4), (3*size//4, size//2), (size//2, 3*size//4), (size//4, size//2)])
    elif symbol.lower() == 'q':
        pygame.draw.circle(surface, background_color, (size//2, size//2), size//3)
        pygame.draw.circle(surface, piece_color, (size//2, size//2), size//3)
        for i in range(8):
            angle = i * 45
            x = size//2 + size//3 * pygame.math.Vector2(1, 0).rotate(angle).x
            y = size//2 + size//3 * pygame.math.Vector2(1, 0).rotate(angle).y
            pygame.draw.circle(surface, background_color, (int(x), int(y)), size//8)
            pygame.draw.circle(surface, piece_color, (int(x), int(y)), size//8)
    elif symbol.lower() == 'k':
        pygame.draw.circle(surface, background_color, (size//2, size//2), size//3)
        pygame.draw.circle(surface, piece_color, (size//2, size//2), size//3)
        pygame.draw.rect(surface, background_color, (size//2-size//6, size//4, size//3, size//2))
        pygame.draw.rect(surface, piece_color, (size//2-size//6, size//4, size//3, size//2))
    
    return surface

def main():
    pygame.init()
    
    if not os.path.exists('src/assets'):
        os.makedirs('src/assets')
    
    pieces = ['p', 'r', 'n', 'b', 'q', 'k']
    for piece in pieces:
        image = create_piece_image(piece, 'b')
        pygame.image.save(image, f'src/assets/{piece}.png')
        
        image = create_piece_image(piece, 'w')
        pygame.image.save(image, f'src/assets/{piece.upper()}.png')
    
    pygame.quit()

if __name__ == '__main__':
    main() 
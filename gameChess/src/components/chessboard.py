import pygame
import chess

class Chessboard:
    def __init__(self, screen, square_size=80):
        self.screen = screen
        self.square_size = square_size
        self.board = chess.Board()
        self.selected_square = None
        self.valid_moves = []
        self.pieces = {}
        self.load_pieces()
        
    def load_pieces(self):
        piece_files = {
            'P': 'P.png', 'R': 'R.png', 'N': 'N.png', 'B': 'B.png', 'Q': 'Q.png', 'K': 'K.png',
            'p': 'p.png', 'r': 'r.png', 'n': 'n.png', 'b': 'b.png', 'q': 'q.png', 'k': 'k.png'
        }
        
        for piece, file in piece_files.items():
            try:
                image = pygame.image.load(f'src/assets/{file}')
                self.pieces[piece] = pygame.transform.scale(image, (self.square_size, self.square_size))
            except:
                print(f"Failed to load piece: {file}")
    
    def draw(self):
        for row in range(8):
            for col in range(8):
                x = col * self.square_size
                y = row * self.square_size
                color = (240, 217, 181) if (row + col) % 2 == 0 else (181, 136, 99)
                
                if self.selected_square and chess.square(col, 7-row) == self.selected_square:
                    color = (124, 192, 254)
                elif chess.square(col, 7-row) in self.valid_moves:
                    color = (124, 192, 254)
                
                pygame.draw.rect(self.screen, color, (x, y, self.square_size, self.square_size))
                
                piece = self.board.piece_at(chess.square(col, 7-row))
                if piece:
                    piece_surface = self.pieces.get(piece.symbol())
                    if piece_surface:
                        self.screen.blit(piece_surface, (x, y))
    
    def handle_click(self, pos):
        col = pos[0] // self.square_size
        row = pos[1] // self.square_size
        square = chess.square(col, 7-row)
        
        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.valid_moves = [move.to_square for move in self.board.legal_moves if move.from_square == square]
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
            self.selected_square = None
            self.valid_moves = []
    
    def is_game_over(self):
        return self.board.is_game_over()
    
    def get_game_result(self):
        if self.board.is_checkmate():
            return "Checkmate! " + ("Black" if self.board.turn else "White") + " wins!"
        elif self.board.is_stalemate():
            return "Stalemate! The game is a draw."
        elif self.board.is_insufficient_material():
            return "Draw due to insufficient material."
        elif self.board.is_fifty_moves():
            return "Draw due to fifty-move rule."
        elif self.board.is_repetition():
            return "Draw due to repetition."
        return None 
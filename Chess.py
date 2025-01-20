import pygame

pygame.init()

Width = 750
Height = 750

screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Chess')
font = pygame.font.Font('Montserrat-Black.ttf', 0)
medium_font = pygame.font.Font('Montserrat-Black.ttf', 40)
big_font = pygame.font.Font('Montserrat-Black.ttf', 40)
timer = pygame.time.Clock()
fps = 60


# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/black-queen.png')
black_queen = pygame.transform.scale(black_queen, (70, 70))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/black-king.png')
black_king = pygame.transform.scale(black_king, (70, 70))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/black-rook.png')
black_rook = pygame.transform.scale(black_rook, (70, 70))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/black-bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (70, 70))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/black-knight.png')
black_knight = pygame.transform.scale(black_knight, (70, 70))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/black-pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (60, 60))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/white-queen.png')
white_queen = pygame.transform.scale(white_queen, (70, 70))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/white-king.png')
white_king = pygame.transform.scale(white_king, (70, 70))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/white-rook.png')
white_rook = pygame.transform.scale(white_rook, (70, 70))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/white-bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (70, 70))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/white-knight.png')
white_knight = pygame.transform.scale(white_knight, (70, 70))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('c:/Users/user/Desktop/CHESS game/artwork/white-pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (60, 60))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']



# Game Variables
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0
selection = 100
valid_moves = []

counter =0



# Draw the chess board
def  draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, '#FFF2DA' , [(600 - (column*200))/1.33, row*100/1.33, 75, 75 ]) 
        else:
            pygame.draw.rect(screen, '#FFF2DA' , [(700 - (column*200))/1.33, row*100/1.33, 75, 75 ]) 
        pygame.draw.rect(screen , '#454545' , [0,600,Width-150,150])
        pygame.draw.rect(screen , '#27432D' , [0,600,Width-145,150] ,5)
        pygame.draw.rect(screen , '#27432D' , [600,0,150,Height] ,5)

        status_test = ['White: Select piece','White: Select destination','Black: Select piece','Black: Select destination']
        screen.blit(big_font.render(status_test[turn_step], True , 'white'),(15,650))
  

# Draw Pieces on the board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn,(white_locations[i][0] * 75 + 8,white_locations[i][1] *75 +8))
        else:
            screen.blit(white_images[index],(white_locations[i][0] * 75 +2 ,white_locations[i][1] *75 +4))
        if turn_step <2:
          if selection == i:
            pygame.draw.rect(screen , '#AFC363' , [white_locations[i][0]*75,white_locations[i][1]*75 , 75,75], 5)

    
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn,(black_locations[i][0] *75 +8 ,black_locations[i][1] *75 +8))
        else:
            screen.blit(black_images[index],(black_locations[i][0] * 75 +4 ,black_locations[i][1] *75 +4))

        if turn_step >=2:
           if selection == i:
            pygame.draw.rect(screen , '#AFC363' , [black_locations[i][0]*75,black_locations[i][1]*75 , 75,75], 5)


# Check For Valid moves
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# Check valid Pawn moves
def check_pawn(position , color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    else:
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    return moves_list


# Check valid Rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# Check valid Knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# Check valid Bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'black':
        enemies_list = white_locations
        friends_list = black_locations
    else:
        friends_list = white_locations
        enemies_list = black_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# Check valid Queen moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# Check valid King moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Check For valid moves for selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
  
    valid_option = options_list[selection]
    return valid_option
    

# Draw valid moves on board
def draw_valid(moves):
    if turn_step<2:
        color = '#AFC363'
    else: 
        color = '#AFC363'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color , (moves[i][0]*75+38, moves[i][1]*75+38),20)


# Draw captured pieces on side of the board
def draw_captured_pieces():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (625, 5 + 40 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (675, 5 + 40 * i))


# Draw flashing square on King when checked
def draw_check():
    checked = False
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 75 + 1,
                                                              white_locations[king_index][1] * 75 + 1, 75, 75], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [black_locations[king_index][0] * 75 + 1,
                                                           black_locations[king_index][1] * 75 + 1, 75, 75], 5)
                 

# Check if the king is in check
def is_king_in_check(king_location, opponent_moves):
    """
    Determine if the king is in check.
    
    Args:
        king_location (tuple): Position of the king (x, y).
        opponent_moves (list): List of all opponent moves.

    Returns:
        bool: True if the king is in check, False otherwise.
    """
    for move_list in opponent_moves:
        if king_location in move_list:
            return True
    return False


# Options to move when king is in check
def filter_moves_to_resolve_check(player_color, player_pieces, player_locations, opponent_moves):
    # Determine opponent details based on the player color
    if player_color == 'white':
        opponent_pieces = black_pieces
        opponent_locations = black_locations
        opponent_color = 'black'
    else:  # player_color == 'black'
        opponent_pieces = white_pieces
        opponent_locations = white_locations
        opponent_color = 'white'
    
    filtered_moves = []
    
    # Determine the king's location
    king_index = player_pieces.index('king')
    king_location = player_locations[king_index]
    
    # Find the pieces checking the king
    checking_pieces = [
        opponent_locations[i]
        for i, moves in enumerate(opponent_moves)
        if king_location in moves
    ]
    
    for i, moves in enumerate(check_options(player_pieces, player_locations, player_color)):
        valid_moves = []
        for move in moves:
            # Simulate the move
            original_position = player_locations[i]
            player_locations[i] = move
            
            # Recalculate opponent moves after the simulated move
            simulated_opponent_moves = check_options(opponent_pieces, opponent_locations, opponent_color)
            
            # For the king, ensure the move doesn't place it in a threatened square
            if i == king_index:
                if move not in [square for move_list in simulated_opponent_moves for square in move_list]:
                    valid_moves.append(move)
            else:
                # Check if the move captures a piece checking the king
                if move in checking_pieces:
                    valid_moves.append(move)
                # Check if the move blocks the check
                elif not is_king_in_check(king_location, simulated_opponent_moves):
                    valid_moves.append(move)
            
            # Revert the move
            player_locations[i] = original_position
        
        filtered_moves.append(valid_moves)
    
    return filtered_moves


# Main Loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0

    screen.fill('#54854E')
    draw_board()
    draw_pieces()
    draw_captured_pieces()
    draw_check()

    if selection != 100:
        valid_moves = check_valid_moves()
        
        # Restrict moves if the king is in check
        if turn_step < 2:  # White's turn
            if is_king_in_check(white_locations[white_pieces.index('king')], black_options):
                valid_moves = filter_moves_to_resolve_check(
                    'white', white_pieces, white_locations, black_options
                )[selection]
        else:  # Black's turn
            if is_king_in_check(black_locations[black_pieces.index('king')], white_options):
                valid_moves = filter_moves_to_resolve_check(
                    'black', black_pieces, black_locations, white_options
                )[selection]
                
        draw_valid(valid_moves)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_cord = event.pos[0] // 75
            y_cord = event.pos[1] // 75
            click_cord = (x_cord, y_cord)
            
            if turn_step <= 1:  # White's turn
                if click_cord in white_locations:
                    selection = white_locations.index(click_cord)
                    if turn_step == 0:
                        turn_step = 1
                if click_cord in valid_moves and selection != 100:
                    white_locations[selection] = click_cord
                    if click_cord in black_locations:
                        black_piece = black_locations.index(click_cord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = [0]

            if turn_step > 1:  # Black's turn
                if click_cord in black_locations:
                    selection = black_locations.index(click_cord)
                    if turn_step == 2:
                        turn_step = 3
                if click_cord in valid_moves and selection != 100:
                    black_locations[selection] = click_cord
                    if click_cord in white_locations:
                        white_piece = white_locations.index(click_cord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = [0]

    pygame.display.flip()
pygame.quit()

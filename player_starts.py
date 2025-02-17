import pygame
import random
import sys

# Initialize Tic-Tac-Toe board
def initialize_board():
    return [' ' for _ in range(9)]

# Check for win, draw, or ongoing game
def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return 'Draw' if ' ' not in board else None

# Available actions
def available_actions(board):
    return [i for i, x in enumerate(board) if x == ' ']

# Take action
def take_action(board, action, player):
    new_board = board.copy()
    new_board[action] = player
    return new_board

# Convert board to a state string
def board_to_state(board):
    return ''.join(board)

# Q-Learning Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate

# Initialize Q-table
Q = {}

# Choose an action based on the Q-table and available moves
def choose_action(state, available_moves, is_opponent=False):
    global Q
    if state not in Q:
        Q[state] = [0] * 9  # Initialize Q-values for all actions

    if random.uniform(0, 1) < epsilon:  # Random exploration
        return random.choice(available_moves)
    else:
        if is_opponent:  # Opponent minimizes AI's Q-value
            best_action = min(available_moves, key=lambda a: Q[state][a])
        else:  # AI maximizes its own Q-value
            best_action = max(available_moves, key=lambda a: Q[state][a])
        return best_action

# Training loop
def train_q_learning(episodes=300000):
    global Q
    for _ in range(episodes):
        board = initialize_board()
        state = board_to_state(board)
        player = 'O'
        
        while True:
            # Ensure state exists in Q-table
            if state not in Q:
                Q[state] = [0] * 9  # Initialize Q-values for all actions

            # Get available actions and choose an action
            available_moves = available_actions(board)
            action = choose_action(state, available_moves, is_opponent=(player == 'O'))

            # Take action and observe new state
            new_board = take_action(board, action, player)
            new_state = board_to_state(new_board)

            # Reward system
            winner = check_winner(new_board)
            if winner == 'X':  # AI (Player X) wins
                reward = 1
                Q[state][action] += alpha * (reward - Q[state][action])
                break
            elif winner == 'O':  # Opponent (Player O) wins
                reward = -1
                Q[state][action] += alpha * (reward - Q[state][action])
                break
            elif winner == 'Draw':  # Draw
                reward = 0
                Q[state][action] += alpha * (reward - Q[state][action])
                break
            else:  # Game continues
                reward = 0
                if new_state not in Q:
                    Q[new_state] = [0] * 9  # Initialize Q-values for all actions in the new state

                # Use minimax approach
                if player == 'X':  # AI maximizes reward
                    max_opponent_Q = max(Q[new_state][a] for a in available_actions(new_board))
                    Q[state][action] += alpha * (reward + gamma * max_opponent_Q - Q[state][action])
                else:  # Opponent minimizes reward
                    min_opponent_Q = min(Q[new_state][a] for a in available_actions(new_board))
                    Q[state][action] += alpha * (reward + gamma * min_opponent_Q - Q[state][action])
            
            # Switch player
            player = 'O' if player == 'X' else 'X'
            state, board = new_state, new_board

# Visualize the game with Pygame
def play_with_pygame():
    pygame.init()

    # Screen settings
    screen_size = 300
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Tic-Tac-Toe AI")
    font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None, 40)
    board = initialize_board()

    # Draw the board
    def draw_board():
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 5)
        pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 5)

        for i in range(9):
            x = (i % 3) * 100 + 50
            y = (i // 3) * 100 + 50
            if board[i] == 'X':
                text = font.render('X', True, (255, 0, 0))
                screen.blit(text, text.get_rect(center=(x, y)))
            elif board[i] == 'O':
                text = font.render('O', True, (0, 0, 255))
                screen.blit(text, text.get_rect(center=(x, y)))

    # Display the winner
    def display_winner(winner):
        pygame.time.wait(1000)  # Wait 1 second before displaying result
        screen.fill((255, 255, 255))
        if winner == 'X':
            message = "AI Wins!"
        elif winner == 'O':
            message = "You Win!"
        else:
            message = "It's a Draw!"
        text = small_font.render(message, True, (0, 0, 0))
        screen.blit(text, text.get_rect(center=(150, 150)))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait 3 seconds before closing
        pygame.quit()
        sys.exit()

    # Convert mouse click to board index
    def get_board_index(mouse_pos):
        x, y = mouse_pos
        row = y // 100
        col = x // 100
        return row * 3 + col

    # Main game loop
    running = True
    player_turn = True
    while running:
        draw_board()
        pygame.display.flip()

        # AI turn
        if not player_turn:
            state = board_to_state(board)
            available_moves = available_actions(board)
            ai_action = choose_action(state, available_moves, is_opponent=False)
            board = take_action(board, ai_action, 'X')
            player_turn = True

        # Check for game end after AI move
        winner = check_winner(board)
        if winner:
            draw_board()
            pygame.display.flip()
            display_winner(winner)

        # Player turn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                index = get_board_index(pygame.mouse.get_pos())
                if board[index] == ' ':
                    board[index] = 'O'
                    player_turn = False

        # Check for game end
        winner = check_winner(board)
        if winner:
            draw_board()
            pygame.display.flip()
            display_winner(winner)
        

# Train the AI and play
print("Training the AI... Please wait.")
train_q_learning()
print("Training complete! Starting the game...")
play_with_pygame()

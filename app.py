import sys

import pygame

pygame.init()

# --- Constants ---
WIDTH, HEIGHT = 500, 600  # Extra height for the score display
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
TEXT_COLOR = (255, 255, 255)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

font = pygame.font.SysFont(None, 32)

# Initialize game state
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
scores = {"X": 0, "O": 0}
player = "X"
game_over = False


def draw_board():
    screen.fill(BG_COLOR)

    # Draw grid lines
    # Horizontal
    pygame.draw.line(
        screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH
    )
    pygame.draw.line(
        screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH
    )
    # Vertical
    pygame.draw.line(
        screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE * 3), LINE_WIDTH
    )
    pygame.draw.line(
        screen,
        LINE_COLOR,
        (2 * SQUARE_SIZE, 0),
        (2 * SQUARE_SIZE, SQUARE_SIZE * 3),
        LINE_WIDTH,
    )

    draw_figures()
    draw_scores()


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "O":
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (
                        int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                        int(row * SQUARE_SIZE + SQUARE_SIZE / 2),
                    ),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )
            elif board[row][col] == "X":
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (
                    col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                )
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (
                    col * SQUARE_SIZE + SPACE,
                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                )
                end_asc = (
                    col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                    row * SQUARE_SIZE + SPACE,
                )
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)


def draw_scores():
    # Clear the score area first by drawing a rectangle over it
    score_area = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
    pygame.draw.rect(screen, BG_COLOR, score_area)

    score_text = f"X: {scores['X']}    O: {scores['O']}  (Press R to Reset)"
    text_surface = font.render(score_text, True, TEXT_COLOR)
    screen.blit(text_surface, (10, HEIGHT - 40))


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] is None


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True


def check_win(player):
    # Check vertical
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def restart():
    global board, game_over, player
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = "X"
    game_over = False
    draw_board()


# Initial draw
draw_board()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            if mouseY < SQUARE_SIZE * 3:  # Clicks only in game area
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        scores[player] += 1
                        game_over = True
                    elif is_board_full():
                        game_over = True
                    else:
                        player = "O" if player == "X" else "X"

                    draw_board()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()

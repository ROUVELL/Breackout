import ctypes

user = ctypes.windll.user32

# screen
WIDTH, HEIGHT = user.GetSystemMetrics(78), user.GetSystemMetrics(79)  # fullscreen
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
CENTER = (HALF_WIDTH, HALF_HEIGHT)
SCREEN = (WIDTH, HEIGHT)

# padle
PADLE_WIDTH = 120
PADLE_HEIGHT = 20
PADLE_SIZE = (PADLE_WIDTH, PADLE_HEIGHT)
PADLE_POS = (WIDTH // 2, HEIGHT - PADLE_HEIGHT - 5)
PADLE_SPEED = 4

# brick
BRICK_WIDTH, BRICK_HEIGHT = 100, 50
BRICK_SIZE = (BRICK_WIDTH, BRICK_HEIGHT)
BRICK_COLORS = ['orange', 'lightgreen', 'lightgrey', 'azure', 'skyblue', 'pink', 'brown', 'yellow']

# ball
BALL_DIAMETR = 16
BALL_START_POS = (WIDTH // 2, HEIGHT // 2)

# level
DX, DY = 5, 5
YOFFSET = 30
MAX_COLS, MAX_ROWS = WIDTH // (BRICK_WIDTH + DX), (HEIGHT // (BRICK_HEIGHT + DY)) - 2
SIDE_OFFSET = (WIDTH % (BRICK_WIDTH + DX)) // 2

# colors
BG = (10, 10, 10)


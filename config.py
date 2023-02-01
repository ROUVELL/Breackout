import ctypes

user = ctypes.windll.user32

# screen
WIDTH, HEIGHT = user.GetSystemMetrics(78), user.GetSystemMetrics(79)  # fullscreen
SCREEN = (WIDTH, HEIGHT)

# brick
BRICK_WIDTH = 100
BRICK_HIGHT = 50
BRICK_SIZE = (BRICK_WIDTH, BRICK_HIGHT)

# level
MAX_COLUMNS = (WIDTH // BRICK_WIDTH)
MAX_ROWS = (HEIGHT // BRICK_HIGHT) - 3

# padle
PADLE_WIDTH = 120
PADLE_HEIGHT = 20
PADLE_SIZE = (PADLE_WIDTH, PADLE_HEIGHT)
PADLE_POS = (WIDTH // 2, HEIGHT - PADLE_HEIGHT - 5)

# ball
BALL_DIAMETR = 16
BALL_START_POS = (WIDTH // 2, 50)

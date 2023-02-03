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

# ball
BALL_DIAMETR = 16
BALL_START_POS = (WIDTH // 2, HEIGHT // 2)

# colors
BG = (10, 10, 10)
BRICK_COLORS = ['orange', 'lightgreen', 'lightgrey', 'azure', 'skyblue', 'pink', 'brown', 'yellow']

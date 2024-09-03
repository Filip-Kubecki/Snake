# Game configuration file
# Contains all values that are intended to be changed

# Snake related values
SNAKE_SEGMENT_NUMBER = 5
SNAKE_START_SPEED = 12  # Smaller number -> faster

# UI related values
# Window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
ENABLE_BORDER = False

# Pause/Game Over screens
DIMMED_BACKGROUND_MAX_ALPHA = 150
DIMMED_BACKGROUND_ALPHA_INCREMENT = 10
# Pause screen
PAUSE_SCREEN_BUTTON_SIZE = 70
PAUSE_SCREEN_IMG_REAL_SIZE = 50
PAUSE_SCREEN_BUTTON_OFFSET = 50
PAUSE_SCREEN_BUTTON_MENU_WIDTH = (
    PAUSE_SCREEN_BUTTON_SIZE*3)+(PAUSE_SCREEN_BUTTON_OFFSET*4)
PAUSE_SCREEN_BUTTON_MENU_HEIGHT = 110
# Game over screen
GAME_OVER_SCREEN_BUTTON_MENU_WIDTH = (
    PAUSE_SCREEN_BUTTON_SIZE)+(PAUSE_SCREEN_BUTTON_OFFSET*2)
GAME_OVER_SCREEN_BUTTON_MENU_HEIGHT = 110


# Game Instance
GAME_INSTANCE_BORDER_COLLISION = False
GAME_INSTANCE_BORDER_WIDTH = 6
GAME_INSTANCE_SCALE = 3
TILE_LEN = 20 * GAME_INSTANCE_SCALE
GAME_INSTANCE_TOP_MARGIN = int(
    WINDOW_HEIGHT / 5) if ENABLE_BORDER else int(WINDOW_HEIGHT/7)

# Calculating Game Instance sizes - based on values above
GAME_INSTANCE_WIDTH = (((((WINDOW_WIDTH // TILE_LEN)) *
                         TILE_LEN) - (WINDOW_WIDTH//20))//TILE_LEN)*TILE_LEN
GAME_INSTANCE_HEIGHT = (((((WINDOW_HEIGHT // TILE_LEN)) *
                        TILE_LEN) - (((GAME_INSTANCE_TOP_MARGIN//TILE_LEN)*TILE_LEN) + (WINDOW_HEIGHT//28)))//TILE_LEN)*TILE_LEN

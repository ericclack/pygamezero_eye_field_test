WIDTH = 1000
HEIGHT = 800
TITLE = "Eye field test"

FIELD = [ [0]*30 for i in range(20) ]

DOT_RADIUS = 15
V_TO_RGV = {
    0: (0,0,0),
    1: (100,100,100),
    2: (200,200,200),
    3: (255, 255, 255)}

CURRENT_X = 0
CURRENT_Y = 0
TARGET = (5, 5) # In dot position (so * RADIUS)

def draw():
    draw_field()
    draw_target()
    draw_dot(CURRENT_X, CURRENT_Y, 3)

def draw_target():
    screen.draw.text('X', [i*DOT_RADIUS for i in TARGET],
        color = "white",
        fontsize = 50)

def draw_dot(x,y,v):
    screen.draw.filled_circle(
        (x*DOT_RADIUS*2,y*DOT_RADIUS*2),
        DOT_RADIUS, V_TO_RGV[v])

def draw_field():
    for y, row in enumerate(FIELD):
        for x, v in enumerate(row):
            draw_dot(x,y,v)

def on_key_up(key):
    global CURRENT_Y, CURRENT_X
    if key == keys.SPACE:
        FIELD[CURRENT_Y][CURRENT_X] = 2
    if key == keys.Q:
        print(FIELD)

    CURRENT_X += 1
    if CURRENT_X >= len(FIELD[0]):
        CURRENT_Y += 1
        CURRENT_X = 0
    if CURRENT_Y >= len(FIELD):
        print("All done")
        print(FIELD)

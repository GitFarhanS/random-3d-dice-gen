from ursina import *
import random

app = Ursina()

dice_texture = load_texture('dice_texture.png')

cube = Entity(model="custom_cube", texture=dice_texture, scale=2)

def roll_dice():
    random_x = random.randint(720, 1440)
    random_y = random.randint(720, 1440)
    
    # Animate random rotation
    cube.animate_rotation_x(random_x, duration=1.0)
    cube.animate_rotation_y(random_y, duration=1.0)
    
    # Delay before snapping
    invoke(animate_rotation_snap, random_x, random_y, delay=1.0)

def animate_rotation_snap(random_x, random_y):
    # Snap rotations to nearest 90 degrees
    random_x_snap = round(random_x / 90.0) * 90.0
    random_y_snap = round(random_y / 90.0) * 90.0

    cube.animate_rotation_x(random_x_snap, duration=1.0)
    cube.animate_rotation_y(random_y_snap, duration=1.0)

def input(key):
    if key == 'space':
        roll_dice()

app.run()

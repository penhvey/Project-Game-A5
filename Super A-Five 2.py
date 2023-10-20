import tkinter as tk
from PIL import Image,ImageTk

window = tk.Tk()
window.geometry("1920x1080")
window.title("Movement")
frame = tk.Frame(window, width=1920, height=1080)
frame.pack()
canvas = tk.Canvas(frame, width=1920, height=1080, bg="white")
canvas.pack()



player = canvas.create_oval(150, 150, 210, 210, fill="gold")


canvas.create_rectangle(0, 630, 400, 810, fill="black", tags="wall")
canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")
canvas.create_rectangle(500, 630, 1536, 810, fill="black", tags="wall")
canvas.create_rectangle(500, 530, 550, 810, fill="black", tags="wall")
canvas.create_rectangle(600, 570, 550, 810, fill="black", tags="wall")
canvas.create_rectangle(650, 595, 550, 810, fill="black", tags="wall")
canvas.create_rectangle(400, 530, 350, 810, fill="black", tags="wall")
canvas.create_rectangle(400, 570, 300, 810, fill="black", tags="wall")
canvas.create_rectangle(400, 600, 250, 810, fill="black", tags="wall")




keyPressed = []
SPEED = 7
TIME = 10
GRAVITY_FORCE=9

def check_movement(dx=0, dy=0):
    ball_coords = canvas.coords(player)

    # Calculate the new coordinates if the ball were to move
    new_x1 = ball_coords[0] + dx
    new_y1 = ball_coords[1] + dy
    new_x2 = ball_coords[2] + dx
    new_y2 = ball_coords[3] + dy

    # Find overlapping objects with the proposed new coordinates
    overlapping_objects = canvas.find_overlapping(new_x1, new_y1, new_x2, new_y2)

    # Check if any wall is in the list of overlapping objects
    for wall_id in canvas.find_withtag("wall"):
        if wall_id in overlapping_objects:
            return False  # Collision detected with a wall, can't move

    return True  # No collision, it's safe to move

def start_move(event):
    if event.keysym not in keyPressed:
        print(event.keysym)
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIME, jump, force-1)

  

def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x = -SPEED
        if "Right" in keyPressed:
            x = SPEED
        if check_movement(x,0):
                canvas.move(player, x, 0)
        if "space" in keyPressed and not check_movement(0,GRAVITY_FORCE):
            jump(30)
        window.after(TIME, move)


def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

def gravity():
    if check_movement(0, GRAVITY_FORCE):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIME, gravity) 

gravity()

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()
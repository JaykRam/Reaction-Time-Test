import tkinter as tk
import time
import random

# Initialize Screen & react_speed
screen = tk.Tk()
react_speed = 0

#SCREENS
def start_react():
    startscreen = screen
    startscreen.title("Start Screen")

    startscreen.geometry("400x300")
    startscreen.configure(bg="sky blue")

    startscreen.bind("<Button-1>", on_blue_click)
    
def red_screen():
    readyscreen = screen
    readyscreen.title("Get Ready Screen")

    readyscreen.geometry("400x300")
    readyscreen.configure(bg="red")

    readyscreen.unbind("<Button-1>")

    # Random time before switch to green
    delay = random.randint(3, 8) * 1000
    screen.after(delay, green_screen)

def green_screen():
    clickscreen = screen
    clickscreen.title("Click! Screen")

    clickscreen.geometry("400x300")
    clickscreen.configure(bg="green")

    # Save time
    global react_speed
    react_speed = time.perf_counter()

    clickscreen.bind("<Button-1>", on_green_click)

def end_react():
    global react_speed
    
    endscreen = screen
    endscreen.title("Start Screen")

    endscreen.geometry("400x300")
    endscreen.configure(bg="sky blue")

    reaction_time = time.perf_counter() - react_speed  

    print("Reaction Time: {:.3f}".format(reaction_time))
    # print("Reaction Time: " + str(reaction_time))

    endscreen.bind("<Button-1>", on_blue_click)

#BUTTON PRESSES
# Start React Game. Go to red screen.
def on_blue_click(event):
    print("Screen clicked")
    red_screen()

# Green Screen
def on_green_click(event):
    print("Screen clicked")
    end_react()

# Debug and Start the game.
start_react()
print("React game started")
screen.mainloop()
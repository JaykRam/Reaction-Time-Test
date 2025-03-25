import tkinter as tk

# def on_blue_click(event):
#     print("Screen clicked")

# Create main window
# mig = tk.Tk()
# mig.title("Start Screen")

# Set window size
# mig.geometry("400x300")

# Set background color
# mig.configure(bg="sky blue")

# Bind mouse click event to the window
# mig.bind("<Button-1>", on_blue_click)

# Run application
# mig.mainloop()

# Close
# startscreen.destroy()



# Initialize Screen
screen = tk.Tk()

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

    #add random time before switch to green





# Start React Game. Go to red screen.
def on_blue_click(event):
    print("Screen clicked")
    red_screen()

# Debug and Start the game.
start_react()
print("React game started")
screen.mainloop()
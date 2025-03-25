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

def start_react():
    startscreen = tk.Tk()
    startscreen.title("Start Screen")

    startscreen.geometry("400x300")
    startscreen.configure(bg="sky blue")

    def on_blue_click(event):
        print("Screen clicked")
        
    
    startscreen.bind("<Button-1>", on_blue_click)

    print("React game started")
    startscreen.mainloop()



start_react()

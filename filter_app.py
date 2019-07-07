# This is a image filter app. By impoorting a image and choosing a filter
# the user can manipulate a image and seve the new one to a file


import tkinter as tk
from tkinter.filedialog import askopenfilename

import GUI_functions as func

# size of the window
WIDTH = 1800
HEIGHT = 1200

# creates main window
root = tk.Tk()

# opens image and converts it to tkinter compatible image
image = func.loadStartingImage()

# create canvas to set the window size
canvas = tk.Canvas(root,  width=WIDTH, height=HEIGHT)
canvas.pack()

# frame to place thing into it
frame = tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)

# label to show which filter is active
filterIndicator = tk.Label(frame, text="Filter", fg="white", bg="black",
    font=("Helvetica", 26))
filterIndicator.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.1)

# label that shows the current image
pic = tk.Label(frame, image=image)
pic.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

# buttons to switch filters
buttonLeft = tk.Button(frame, text="left", command=func.decreaseFilterIndex)
buttonLeft.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.8)

buttonRigth = tk.Button(frame, text="right", command=func.increaseFilterIndex)
buttonRigth.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.8)

# create menuebar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=func.changeImage)
filemenu.add_command(label="Save", command=func.donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=func.donothing)
helpmenu.add_command(label="About...", command=func.donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# keep main window opened
root.mainloop()

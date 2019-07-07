# This is a image filter app. By impoorting a image and choosing a filter
# the user can manipulate a image and seve the new one to a file

from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename

def increaseFilterIndex():
    global filterIndex
    filterIndex += 1
    print(filterIndex)

def decreaseFilterIndex():
    global filterIndex
    if filterIndex > 0:
        filterIndex -= 1
    print(filterIndex)

def loadStartingImage():
    img = Image.open("b39.jpg")
    tkimage = ImageTk.PhotoImage(img)

    return tkimage

def changeImage():
    filename = askopenfilename()
    img = Image.open(filename)
    image1 = ImageTk.PhotoImage(img)
    pic.configure(image=image1)
    pic.image = image1
    print(filename)

def donothing():
    pass

# size of the window
WIDTH = 1800
HEIGHT = 1200

# index to select filter
filterIndex = 0

# creates main window
root = tk.Tk()

# opens image and converts it to tkinter compatible image
image = loadStartingImage()

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
buttonLeft = tk.Button(frame, text="left", command=decreaseFilterIndex)
buttonLeft.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.8)

buttonRigth = tk.Button(frame, text="right", command=increaseFilterIndex)
buttonRigth.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.8)

# create menuebar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=changeImage)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# keep main window opened
root.mainloop()

from PIL import Image, ImageTk

filterIndex = 0

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

from tkinter import *
from tkinter.ttk import *
import pickle
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.gridspec import GridSpec
import glob
import os
from qbstyles import mpl_style

COLORMAP = 'plasma'
SHADING='nearest'
DARK=True


def enableInteractive():
    global plt
    plt.ion()

def disableInteractive():
    global plt
    plt.ioff()

def setTheme(dark=False):
    DARK = dark

    mpl_style(dark=DARK, minor_ticks=False)

mpl_style(dark=DARK, minor_ticks=False)

cdir = "./"

content = os.listdir(cdir)
folderList = list()

for c in content:
    if os.path.isdir(c):
        folderList.append(c)

print(f"Found {len(folderList)} folders in current directory:\n {folderList}")


selection = ""
if len(folderList) == 1:
    selection = folderList[0]
else:
    while(selection not in folderList):
        idx = input("Choose the desired datafolder as index\n")
        selection = folderList[int(idx)]

fileList = glob.glob(f"{cdir + selection}/*.p")
pt = 0

def setFigureFromFile(filePath):
    print(f"Showing {fileList[pt]}")

    data = pickle.load(open(fileList[pt],'rb'))
    setFigureFromData(data=data)


def setFigureFromData(data):
    fig, ax= plt.subplots()
    ax.remove()

    ax = data["plothandle"]

    ax.figure = fig
    fig.axes.append(ax)
    fig.add_axes(ax)
    
    gs = GridSpec(1,1,figure=fig)[0]
    fig.axes[0].set_subplotspec(gs)

    canvas = FigureCanvasTkAgg(fig, main)
    canvas.get_tk_widget().grid(row=0, column=0)


def rightKey(event):
    global pt

    pt = pt + 1 if pt < len(fileList)-1 else pt
    setFigureFromFile(fileList[pt])


def leftKey(event):
    global pt

    pt = pt - 1 if pt > 0 else pt
    setFigureFromFile(fileList[pt])

def resize(event):
    setFigureFromFile(fileList[pt])


def startup():
    
    setFigureFromFile(fileList[pt])

# w2 = Scale(main, from_=0, to=200, orient=HORIZONTAL)
# w2.set(23)
# w2.pack()

main = Tk()
frame = Frame(main)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
# main.bind("<Configure>", resize)


startup()

main.mainloop()

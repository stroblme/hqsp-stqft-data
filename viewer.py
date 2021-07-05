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

print(f"Viewing data inside {selection}")

main = Tk()



        

def setFigureFromFile(filePath):
    print(f"Showing {fileList[pt]}")

    data = pickle.load(open(fileList[pt],'rb'))
    setFigureFromData(data=data)


def setFigureFromData(data):
    figure = data["plothandle"]
    gs = GridSpec(1,1,figure=figure)[0]
    figure.axes[0].set_subplotspec(gs)

    canvas = FigureCanvasTkAgg(figure, main)
    canvas.get_tk_widget().grid(row=0, column=0)


def rightKey(event):
    global pt

    pt = pt + 1 if pt < len(fileList) else pt
    setFigureFromFile(fileList[pt])


def leftKey(event):
    global pt

    pt = pt - 1 if pt > 0 else pt
    setFigureFromFile(fileList[pt])

fileList = glob.glob(f"{cdir + selection}/*.p")
pt = 0
setFigureFromFile(fileList[pt])

frame = Frame(main, width=1600, height=900)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.mainloop()

from tkinter import *
from tkinter.ttk import *
import pickle
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.gridspec import GridSpec

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

fileList = os.listdir(cdir + selection)
pt = 0
prev_pt = 0

if fileList[pt][-2:] != ".p":
    if prev_pt == pt:
        pt += 1
        prev_pt = pt
        
print(f"Showing {fileList[pt]}")
data = pickle.load(open(cdir + selection + "/" + fileList[pt],'rb'))


figure = data["plothandle"]
gs = GridSpec(1,1,figure=figure)[0]
figure.axes[0].set_subplotspec(gs)

canvas = FigureCanvasTkAgg(figure, main)
canvas.get_tk_widget().grid(row=0, column=0)

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

frame = Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.mainloop()

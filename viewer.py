from tkinter import *
from tkinter.ttk import *
import pickle
import matplotlib
from matplotlib.pyplot import plot
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import os

cdir = "./"

content = os.listdir(cdir)
folderList = list()

for c in content:
    if os.path.isdir(c):
        folderList.append(c)

print(f"Found {len(folderList)} folders in current directory:\n {folderList}")


selection = ""
while(selection not in folderList):
    idx = input("Choose the desired datafolder as index\n")
    selection = folderList[int(idx)]

print(f"Viewing data inside {selection}")

root = Tk()

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
figure.subplot()
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()

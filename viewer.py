from tkinter import *
from tkinter.ttk import *
import pickle
from git import exc
import matplotlib
from matplotlib.backend_bases import MouseEvent
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
DARK=False

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



# def setFigureFromFile(filePath):
#     print(f"Showing {fileList[pt]}")

#     data = pickle.load(open(fileList[pt],'rb'))
#     setFigureFromData(data=data)


# def setFigureFromData(data):
#     fig, ax= plt.subplots()
#     ax.remove()

#     ax = data["plotdata"]

#     ax.figure = fig
#     fig.axes.append(ax)
#     fig.add_axes(ax)
    
#     gs = GridSpec(1,1,figure=fig)[0]
#     fig.axes[0].set_subplotspec(gs)

#     canvas = FigureCanvasTkAgg(fig, main)
#     canvas.get_tk_widget().grid(row=0, column=0)

clickEventHandled = True
def on_click(event):
    """Enlarge or restore the selected axis."""
    global clickEventHandled

    if not clickEventHandled:
        return

    ax = event.inaxes
    if ax is not None:
        # Occurs when a region not in an axis is clicked...
        if int(event.button) is 1:
            # On left click, zoom the selected axes
            ax._orig_position = ax.get_position()
            ax.set_position([0.1, 0.1, 0.85, 0.85])
            for axis in event.canvas.figure.axes:
                # Hide all the other axes...
                if axis is not ax:
                    axis.set_visible(False)
            event.canvas.draw()

        elif int(event.button) is 3:
            # On right click, restore the axes
            try:
                ax.set_position(ax._orig_position)
                for axis in event.canvas.figure.axes:
                    axis.set_visible(True)
            except AttributeError:
                # If we haven't zoomed, ignore...
                pass

            event.canvas.draw()

    clickEventHandled = True

def matplotlibtest():

    fig, ax= plt.subplots(frameon=False)
    ax.remove()

    
    for filePath in fileList:
        try:
            data = pickle.load(open(filePath,'rb'))
        except Exception as e:
            print(f"Error loading {filePath}: {e}")
            continue
        
        if "plotdata" not in data.keys():
            continue

        cax = data["plotdata"]
        cax.figure = fig
        fig.axes.append(cax)
        fig.add_axes(cax)
    
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.tight_layout()
    plt.show()

# matplotlibtest()

def show(yData, x1Data, title, xlabel, ylabel, x2Data=None, subplot=None):
    # fighandle = plt.figure()

    if subplot is not None:
        plt.subplot(*subplot,frameon=False)
        plt.subplots_adjust(wspace=0.58)
    else:
        plt.figure(figsize = (10, 6))

    if x2Data is None:
        plt.stem(x1Data, yData)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    else:
        plt.pcolormesh(x2Data, x1Data, yData, cmap=COLORMAP, shading=SHADING)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
            
    plt.title(title)

    plt.tight_layout()

def createPlots():
    for filePath in fileList:
        try:
            data = pickle.load(open(filePath,'rb'))
        except Exception as e:
            print(f"Error loading {filePath}: {e}")
            continue
        
        if "plotdata" not in data.keys():
            continue

        yData = data["plotdata"]["yData"]
        x1Data = data["plotdata"]["x1Data"]
        title = data["plotdata"]["title"]
        xlabel = data["plotdata"]["xlabel"]
        ylabel = data["plotdata"]["ylabel"]
        x2Data = data["plotdata"]["x2Data"]
        subplot = data["plotdata"]["subplot"]

        show(yData,x1Data,title,xlabel,ylabel,x2Data,subplot)

    fig = plt.gcf()
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

createPlots()

# exit

# def rightKey(event):
#     global pt

#     tpt = pt + 1 if pt < len(fileList)-1 else pt
#     setFigureFromFile(fileList[pt])
#     pt = tpt


# def leftKey(event):
#     global pt

#     tpt = pt - 1 if pt > 0 else pt
#     setFigureFromFile(fileList[pt])
#     pt = tpt


# def resize(event):
#     setFigureFromFile(fileList[pt])


# def startup():
    
#     setFigureFromFile(fileList[pt])

# # w2 = Scale(main, from_=0, to=200, orient=HORIZONTAL)
# # w2.set(23)
# # w2.pack()

# main = Tk()
# frame = Frame(main)
# main.bind('<Left>', leftKey)
# main.bind('<Right>', rightKey)
# # main.bind("<Configure>", resize)


# startup()

# main.mainloop()

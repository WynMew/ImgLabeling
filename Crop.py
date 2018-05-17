import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.widgets as widgets

def onselect(eclick, erelease):
    if eclick.ydata>erelease.ydata:
        eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
    if eclick.xdata>erelease.xdata:
        eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
    print(' startposition : (%f, %f)' % (eclick.xdata, eclick.ydata))
    print(' startposition : (%f, %f)' % (eclick.xdata, eclick.ydata), file=open("output.txt", "a"))
    print(' endposition   : (%f, %f)' % (erelease.xdata, erelease.ydata))
    print(' endposition   : (%f, %f)' % (erelease.xdata, erelease.ydata),file=open("output.txt", "a"))
    print(' used button   : ', eclick.button)
    #ax.set_ylim(erelease.ydata,eclick.ydata)
    #ax.set_xlim(eclick.xdata,erelease.xdata)
    #fig.canvas.draw()

directory = '/home/wynmew/Documents/frame'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print('++++++++++', file=open("output.txt", "a"))
        print(os.path.join(directory, filename))
        print(os.path.join(directory, filename), file=open("output.txt", "a"))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #filename = "test.png"
        im = Image.open(filename)
        arr = np.asarray(im)
        plt_image = plt.imshow(arr)
        rs = widgets.RectangleSelector(
            ax, onselect, drawtype='box',
            rectprops=dict(facecolor='red', edgecolor='black', alpha=0.5, fill=True))
        plt.show()
        continue
    else:
        continue

'''

'''
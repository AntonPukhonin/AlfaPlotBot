# -*- coding: utf-8 -*-
import os
import sys
import alphaComposite

path = os.getcwd()
sys.path.insert(0, path + "/rawdata")

import numpy as np
import matplotlib.pyplot as plt

import datetime
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import mockChart
from datetime import datetime, date, timedelta
from Tkinter import Tk, Canvas
from PIL import ImageTk, Image, ImageDraw

def createChart(categories, average, user):
    createPlot(categories, average, user)
    size = (800,600)

    image = getBgImage(categories, average, user)

    overlay = Image.open("filename.png")
    overlay = overlay.convert("RGBA")
    datas = overlay.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    overlay.putdata(newData)

    background = Image.new("RGBA", size, color=(255,255,255, 255))
    background.paste(image, (193, 60), image)xw
    background.paste(overlay, (0, 0), overlay)
    background.save("filename.png","PNG")
    print ("success")


def createPlot(categories, average, user):
    groups = len(categories)

    fig, ax = plt.subplots()

    index = np.arange(groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, average, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label='Average for the region')

    rects2 = plt.bar(index + bar_width, user, bar_width,
                     alpha=opacity,
                     color='r',
                     error_kw=error_config,
                     label='Your expenses')

    plt.xlabel('Expenses')
    plt.ylabel('Category')

    plt.xticks(index + bar_width, categories)
    plt.legend()

    fig.autofmt_xdate()

    fig.savefig("filename", transparent=True)
    plt.close(fig)

def getBgImage(categories, average, user):
    return Image.open("1.png")

categories, expancies = mockChart.get_chart(1, 2)
createChart(categories, expancies, expancies)

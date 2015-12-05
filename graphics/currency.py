#!/usr/bin/env python
"""
Show how to make date plots in matplotlib using date tick locators and
formatters.  See major_minor_demo1.py for more information on
controlling major and minor ticks

All matplotlib date plotting is done by converting date instances into
days since the 0001-01-01 UTC.  The conversion, tick locating and
formatting is done behind the scenes so this is most transparent to
you.  The dates module provides several converter functions date2num
and num2date

"""
import os
import sys

path = os.getcwd()
sys.path.insert(0, path + "/rawdata")

import datetime
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from mockAsset import Asset
from datetime import datetime, date, timedelta
from Tkinter import Tk, Canvas
from PIL import ImageTk, Image, ImageDraw

def createChartWeek(title, days, ticks):
    currentDay = days[len(days) - 1];
    rightDays = []
    rightTicks = []

    i = 0
    for day in days:
        if currentDay.toordinal() - 7 < day.toordinal():
            rightDays.append(day)
            rightTicks.append(ticks[i])
        i = i + 1
    print len(days)
    print len(rightDays)

    createChart(title, rightDays, rightTicks, False)

def checkIncreasingFunction(ticks):
    first = ticks[0]
    last = ticks[len(ticks) - 1]
    return last > first

def createChart2(currencyTitle, days, ticks):
    createChart(currencyTitle, days, ticks, False)

def createChart(currencyTitle, days, ticks, isMagic):
    size = (800, 600)
    fig, ax = plt.subplots()
    plt.plot(days, ticks)
    plt.title(currencyTitle)
    fig.autofmt_xdate()

    fig.savefig("filename", transparent=True)
    plt.close(fig)

    if isMagic:
        background = Image.open("currencyNegative.png")
    else:
        background = Image.open("currencyPositive.png")

    background = background.resize(size, Image.ANTIALIAS)
    overlay = Image.open("filename.png")
    mask = Image.new("RGBA", size, color=(255,255,255,150))

    background.paste(mask, (0, 0), mask)
    background.paste(overlay, (0, 0), overlay)
    background.save("filename.png","PNG")
    print ("success")

ass = Asset(1)
dates, rate = ass.get_timeseries("AdjClose")
createChartWeek("test", dates, rate)

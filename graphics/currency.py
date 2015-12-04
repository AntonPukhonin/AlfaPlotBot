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

def drawGraph(days, values, filename):
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    yearsFmt = mdates.DateFormatter('%Y')

    # load a numpy record array from yahoo csv data with fields date,
    # open, close, volume, adj_close from the mpl-data/example directory.
    # The record array stores python datetime.date as an object array in
    # the date column
    datafile = cbook.get_sample_data('goog.npy')
    try:
        # Python3 cannot load python2 .npy files with datetime(object) arrays
        # unless the encoding is set to bytes. Hovever this option was
        # not added until numpy 1.10 so this example will only work with
        # python 2 or with numpy 1.10 and later.
        r = np.load(datafile, encoding='bytes').view(np.recarray)
    except TypeError:
        r = np.load(datafile).view(np.recarray)

    fig, ax = plt.subplots()
    ax.plot(r.date, r.adj_close)


    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)

    datemin = datetime.date(r.date.min().year, 1, 1)
    datemax = datetime.date(r.date.max().year + 1, 1, 1)
    ax.set_xlim(datemin, datemax)


    # format the coords message box
    def price(x):
        return '$%1.2f' % x


    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.format_ydata = price
    ax.grid(True)

    # rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them
    fig.autofmt_xdate()

    print ("success")

    fig.savefig(filename)
    plt.close(fig)
    return filename

def example2(days, ticks):
    currenctDay = days[0];
    rightDays = days

    for day in days:
        print day

    example("exmaple", rightDays, ticks)

def example(currencyTitle, days, ticks):
    fig, ax = plt.subplots()
    plt.plot(days, ticks)
    plt.xlabel(currencyTitle)

    # datafile = cbook.get_sample_data(path + '/currencyPositive.jpg')
    # img = plt.imread(datafile)
    # plt.scatter(x,y,zorder=1)
    # plt.imshow(img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])

    fig.autofmt_xdate()
    fig.savefig("filename")
    plt.close(fig)
    print ("success")

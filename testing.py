#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:54:37 2020
Updated on Jan 04 2021
@author: Sid, Mayur
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy import stats
import matplotlib.ticker as plticker
import base64
import io
import datetime
import yfinance as yf
from yahoo_fin import stock_info as si

spy = yf.Ticker("SPY")
global spyPrice
spyPrice = si.get_live_price("spy")

# [DEPRECIATED] Get the current date and YTD
# Added function to adjust the number of
# years in the past if needed
# I think this also accounts for leap years
def subtractYears(dt, years):
    try:
        dt = dt.replace(year=dt.year - years)
    except ValueError:
        dt = dt.replace(year=dt.year - years, day=dt.day - 1)
    return dt


delta = 120
todayDate = datetime.datetime.now()
pastDate = todayDate - datetime.timedelta(delta)
todayStr = todayDate.strftime("%Y-%m-%d")
pastStr = pastDate.strftime("%Y-%m-%d")

histData = yf.download("SPY", start=pastStr, end=todayStr)
histData.reset_index(level=0, inplace=True)

copySPY = histData.copy()
copySPY['daily_return'] = (histData['Adj Close'] / histData['Adj Close'].shift(1)) - 1
copySPY['daily_return'] = copySPY['daily_return'] * 100
copySPY.dropna(inplace=True)
#copySPY['norm_price'] = copySPY['norm_price']*spyPrice

daily_return = list(copySPY['daily_return'])
norm_price = []

for i in range(len(daily_return)):
    if daily_return[i] > 0 or daily_return[i] < 0:
        norm_price.append(daily_return[i])
    else:
        norm_price.append(0)

norm_price = [i * spyPrice for i in norm_price]

copySPY['norm_price'] = norm_price

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

plt.figure(figsize = (10, 5))
graph = plt.bar(copySPY['Date'], copySPY['daily_return'], color=(copySPY['daily_return'] > 0).map({True: 'g',
                                                    False: 'r'}))
addlabels(copySPY['Date'], norm_price)

# graph = copySPY['daily_return'].bar(title='test daily 31 Days')
plt.title('Daily Price Change $SPY, ' + str(delta) + " Days, " + pastDate.strftime("%b %Y") +
          " - " + todayDate.strftime("%b %Y"))
plt.ylabel('Percent (Relative) Price Change')
plt.style.use('seaborn')


plt.show()

# Returns the day as an integer, given a date string
# 1M, 2T, 3W, 4R, 5F, 6S, 7S
def getDay(date):
    day = datetime.datetime.strptime(str(date), "%Y-%m-%d %X").isoweekday()
    return day


def spreader():
    # print("1M, 2T, 3W, 4R, 5F, 6S, 7S")
    # print("Enter open day 1: ")
    # day1 = int(input())
    # day1 = 1
    day1 = datetime.datetime.today().isoweekday()
    # print("Enter close day 2: ")
    # day2 = int(input())
    day2 = 0
    if day1 <= 2:
        day2 = 3
    else:
        day2 = 5
    binOpen = int(delta / 7)
    binClose = int(delta / 7)
    opens = np.zeros((binOpen, 1))
    closes = np.zeros((binClose, 1))
    counter = 0

    for i in range(len(histData)):
        if getDay(histData.iloc[i, 0]) == day1:
            opens[counter] = float(histData["Open"][i])
            counter = counter + 1
    counter = 0
    for i in histData.index:
        if getDay(histData.iloc[i, 0]) == day2:
            closes[counter] = float(histData["Adj Close"][i])
            counter = counter + 1

    return opens, closes


def relativeChange(initial=[], final=[]):
    # np.seterr(divide='ignore', invalid='ignore')
    # declare empty array to hold calculated relative changes
    change = np.zeros((len(final), 1))
    # iterate thru first array (both should have same size)
    for i in range(len(initial)):
        # ignore days when no trades happened
        if initial[i] == 0.0 or final[i] == 0.0:
            continue
            # relative change formula
        else:
            change[i] = (final[i] - initial[i]) / initial[i] * 100
    cleanChange = change[(np.isnan(change) == False) & (np.isinf(change) == False)]
    return cleanChange * 1


def plotPDF(arr):
    # TODO: graph histogram vs time, plot every single point, overlay VIX
    # 10-20 MA for short term analysis
    # output: new histo, KDE graphs, VIX, and 5-10 or 10-20 MA
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # plot histogram
    n, bins, patches = plt.hist(arr, bins=52, density=True)
    # color code histogram
    fracs = n / arr.max()  # normalize color code by height (likelihood)
    norm = colors.Normalize(fracs.min(), fracs.max())  # norm fracts [0,1]
    # loop thru each bin and set colors (using viridis map)
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    # calculate kernel density estimator (with 2 separate techniques)
    kde1 = stats.gaussian_kde(arr)
    kde2 = stats.gaussian_kde(arr, bw_method='silverman')
    # plot KDE
    arr_eval = np.linspace(-10, 10, num=200)
    scotts = ax.plot(arr_eval, kde1(arr_eval), 'k-', label="Scott's Rule")
    ax.plot(arr_eval, kde2(arr_eval), 'r-', label="Silverman's Rule")

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    global toText
    toText = str(base64.b64encode(buf.read()))
    print(toText)

    # gather x and y values into list
    xVals = scotts[0].get_xdata()
    yVals = scotts[0].get_ydata()

    # plt.plot(yVals, xVals)
    # in order to find y values given x, first split array
    # of y-values in half (even split), then to find closest approximation
    # to .05, subtract .05 from the array, and collect the absolute value
    # of the smallest item, returns index of y value, which can be used to
    # extract the corresponding x value
    # print(xVals)
    # print(yVals)
    botY, topY = np.split(yVals, 2)
    # print(botY, topY)

    # idy = np.where(yVals== 0.05)
    idyNeg = (np.abs(botY - .05)).argmin()
    print(idyNeg)
    idyPos = (np.abs(topY - .05)).argmin()
    idyPos = (len(topY) - idyPos) * -1
    print(idyPos)

    # now returns proper x value associated ith y,
    print(xVals[idyNeg])
    print(xVals[idyPos])

    global callThresh
    callThresh = xVals[idyPos]
    global putThresh
    putThresh = xVals[idyNeg]

    # set tick frequency
    loc = plticker.MultipleLocator(base=2.0)
    ax.xaxis.set_major_locator(loc)
    # x, y, and plot titles
    plt.xlabel('Percent (Relative) Price Change')
    plt.ylabel('Probability')
    plt.title('Relative Price Change $SPY, ' + pastDate.strftime("%b %Y") +
              " - " + todayDate.strftime("%b %Y"))
    # display plot
    plt.interactive(False)
    plt.show()
    plt.close()


def brr():
    # choice = getInterval()
    # print(histData)
    openInput, closeInput = spreader()
    print()
    relChange = relativeChange(openInput, closeInput)

    plotPDF(relChange)

    print("Enter +5% threshold (decimal): ")
    plusFive = float(input())
    print("Enter -5% threshold (decimal): ")
    minusFive = float(input())

    spyPrice = si.get_live_price("spy")
    # spyPrice = 378.72

    print()
    fiveBelow = spyPrice - minusFive * spyPrice
    fiveAbove = spyPrice + plusFive * spyPrice

    print("5% PUT threshold: ", round(fiveBelow, 2))
    print("Current price of SPY:", round(spyPrice, 2))
    print("5% CALL threshold: ", round(fiveAbove, 2))


def testMain():
    openInput, closeInput = spreader()
    print()
    relChange = relativeChange(openInput, closeInput)
    # print(relChange)
    plotPDF(relChange)
    # print("Enter +5% threshold (decimal): ")
    # plusFive = float(input())
    plusFive = .02
    # print("Enter -5% threshold (decimal): ")
    # minusFive = float(input())
    minusFive = .03


    # spyPrice = 378.72

    print()
    fiveBelow = spyPrice + putThresh / 100 * spyPrice
    fiveAbove = spyPrice + callThresh / 100 * spyPrice

    '''<html>
    <h1>$SPY [date]</h1>
    <p>5% PUT threshold: 403.01</p>
    <p>Current SPY price: 418.79</p>
    <p>5% CALL threshold: 434.99</p> 
      <img src="data:image/jpeg;base64,XXX"/>

    </html>'''

    message = '''<html>
        <head>
            <style>
                body {
                     font-family: verdana;
                     margin: 10px;
                }
                h1   {color: blue;}
                p    {color: black;}
                marquee    {color: black;}
            </style>
        </head>
      <body>
        <marquee width = "10%%">SPDR S&P 500 ETF Trust</marquee>
        <p>%s</p>
        <p>Delta: %d</p>
        <p>5%% PUT threshold: %s</p>
        <p>Current SPY price: %s</p>
        <p>5%% CALL threshold: %s</p> 
        <img src="data:image/png;base64,%s"
          width="600" />
      </body>
    </html>'''

    f = open('home.html', 'w')
    stamp = datetime.datetime.now()
    print(stamp)
    f.write(message % (
    stamp, delta, str(round(fiveBelow, 2)), str(round(spyPrice, 2)), str(round(fiveAbove, 2)), toText[2:-1]))
    f.close()

    print("5% PUT threshold: ", round(fiveBelow, 2))
    print("Current price of SPY: ", round(spyPrice, 2))
    print("5% CALL threshold: ", round(fiveAbove, 2))


testMain()

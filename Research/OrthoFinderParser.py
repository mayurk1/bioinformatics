# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:43:45 2019

@author: Mayur Khanna
"""

#! /usr/bin/env python

import csv
import pandas as pd

global aboveCounter

aboveCounter = 0
#dont need for this program
def getBelow(row):
    count = 0
    r = list(row)
    for cell in r[2:19]:
        if count >= 2:
            return True
        if cell > 0:
            count += 1
    return False            

def getAbove1(row):
    global aboveCounter
    r = list(row)
    for cell in r[46:48]:
        if cell > 0:
            aboveCounter += 1
            
def getAbove2(row):
    global aboveCounter
    r = list(row)
    for cell in r[51:53]:
        if cell > 0:
            aboveCounter += 1 
            
def getAboveSingles(row):
    global aboveCounter
    r = list(row)
    if r[3] > 0:
        aboveCounter += 1 
    if r[50] > 0:
        aboveCounter += 1         
    if r[55] > 0:
        aboveCounter += 1
    print r[3]    
    if r[63] > 0:
        aboveCounter += 1
    if r[65] > 0:
        aboveCounter += 1
         
def getShark(row):
    count = 0
    r = list(row)
    for cell in r[57:60]:
        if cell > 0:
            count += 1
        if count >= 1:
            return True            
    return False

def getFish(row):
    count = 0
    r = list(row)
    print r
    for cell in r[11:45]:
        if cell == 0:
            count += 1
    if count >= 34:
            return True
    return False             


def single_true(iterable):
    i = iter(iterable)
    return any(i) and not any(i)   

#Current issue is that MAEL is not showing up as a successful hit!!! 3/28/19
def main(): 
    global aboveCounter
    query = pd.read_csv("Orthogroups.GeneCount.csv", sep = "\t")
    #query = pd.read_csv("GeneGroupsTest.csv", sep = "\t", index_col = False)
    #hitsList = []
    names = []
    
#    for row in query.itertuples():

    for row in query.itertuples():
        getAbove1(row)
        getAbove2(row)
        getAboveSingles(row)
        if getFish(row) and getShark(row) and aboveCounter >= 5:  
            names.append(row)
        aboveCounter = 0    

    with open('returned.csv', 'w+') as f:
        writer = csv.writer(f)
        for val in names:
            writer.writerow([val])                           

main()            





















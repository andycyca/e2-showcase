#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:16:55 2021

@author: andycyca
"""

import re

filename = 'e2stats.csv'

# There will be two rounds of preprocessing because regexes to do it in
# one step become too unwieldy
prep1 = filename[:-4] + '_preprocessing' + filename[-4:]
prep2 = filename[:-4] + '_final' + filename[-4:]

# Functions for converting special cases
months = {
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12}

def return_chings(line):
    if line == '  ':
        result = r'0'
    else:
        result = str(re.sub(r'^\s*(\d+).+$', r'\1', line))
    return result

def return_hidden(line):
    if line:
        return 'True'
    else:
        return 'False'

# First preprocessing round, reorders line per line to a more
# readable format.
preprocess1 = r'^(\d+C.+|  )\t(.+?) \((.+?)\) \t(.+?)\t\+(\d+?)\/\-(\d+?) \t(H |)\t(\w{3}) (\d\d) (\d{4}) at (\d\d):(\d\d).?$'

# yyyy; mm; dd; hh; mm; title; nodetype; up; down; rep; chings; hidden
out1 = r'\10\t\8\t\9\t\11\t\12\t\2\t\3\t\5\t\6\t\4\t\1\t\7'
outheader = 'year\tmonth\tday\thour\tminute\ttitle\tnodetype\tupvotes\tdownvotes\trep\tchings\thidden\n'

# Preprocess month, 0-chinged writeups and hidden/public flag
preprocess2 = r'^(.+?)\t(.+?)(\t.+)$'
preprocess3 = r'^((?:.+?\t){10})(.+?)(\t.*)$'
preprocess4 = r'^(.+)\t(H |)$'

with open(filename, 'r') as f, open(prep1, 'w') as outfile:
    lines = f.readlines()
    for l in lines:
        result = re.sub(preprocess1, out1, l)
        outfile.write(result)

# Second preprocessing round, corrects the number of chings and
# changes the public/hidden status to True/False, respectively

with open(prep1, 'r') as f, open(prep2, 'w') as outfile:
    lines = f.readlines()
    outfile.write(outheader)
    for l in lines:
        # Get the month string and return it as number
        month = str(months[re.search(preprocess2, l).group(2)])
        mid1 = re.sub(preprocess2, r'\g<1>'+r'\t'+month+r'\g<3>', l)
        # Get the string for chings or empty string and return it as number
        chingstr = str(re.search(preprocess3, mid1).group(2))
        chings = return_chings(chingstr)
        mid2 = re.sub(preprocess3, r'\g<1>'+chings+r'\g<3>', mid1)
        # Get the "H" or empty string and turn it into True/False
        hiddenstr = str(re.search(preprocess4, mid2).group(2))
        hidden = return_hidden(hiddenstr)
        mid3 = re.sub(preprocess3, r'\g<1>'+r'\g<2>'+r'\t'+str(hidden), mid2)
        outfile.write(mid3)

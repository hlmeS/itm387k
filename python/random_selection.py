#! /usr/bin/env python2

"""

Title: Random student selection
Author: Holm Smidt
Version: 0.9
Date: 09-19-2017

Overview:
 ... some text here

Next steps:
 ... integrate with json storage

"""
import numpy as np

def csv_string_import(filepath):
    output = np.loadtxt(filepath, delimiter=',', dtype=np.str)

    return output

def random_selection(listInput, n ):
    #np.random.seed(1)
    return np.random.choice(listInput, n, replace=False)

def get_input():
    filepath = raw_input("Enter input filepath: ")
    size = raw_input("How many would you like to select: ")
    return (filepath, int(size))

def answer():
    (filepath, size) = get_input()
    selected = random_selection(csv_string_import(filepath), size)
    print 'Selection: ', selected

answer()

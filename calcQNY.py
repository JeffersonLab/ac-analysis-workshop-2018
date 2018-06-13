#!/usr/bin/python

# Import various modules
import os, sys, time, glob, string, pickle
import numpy as np
import matplotlib.pyplot as plt
import ROOT as r
from matplotlib import rc

# Open data dictionary produced via makeDict.py
dd = pickle.load(open('dataDict.pkl', 'rb'))

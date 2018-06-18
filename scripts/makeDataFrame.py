#!/usr/bin/python

# Import various modules
import string, glob, pickle
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ROOT as R
import pandas as pd
from matplotlib import rc

# Report file dictionary
rfd = { 'rn'       : [],  # run number
        'pcent'    : [],  # central momentum
        'q4a'      : [],  # bcm4a charge (mC, cut > 5 uA)
        'clt'      : [],  # computer live time
        'elt'      : [],  # electronic live time
        'etr_eff'  : [],  # electron tracking efficiency
        'scin_eff' : [] } # 3/4 trigger efficiency

# Populate list of report files from 21 degrees
rf = glob.glob('../all-reports/replay_shms_production_*_-1.report')
# Sort the lists for consistency
rf.sort()
# Store values of interest in lists
for index, run in enumerate(rf):
   with open(rf[index]) as fobj:
        for line in fobj:
            data = line.split(':')
            # Kinematic configurations
            if ('Run Num'  in data[0]) : rfd['rn'].append(data[1].strip())
            if ('Momentum' in data[0]) : rfd['pcent'].append(data[1].strip())
            # Charge and current
            if ('BCM4a Beam Cut Charge' in data[0]) : rfd['q4a'].append(filter(lambda x: x in string.digits + '.', data[1]))
            # Live times (must be multiplied by 0.01 -> done later)
            if ('Pre-Scaled Ps2 SHMS Computer Live Time' in data[0])   : rfd['clt'].append(data[1][:8].strip())
            if ('OG 6 GeV Electronic Live Time (100, 150)' in data[0]) : rfd['elt'].append(data[1][:8].strip())
            # Tracking efficiencies
            if ('E SING FID TRACK EFFIC' in data[0]) : rfd['etr_eff'].append(data[1][:8].strip())
            # Trigger efficiency
            if ('3_of_4 EFF' in data[0]) : rfd['scin_eff'].append(data[1].strip())

# Create pandas data frame from report file dictionary
# By default the keys of the dict become the DataFrame columns
pdf = pd.DataFrame.from_dict(rfd)
# Convert object data type to float
pdf = pdf.astype(float)

# Plot variables in data frame


# Create DataFrame using dictionary keys as rows
# pdfRows = pd.DataFrame.from_dict(rfd, orient = 'index')

# Create DataFrame while customizing the column names
# pdfCustom = pd.DataFrame.from_dict(rfd, orient = 'index', columns = ['compLT', 'elecLT', 'trEff', 'P', 'charge', 'runNum', 'trigEff'])

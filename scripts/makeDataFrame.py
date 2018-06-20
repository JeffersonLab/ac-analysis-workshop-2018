#!/usr/bin/python

# Import various modules
import string, glob, pickle
import pandas as pd

# Report file dictionary
rfd = { 'rn'           : [],  # run number
        'pcent'        : [],  # central momentum
        'i4a'          : [],  # bcm4a current (uA, cut > 5 uA)
        'i4b'          : [],  # bcm4b current (uA, cut > 5 uA)
        'clt'          : [],  # computer live time
        'pt2'          : [],  # EL-REAL (pTRIG2) rate
        'tr_eff'       : [],  # tracking efficiency
        'etr_eff'      : [],  # electron tracking efficiency
        'htr_eff'      : [],  # hadron tracking efficiency
        'scin_eff'     : [] } # 3/4 trigger efficiency
        
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
            if ('BCM4a Beam Cut Current' in data[0]) : rfd['i4a'].append(filter(lambda x: x in string.digits + '.', data[1]))
            if ('BCM4b Beam Cut Current' in data[0]) : rfd['i4b'].append(filter(lambda x: x in string.digits + '.', data[1]))
            # Live times (must be multiplied by 0.01 -> done later)
            if ('Pre-Scaled Ps2 SHMS Computer Live Time' in data[0])   : rfd['clt'].append(data[1][:8].strip())
            # Tracking efficiencies
            if ('SING FID TRACK EFFIC' in data[0]) and (data[0].count(' ') == 14) : rfd['tr_eff'].append(data[1][:8].strip())
            if ('E SING FID TRACK EFFIC' in data[0])      : rfd['etr_eff'].append(data[1][:8].strip())
            if ('HADRON SING FID TRACK EFFIC' in data[0]) : rfd['htr_eff'].append(data[1][:8].strip())
            # Trigger efficiency
            if ('3_of_4 EFF' in data[0]) : rfd['scin_eff'].append(data[1].strip())
            # EL-REAL trigger rate
            if ('pTRIG2' in data[0]) : 
               pt2b = data[1][data[1].find('[')+1:data[1].find(']')]
               rfd['pt2'].append(filter(lambda x: x in string.digits + '.', pt2b))
            
# Create pandas data frame from report file dictionary
# By default the keys of the dict become the DataFrame columns
df = pd.DataFrame.from_dict(rfd)
# Convert object data type to float
df = df.astype(float)

# Save the dictionary into a pickle file
pickle.dump(df, open('../dframes/dataFrame.pkl', 'wb'))

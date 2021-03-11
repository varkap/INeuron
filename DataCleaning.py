import numpy as np
import pandas as pd
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

# Problem 1
df['FlightNumber'] = range(10045, 10086, 10)

# Problem 2
df2 = df
frm = []
to = []
for f in df2['From_To']:
    frm.append(f.split('_')[0])
    to.append(f.split('_')[1])
df2['From'] = frm
df2['To'] = to

# Problem 3
capped = []
for f in df2['From']:
    capped.append(f.capitalize())
df2['From'] = capped
capped = []
for f in df2['To']:
    capped.append(f.capitalize())
df2['To'] = capped

# Problem 4
del df['From_To']
df = df2

# Problem 5
first = []
second = []
third = []
for r in df['RecentDelays']:
    try:
        first.append(r[0])
    except:
        first.append(np.NaN)
    try:
        second.append(r[1])
    except:
        second.append(np.NaN)
    try:
        third.append(r[2])
    except:
        third.append(np.NaN)
df['delay_1'] = first
df['delay_2'] = second
df['delay_3'] = third

import pandas as pd
import numpy
import numpy as np

data = pd.read_csv("./csvs/3195035949.csv")
data = data.drop(['Unnamed: 0'], axis=1)

from dateutil.parser import parse
def to_timestamp(date):
    try:
        return parse(date, fuzzy=True).timestamp()
    except:
        return date

# remove nan timestamps
data['timestamp'] = data['timestamp'].apply(to_timestamp)
data = data[~numpy.isnan(data['timestamp'])]

def to_running_economy(hr, speed):
    return hr/speed

data["RE"] = data["speed"] / data["heart_rate"]
data = data[~numpy.isnan(data['RE'])]
# remove inf
data = data[numpy.isfinite(data['RE'])]

# great RE is looking normal and like a grate candidate for analysis!
import pylab as pl
from pandas import *
def plot_hist(column_name,title,x_axis_title,y_axis_title):
    ax = data.hist(column=column_name)
    ax = ax[0]
    for x in ax:
    
        # Despine
        x.spines['right'].set_visible(False)
        x.spines['top'].set_visible(False)
        x.spines['left'].set_visible(False)
    
        # Switch off ticks
        x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    
        # Draw horizontal axis lines
        vals = x.get_yticks()
        for tick in vals:
            x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
    
        # Remove title
        x.set_title(title)
    
        # Set x-axis label
        x.set_xlabel(x_axis_title, labelpad=20, weight='bold', size=12)
    
        # Set y-axis label
        x.set_ylabel(y_axis_title, labelpad=20, weight='bold', size=12)
    
        # Format y-axis label
        x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))


plot_hist("cadence","Histogram of Cadence","Cadence","Count")
plot_hist("distance","Histogram of Distance","Distance Run (kilometers)","Count")









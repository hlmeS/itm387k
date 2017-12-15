#! /usr/bin/env python2

"""
Title:
Author:
Date:

Description:


"""

"""
Library Import:

Here we will import some libraries
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import datetime
import sqlUtils             # make sure that sqlUtil.py and config.ini are in the same working directory


"""
Data Retrieval
The first step is to get the data. In this case, the query has been given to you.
In this query, we're looking at temperatures, power, and energy in the month of November.

The query function from the class that I provided you with is currently very static in that it expects the timestamp
as the first column and then 4 data columns. The data returned will be the time array and a data array with 5 columns.
The first column of that array can be ignored, it's just time in seconds extracted from the timestamp.

Your task:
Query for the month of September or October and exclude the DC components (solar contributions) from the power and energy data.
Once you choose your month, you can replace any reference and instruction with November with your choice.
"""

# create connection using the sqlUtils class
con = sqlUtils.sqlCon()

# define query here
query = ("SELECT timestamp, tempSet, tempActual, (realP+dcP), (acE+dcE) FROM measurement "
                             "WHERE containerID=3 and MONTHNAME(timestamp) = 'November' ORDER BY timestamp ; " )

# connect to DB
cnx = con.db_connect()

# run the query and return data in frames
nptime, simout = con.db_query(cnx, query)


"""
Data Extraction

Now that we have data in the variables nptime and simout, we want to extract the data and put them into a
pandas array. Once the data is in the array, you can play arround with it to extract some information such as number
of datapoints, and so on.
It's also a good opportunity to learn about data access once they're in the array.

Use the given examples to do the tasks.
"""

# data extraction, just renaming here
setpoint = simout[:,1]
temperature = simout[:,2]
power = simout[:,3]
energy = simout[:,4]

# store everything in a pandas dataframe
data = pd.DataFrame({"Setpoint": setpoint, "Temperature": temperature, "Power": power, "Energy": energy})
# set the index based on time
data = data.set_index(pd.DatetimeIndex(nptime))

# example on how to access columns in the data frame (think of it as DB relation with time as the primary key)

# get the indices
print "Indeces: ", data.index

""" Quick Note
Arguments can be printed in the same line using the print statement in Python 2.7 and seperating them with
a comma. As in many other languages, single and double quotations are strings.

String concatenation can be done with a plus symbol.
For example, "Happy" + " " + "Holidays!" , would result in: "Happy Holidays!".
"""

# get setpoint.
print "Setpoints: ", data.Setpoint
# or
print "Setpoints: ", data["Setpoint"]

""" YOUR TASK,
print the remaining columns using each method at least once
"""
#print
#print
#print

# Accessing individual data points by row number or date key
print "First temperature record: ", data.Temperature[0]     # everything's 0-indexed in Python
print "Temperature on Nov. 11, 10.10pm: ", data['2017-11-11 22:10'].Temperature
print "Entire record for Nov. 11, 10.10pm: ", data['2017-11-11 22:10']

# Time ranges
print "Energy for Nov. 3-6: ", data['2017-11-03':'2017-11-06'].Energy
print "No of energy between Nov. 3-6: ", data['2017-11-03':'2017-11-06'].Energy.size
print "No of records between Nov. 3-6: ", data['2017-11-03':'2017-11-06'].size

""" YOUR TASK,
* show the temperature on Nov. 15 at 3pm
* show the temperature on Nov. 15 between 3 and 7 pm
* show the setpoint Nov. on 15 between 3 and 7pm
* show the difference between the setpoint and the temperature on Nov. 15 between 3 and 7pm
    ** subtract one from the other
"""

#print
#print
#print
#print


"""
Statistics

In the following section, we will implement some statistics to analyze our
time series data.

You will need to use the following functions
- sum()
- max()
- min()
- mean()
- std()


"""

# Energy data is in Watt-hour, so convert to kWh
# total consumption
print "Total Consumption: ", data.Energy.sum() / 1000  , " kWh"#
# avg daily consumption --- YOUR TURN , hint: 30 days in November
print "Avg Daily Consumption: ",

# Power
# peak power of the month,
print "Peak Power in November: ", data.Power.max() ,  " W"
# variability (stand. deviation in power consumption , YOUR TURN
print "Variability in Power Consumption",

# Temperature
# avg temperature
print "Average Actual Temperature: ", data.Temperature.mean(), " deg F"
# variability (stand. deviation)
print "Variability in Temperature: ",
# minimum temperature
print "Minimum Temperature: ",


# Temperature Error
# Total
print "Monthly Cummulative Temperature Error: ", sum(x for x in abs(data.Setpoint - data.Temperature)) , " deg F"
# Avg daily --- YOUR TURN , hint: 30 days in November
print "Average Daily Cummulative Temperature Error: ",
# Avg hourly --- YOUR TURN
print "Average Hourly Cummulative Temperature Error: ",



"""
Visualization

There are many ways to visualize this data, so let's just take a look at some of them.
In the end, we will look at creating a loop that can plot data for every day of the month.

We'll be relying on the pandas plot function, which basically just encapsulates the matplotlib
graphing library.

"""

# Power Graph
# Try out different days and time spans, and decide on which one you want to save in the end
# Go here and pick your colormap: http://matplotlib.org/1.4.3/examples/color/colormaps_reference.html
fig, axes = plt.subplots(figsize=(15,7))
data['2017-11-02'].plot(ax=axes, y=["Power"], colormap='Spectral')
axes.set_title('Power Consumption, November 02, 2017')
axes.set_ylabel('Power [W]')
fig.tight_layout()
fig.savefig("output/power_nov1.png")

# Temperature
# Try out different days and time spans, and decide on which one you want to save in the end
# Go here and pick your colormap: http://matplotlib.org/1.4.3/examples/color/colormaps_reference.html
fig, axes = plt.subplots(figsize=(15,7))
data['2017-11-02'].plot(ax=axes, y=["Setpoint", "Temperature"], colormap='Spectral')
axes.set_title('Temperature, November 02, 2017')
axes.set_ylabel('Temperature [F]')
fig.tight_layout()
fig.savefig("output/temp_nov1.png")

# Energy
# Let's try out daily bar graphs through the month
# We need to group data by day as you may remember from Tableau ...

print "Resampled and summed energy day: ", data.resample('D').Energy.sum()/1000

#data2 = pd.DataFrame({"Energy": data.resample('D').Energy.sum()/1000})
energyDailyData = data.resample('D').sum()
energyDailyData.Energy /= 1000.0

# Your task is to also display total kWh in the title using the concatenation operator.
# You'll need to convert the float to a string using the str() operatore
fig, axes = plt.subplots(figsize=(15,7))

#energyDailyData.plot(ax=axes,kind='bar', y="Energy", colormap='Spectral')

# we're using matplotlib's bar chart because the pandas plot doesn't show nice xticks
axes.bar(energyDailyData.index, energyDailyData.Energy, color='b')
axes.set_title('Energy Usage, November, 2017')
axes.set_ylabel('Energy [kWh]')
axes.xaxis.set_major_locator(mdates.WeekdayLocator())
#set major ticks format
axes.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

fig.tight_layout()
fig.savefig("output/energy_nov.png")


# This is the loop that output one graph per day , please change the output filename of it.
# Uncomment below to output files
last_day = ""

for i, day in enumerate(pd.unique(data.index)):

    if last_day != str(day).split("T",1)[0]:
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15,9), sharex=False, )

        print str(day).split("T",1)[0]

        data[str(day).split("T",1)[0]].plot(ax=axes[0], y=["Setpoint", "Temperature"]); axes[0].set_title('Temperature, '+ str(day).split("T",1)[0]);
        data[str(day).split("T",1)[0]].plot(ax=axes[1], y=["Power"]); axes[1].set_title('Power Consumption, '+ str(day).split("T",1)[0]);

        fig.tight_layout()
        fig.savefig("output/output_"+str(day).split("T",1)[0]+".png")

    last_day = str(day).split("T",1)[0]

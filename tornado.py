"""
Caroline Williams
created: January 31, 2021
updated: February 6, 2021
Storms: Tornadoes Project
This script examines tornado start points in the US over history.
"""

# Import Libraries
from urllib.request import urlopen
from zipfile import ZipFile
from census import Census
from us import states
import geopandas as gpd
import matplotlib.pyplot as plt
import descartes


# Download NWS Tornado Data
# TODO: convert absolute paths to relative path

torn_url = 'https://www.spc.noaa.gov/gis/svrgis/zipped/1950-2019-torn-initpoint.zip'

# get zip file
respt = urlopen(torn_url)
tempzipt = open("C:/Users/Caroline/Documents/Projects/storms/temp/1950-2019-torn-initpoint.zip", "wb")
tempzipt.write(respt.read())
tempzipt.close()

# unzip and direct shapefile output
zipt = ZipFile("C:/Users/Caroline/Documents/Projects/storms/temp/1950-2019-torn-initpoint.zip")
zipt.extractall("C:/Users/Caroline/Documents/Projects/storms/data/")

county_url = 'https://opendata.arcgis.com/datasets/48f9af87daa241c4b267c5931ad3b226_0.zip'

respc = urlopen(url)
tempzipc = open("C:/Users/Caroline/Documents/Projects/storms/temp/USA_Counties-shp.zip", "wb")
tempzipc.write(resp.read())
tempzipc.close()

# unzip and direct shapefile output
zipc = ZipFile("C:/Users/Caroline/Documents/Projects/storms/temp/USA_Counties-shp.zip")
zipc.extractall("C:/Users/Caroline/Documents/Projects/storms/data/USA_Counties")

# Import data
torn = gpd.read_file("C:/Users/Caroline/Documents/Projects/storms/data/1950-2019-torn-initpoint/1950-2019-torn-initpoint.shp")
county = gpd.read_file("C:/Users/Caroline/Documents/Projects/storms/data/USA_Counties/USA_Counties.shp")

# Calculate Number of tornadoes per year in the US
torn['obsv'] = 1 # add a new column and fill values with 1
sum = torn.groupby(["yr"]).sum(["obsv"]) # calculate observations by year

# Plot Tornado Observations by Year
plt.plot(sum["obsv"]) # plot observation column
plt.xlabel("Year") # x-axis title
plt.ylabel("Tornado Frequency") # y-axis title
plt.title("Number of Tornadoes per Year 1950 - 2019") # title

# export figure
plt.savefig("C:/Users/Caroline/Documents/Projects/storms/figures/tornado_freq.png")

# display figure
plt.show() # display plot

# Projecting
torn = torn.set_crs(epsg=4326)
print(torn.crs)
county = county.set_crs(epsg=4326)
print(county.crs)

# Join tables
torn_county = gpd.sjoin(county, torn, how = "inner", op = 'intersects')
torn_county = torn_county[["NAME", "STATE_NAME", "obsv", "geometry"]]

# Remove Alaska, Hawaii, & US territories
# remove from tornado county data
states = "Alaska", "Hawaii", "Puerto Rico"
for i in states:
    torn_county = torn_county[torn_county.STATE_NAME != i]

# remove from county data
for i in states:
    county = county[county.STATE_NAME != i]

# Aggregate sum by state
sum_county = torn_county.dissolve(by="NAME", aggfunc='sum')

# Save county data
sum_county.to_file("C:/Users/Caroline/Documents/Projects/storms/data/outputs/county.shp")
sum_county = gpd.read_file("C:/Users/Caroline/Documents/Projects/storms/data/outputs/county.shp")

# Maps
# Sum of Tornado Occurrences 1950 - 2019
torn.reset_index(drop=True, inplace=True)
fig, ax = plt.subplots()
county.plot(ax=ax, color = "darkgrey")
sum_county.plot(ax=ax, column = 'obsv')
plt.title("Total Number of Tornadoes 1950 - 2019")
#plt.colorbar(mappable=sum_county, label="Sum", orientation="vertical")
plt.tight_layout()
plt.show()

# Export Map
plt.savefig("C:/Users/Caroline/Documents/Projects/storms/maps/tornado_sum_1950_2019.png")

# TODO: create subplots of average number of tornadoes per state by 4 time periods or all time
# TODO: alongside total and average maps, plot damage or tornado severity

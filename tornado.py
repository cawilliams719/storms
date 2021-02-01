"""
Caroline Williams
January 31, 2021
Storms: Tornadoes Project
This script examines tornado start points in the US over history.
"""

# Import Libraries
from urllib.request import urlopen
from zipfile import ZipFile
import geopandas as gpd
import matplotlib.pyplot as plt


# Download NWS Tornado Data
# TODO: convert absolute paths to relative path
"""url = 'https://www.spc.noaa.gov/gis/svrgis/zipped/1950-2019-torn-initpoint.zip'

resp = urlopen(url)
tempzip = open("C:/Users/Caroline/Documents/Projects/storms/temp/1950-2019-torn-initpoint.zip", "wb")
tempzip.write(resp.read())
tempzip.close()

zip = ZipFile("C:/Users/Caroline/Documents/Projects/storms/temp/1950-2019-torn-initpoint.zip")
zip.extractall("C:/Users/Caroline/Documents/Projects/storms/data/")"""

# Import data
# TODO: add in country GIS data to calculate avg number of tornadoes by state (Chloropleth Map)
torn = gpd.read_file("C:/Users/Caroline/Documents/Projects/storms/data/1950-2019-torn-initpoint/1950-2019-torn-initpoint.shp")

# Data manipulation
torn['obsv'] = 1 # add a new column and fill values with 1
sum = torn.groupby(["yr"]).sum(["obsv"]) # calculate observations by year

# Plot Tornado Observations by Year
plt.plot(sum["obsv"]) # plot observation column
plt.xlabel("Year") # x-axis title
plt.ylabel("Tornado Frequency") # y-axis title
plt.title("Number of Tornadoes per Year 1950 - 2019") # title
plt.show() # display plot

# export figure
plt.savefig("C:/Users/Caroline/Documents/Projects/storms/figures/tornado_freq.png")

# Join tables
# TODO: remove Alaska and Hawaii - keep CONUS
#torn.plot()
#plt.show()
"""world = gpd.datasets.get_path('naturalearth_lowres')
na = world[world.continent == 'North America'].plot(
    color = 'white',
    edgecolor = 'black')

torn.plot(na, color = 'yellow')
plt.show()"""

"""
Caroline Williams
January 31, 2021
Storms: Tornadoes Project
This script examines tornado start points in the US over history.
"""

## Import Libraries
from urllib.request import urlopen
from zipfile import ZipFile
import geopandas as gpd


## Download NWS Tornado Data
# TODO: convert absolute paths to relative path
url = 'https://www.spc.noaa.gov/gis/svrgis/zipped/1950-2019-torn-initpoint.zip'

resp = urlopen(url)
tempzip = open("C:/Users/Caroline/Documents/Projects/storms/temp/1950-2019-torn-initpoint.zip", "wb")
tempzip.write(resp.read())
tempzip.close()

zip = ZipFile("C:/Users/Caroline/Documents/Projects/storms/temp/1950-2019-torn-initpoint.zip")
zip.extractall("C:/Users/Caroline/Documents/Projects/storms/data/")

## Import data
torn_1950_2019 = gpd.read_file("C:/Users/Caroline/Documents/Projects/storms/data/1950-2019-torn-initpoint/1950-2019-torn-initpoint.shp")
# Geospatial Projects

### About Me
I have completed my bachelor and master degree in Urban and Rural Planning Discipline at Khulna University. At present, I am pursing my Master in Science in Earth Sciences (Geogrphy) at the University of Memphis. I am also working as Graduate Research Assistant in Applying Induced Travel Study in Tennessee. I love to work with geospatial data. I want to unfold differnt real worlds problems with the help of geospatial and statistical methods.

### Education
- M.S. in Earth Sciences, The University of Memphis, Jan 2024 – Present
- Master of Urban and Rural Planning, Khulna University, Jul 2022 – Jan 2024
- Bachelor of Urban and Rural Planning, Khulna University, Jan 2017 – Mar 2022

### Adv. GIS Course Project List
**Final Project: Remote Sensing Index Calculation**

Description
- Before using this code, user must have an account on [Google Earth Engine](https://code.earthengine.google.com/) and a cloud project. If you are first time using Google Earth Engine in Python platform you can check out this [geemap website](https://geemap.org/installation/).
  
- In this project, I tried to give user as much flexibility as I can. After successfully authenticate the GEE map, user will have option to choose which way user want to import the area of interest. At present there are two option:
    1. calling from google earth engine cloud project;
    2. local shapefile.
  
- After defining the AOI, user can input the date range and how much cloud cover user will consider.
  
- Then user will have option to choose which index or indices (NDVI, SAVI, MSAVI, GRVI, NDWI, MNDWI,MAWEI, NDMI, NDBI, and LST) user want to calculate.
  
- The code will run in a loop until user want to break the program.
  
- The calculated index or indices will save to a folder name 'GEE_Exports' in user's google drive.
  
- Here is the final project [Github Repository Link](https://github.com/luisvillalxv/Adv-GIS-project/blob/246ff7ca2339e710443fe2458a1d7b60543e4d7a/RemoteSensingIndexCalculation.ipynb)

**ArcGIS Pro Toolbox: Batch Pixel Count to Table**

Description
- In this toolbox, there is two tools:
    1. Batch Pixel Count to Table for All Classes
    2. Batch Pixel Count to Table for Single Class
- If you have more than one same type of rasters and you want to count the pixel size for each raster and store into one single CSV file then this tools will be helpful for you.
- In this toolbox, you can set the workplace, and it will automatic list out the rasters store in that geodatabase or folder.
- Then user had to input the class name (e.g., Value, landcover etc)
- If user want to count spefice class then user has to input the value of that class.
- Finally, user had to specify the file name (Note: User must add extension .csv or .txt after giving the file desire name)
- Here is the toolbox and Python files [Github Respository Link](https://github.com/biswasjayanta/Python-For-GeospatialAnalysis/tree/5e9966ec2bdb445308100a1cecd5664bb2adf65a/BatchPixelCountToolbox)

# Geospatial Solutions 🛰️

### About Me
I have completed my bachelor and master degree in Urban and Rural Planning Discipline at Khulna University. Also got my second master degree in Earth Sciences from the University of Memphis. At present, I am pursing my Doctoral Degree in Geography at the University of North Carolina at Charlotte.

I love to work with geospatial data. I want to unfold differnt real worlds problems with the help of geospatial and statistical methods. In this [Github page](https://biswasjayanta.github.io), you will find differnt real worlds problem that I have been tried to solve with the help of GIS and programming language and it's packages. 

### Education
- PhD in Geography, University of North Carolina at Charlotte, Jan 2026 - Present
- M.S. in Earth Sciences, The University of Memphis, Jan 2024 – Dec 2025
- Master of Urban and Rural Planning, Khulna University, Jul 2022 – Jan 2024
- Bachelor of Urban and Rural Planning, Khulna University, Jan 2017 – Mar 2022

### Portfolio Link (Geovisualization)

[Geovisualization Portfolio](https://biswasjayanta.github.io/GeoVisualization_Portfolio.html)

### Geospatial Project List
**Final Project: Remote Sensing Index Calculation**

*What are the spatial indices in remote sensing?*

Spectral Indices are a set of mathematical equations performed on a per-pixel basis on data coming from multispectral remote sensing (satellite) data.

When looking at satellite data, you don’t get a single image, you get all the red data, all the blue data, all the green data, right through infra-red up to ultraviolet. Then you apply a formula to each pixel to pull out information you want.

A spectral index is a formula that helps different phenomena on the ground be perceived. You can detect things like soil moisture, “greeness” - which can be a proxy for biomass, the composition of the land - such as ferric oxide, flooding, and even tracking seaweed in the ocean.

A lot can be inferred from this data, and it is absolutely fascinating to go down rabbit holes in this area.

*Importance and Application*

Remote sensing spectral indices are incredibly valuable tools with a wide range of practical applications. These indices help us explore the environment further and gather valuable insights. By harnessing the power of satellite data and mathematical formulas, these indices empower researchers, scientists, and environmentalists to make informed decisions and contribute to the preservation and sustainable management of our planet's resources.

Increasingly they can be used in industry, putting the insights derived from these indices into the hands of people and businesses who are affected by the real world impacts which the indices can highlight, like flood and fire risk.

*Motivation*

In traditional way, we have to download the data from respective satellite image sources if the area of interest doesn't cover with one tile then we have to download several which is time consuming. On the other hand, if we want to comapre between differnt satellite then it become far more difficult and time consuming. The emergence of Google Earth Engine dose save the hassel of downloading the satellite images but still we have to code for diffent satellite and each time we run the code it run all the lines. My motivation comes from what if I want to calculate one or more indices from without rewriting the code. What if I want to switch between satellites!! That is why I tried to develop this **Remote Sensing Indices Tool** with the help of Python library where I can choose which satellite how many index I want without rewriting the code each time.   

*Tool Description*

- Before using this code, user must have an account on [Google Earth Engine](https://code.earthengine.google.com/) and a cloud project. If you are first time using Google Earth Engine in Python platform you can check out this [geemap website](https://geemap.org/installation/).
  
- In this project, I tried to give user as much flexibility as I can. After successfully authenticate the GEE map, user will have option to choose which way user want to import the area of interest. At present there are three options:
    1. From Google Earth Engine cloud project;
    2. Local Shapefile.
    3. Draw on the Map
  
- After defining the AOI, user can input the date range and how much cloud cover user will consider.

- User has option to choose which satellite image user want to use: Landsat-8 or Sentinel-2
  
- Then user will have option to choose which index or indices **(NDVI, SAVI, MSAVI, GRVI, NDWI, MNDWI,MAWEI, NDMI, NDBI, and LST)** user want to calculate.
  
- The code will run in a loop until user want to break the program.
  
- The calculated index or indices will save to a folder name **'GEE_Exports'** in user's google drive.
  
- Here is the final project [Github Repository Link](https://github.com/biswasjayanta/Python-For-GeospatialAnalysis/blob/8950e5e82e8f1eee43281e13bcc2e8f09873c6c0/RemoteSensingIndexCalculation.ipynb)

**ArcGIS Pro Toolbox: Batch Pixel Count to Table**

*Motivation*

During one of my final class project, I run into a problem. I had 84 study sites and 9 years of land use land cover images. For each study site, I had 3 buffers (half kilometer, one kilometer, and one and half kilometers). For each buffer from 84 sites from 9 years land cover data, I had to find out how much developed areas I had for each buffer. So, finally I had 2268 rasters from where I had to extract number of pixels for developed areas into a single csv file. This huge task motivated me to developed this **ArcGIS Pro Script Tool** where I can just input my workplace and relax and the tool will calculate the pixel and give me a single csv file.

*Description*
- In this toolbox, there is two tools:
    1. Batch Pixel Count to Table for All Classes
    2. Batch Pixel Count to Table for Single Class
- If you have more than one same type of rasters and you want to count the pixel size for each raster and store into one single CSV file then this tools will be helpful for you.
- In this toolbox, you can set the workplace, and it will automatic list out the rasters store in that geodatabase or folder.
- Then user had to input the class name (e.g., Value, landcover etc)
- If user want to count spefice class then user has to input the value of that class.
- Finally, user had to specify the file name (Note: User must add extension .csv or .txt after giving the file desire name)
- Here is the toolbox and Python files [Github Respository Link](https://github.com/biswasjayanta/Python-For-GeospatialAnalysis/tree/5e9966ec2bdb445308100a1cecd5664bb2adf65a/BatchPixelCountToolbox)

**Remote Sensing Ecological Index (Ongoing)**

*Motivation*

Rapid urbanization greatly damaged the ecology and environment. Due to this, there are several problems occured such as urban heat island, air-water-soil polution, destruction of local vegetation and animal species, and many more. All of these are contributing to global climate change as well as hampering the path of sustainable development. Remote sensing can be a effective tool to actively monitor the environmental degradation. This index will combined normalized difference vegetation index (NDVI), wetness index, normalized difference build-up and soil index (NDBSI), and land surface temperature (LST) using weighted entropy value method and moving window.

*Description*

- This tool will call Geemap in python environment and then calculate the necessary indices (NDVI, Wetness, NDBSI, and LST)
- Export the image to the drive
- Convert the image to point in ArcGIS Pro
- Extract the multivalue to the points
- Export the CSV and import into the python enviornment for RSEI calculation
- Here is the Github Respository for both of this code: [Index Calculation](https://github.com/biswasjayanta/Python-For-GeospatialAnalysis/blob/7d0dd8a7bce8d6c6ebc82a895e523db1bcc8e958/ecological_index.ipynb) [RSEI Calculation](https://github.com/biswasjayanta/Python-For-GeospatialAnalysis/blob/4ff1f6fc2777eea52071cba033b01ec55f95fd02/RMSI.py)
[Note: I am still working to make this code into one seemless python code]

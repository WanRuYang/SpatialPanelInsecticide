# SpatialPanelInsecticide
Applied spatial panel model to unveil the relationship between crop diversity

### Define model variables and feature engineering:
- y = insecticide use intensity
    - load data (Pesticide Use Reporting, PUR, data in csv and associated shapfile format) to postgresql database
    - extracted field-level data (annual) and aggregated to the smallest areal unit (~ 1 square mile "sections") defined in the shapefile
- x1 = crop diverstiy
    - extracted annual crop type data from the aforementioned database
    - write python code to calculate crop diversity at section level
- x2 = crop value
    - extracted crop market value from California agricultural report 
    - estimate section-level annual crop value with PUR data
- x3 = growing season degree day (GDD)
    - download PRISM data
    - estimate lower temperature bond using insecticide database
    - estimate annual GDD at aggregate to section level
- x4 = evapotranspiration (Etc)
    - download modis image and CIMIS data
    - reproject and resample to estiamte 
    - calculate NDVI from modis image and estimate Etc from 
- Spatial weights matrix:
    - R spdep package and the section shapefile 

### Model estimation:
- R splm package




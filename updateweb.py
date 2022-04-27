import sys 

sys.path.append('/Users/juliaputko/pyglider')
import pyglider.website as pyweb
import logging

logging.basicConfig(level=logging.DEBUG)


# uses the templat in `.templates/deploymentsIndex.html` to render
# index.html in each of the subdirectories:



#pyweb.geojson_deployments('./')
#pyweb.index_deployments('./dfo-walle652/')
#pyweb.index_deployments('./dfo-bb046/')
#pyweb.url_jp('./')
#pyweb.ticker('./')
#pyweb.index_story('./')

#if 1:
    #pyweb.index_deployments('./dfo-rosie713/')
    #pyweb.index_deployments('./dfo-mike579/')
    #pyweb.index_deployments('./dfo-eva035/')



####
## rerun pyglider slocum processing script 
#outname = slocum.raw_to_L1timeseries(rawdir, l1tsdir, deploymentyaml,
#            profile_filt_time=400, profile_min_time=100)

###

"""
#####################################

#walle's figure processing 

import logging
import os
import pyglider.ncprocess as ncprocess
import pyglider.plotting as pgplot
import pyglider.slocum as slocum

logging.basicConfig(level='DEBUG')

binarydir  = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/realtime_raw/'
rawdir     = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/realtime_rawnc/'
cacdir     = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/cac/'
sensorlist = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/dfo-walle652_sensors.txt'
deploymentyaml = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/deploymentRealtime.yml'
l1tsdir    = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/L0-timeseries/'
profiledir = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/L0-profiles/'
griddir    = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/L0-gridfiles/'
plottingyaml = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/plottingconfig.yml'
scisuffix    = 'tbd'
glidersuffix = 'sbd'


#outname = 'L1-timeseries/rosie713-20190314T1920_L1.nc'
outname = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/L0-timeseries/dfo-walle652-20210121.nc'
pgplot.timeseries_plots(outname, plottingyaml)

#outname = ncprocess.make_L2_gridfiles(outname, griddir, deploymentyaml)
outname = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/L0-gridfiles/dfo-walle652-20210121_grid.nc'
pgplot.grid_plots(outname, plottingyaml)


#####################################################################################



##bb's figure processing 

binarydir  = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/realtime_raw/'
rawdir     = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/realtime_rawnc/'
cacdir     = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/cac/'
sensorlist = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/dfo-bb046_sensors.txt'
deploymentyaml = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/deploymentRealtime.yml'
l1tsdir    = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/L0-timeseries/'
profiledir = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/L0-profiles/'
griddir    = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/L0-gridfiles/'
plottingyaml = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/plottingconfig.yml'
scisuffix    = 'tbd'
glidersuffix = 'sbd'

#/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511


#outname = 'L1-timeseries/rosie713-20190314T1920_L1.nc'
outname = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/L0-timeseries/dfo-bb046-20210511_L0.nc'
pgplot.timeseries_plots(outname, plottingyaml)

#outname = ncprocess.make_L2_gridfiles(outname, griddir, deploymentyaml)
outname = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/L0-gridfiles/dfo-bb046-20210511_grid.nc'
pgplot.grid_plots(outname, plottingyaml)



"""
#####
"""
import logging
import os
import pyglider.plotting as pgplot

walledir = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/L0-gridfiles/dfo-walle652-20210121_grid.nc'
wallerawnc = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/realtime_rawnc/dfo-walle652-0333-rawebd.nc'
wallefig = '/Users/juliaputko/processing/dfo-walle652/dfo-walle652-20210121/figs/MissionMap_jptest.png'

bbdir = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/L0-gridfiles/dfo-bb046-20210511_grid.nc'
bbrawnc = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/rawnc_realtime/dfo-bb046-rawgli.nc'
bbfig = '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20210511/figs/MissionMap_jptest.png'

#pgplot.test(walledir,wallerawnc,wallefig)
pgplot.test(bbdir, bbrawnc, bbfig)

"""
######


#### WALLE Map Creation 

#import logging
#import os
#import pyglider.mapplotting as mappgplot

#mappgplot.test2() 

#####


import pyglider.website as pyweb
import logging

logging.basicConfig(level=logging.DEBUG)
# uses the templat in `.templates/deploymentsIndex.html` to render
# index.html in each of the subdirectories:

pyweb.geojson_deployments('./')

if 1:
    #pyweb.index_deployments('./dfo-walle652/')
    pyweb.index_deployments('./dfo-bb046/')
    #pyweb.index_deployments('./dfo-rosie713/')
    #pyweb.index_deployments('./dfo-mike579/')
    #pyweb.index_deployments('./dfo-eva035/')

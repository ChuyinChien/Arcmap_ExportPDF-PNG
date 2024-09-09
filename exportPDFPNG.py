# !/usr/bin/python
# coding:utf-8

import arcpy, os, re, sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
mxds = arcpy.GetParameterAsText(0)
outPdf_check = arcpy.GetParameterAsText(1)
outPng_check = arcpy.GetParameterAsText(2)
mxdsList = mxds.split(";")
for fullpath in mxdsList:
    mxd_name = os.path.split(fullpath)[1][4:-7]
    mxd_fname = os.path.split(fullpath)[1][:-4]
    mxd_path = os.path.split(fullpath)[0]
    pdf_path = mxd_path.replace("MXD","PDF")
    if not os.path.exists(pdf_path):os.makedirs(pdf_path)
    png_path = mxd_path.replace("MXD","PNG")
    if not os.path.exists(png_path):os.makedirs(png_path)
    mxddoc = arcpy.mapping.MapDocument(fullpath)
    if str(outPdf_check) == "true":
        pdf_name = os.path.join(pdf_path, mxd_fname + ".pdf")
        arcpy.AddMessage("EXPORT PDF: " + pdf_name)
        arcpy.mapping.ExportToPDF(mxddoc, pdf_name,"",640,480,300,"BEST","RGB",False,"ADAPTIVE","VECTORIZE_BITMAP")
    if str(outPng_check) == "true":
        for lyr in arcpy.mapping.ListLayers(mxddoc,mxd_name+"*"):
            if lyr.datasetName == "TOWN_COUNTY_Boundary":
                lyr.transparency = 30
                arcpy.AddMessage(lyr.name + " Admin Trans = 30 ")
        mxddoc.saveACopy(mxd_fname + "(PNG)" + ".mxd", '10.1')
        png_name = os.path.join(png_path, mxd_fname + ".png")
        arcpy.AddMessage("EXPORT PNG: " + png_name)
        arcpy.mapping.ExportToPNG(mxddoc, png_name,"",0,0,300,)
    del fullpath
del mxdsList

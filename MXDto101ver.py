import arcpy, os, re, sys
mxds = arcpy.GetParameterAsText(0)

mxdsList = mxds.split(";")
for fullpath in mxdsList:
    mxd_name = os.path.split(fullpath)[1][4:-7]
    mxd_fname = os.path.split(fullpath)[1][:-4]
    mxd_path = os.path.split(fullpath)[0]
    newmxd_path = mxd_path.replace("MXD","MXD101")
    if not os.path.exists(newmxd_path):os.makedirs(newmxd_path)
    mxddoc = arcpy.mapping.MapDocument(fullpath)
    outmxd = os.path.join(newmxd_path, mxd_fname + ".mxd")
    mxddoc.saveACopy(outmxd, '10.1')
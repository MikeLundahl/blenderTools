import bpy

theObject01 = "Cube*"
theObject02 = "Sphere*"

#select objects
def selectObjects(theObjectName):
    bpy.ops.object.select_pattern(pattern=theObjectName)


selectObjects(theObject02)
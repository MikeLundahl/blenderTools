import bpy

theObjects = ["Cube*", "Sphere*"] 

#select objects
def selectObjects(theObjectName):
    for o in theObjectName: 
        bpy.ops.object.select_pattern(pattern=o)


selectObjects(theObjects)
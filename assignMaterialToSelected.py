import bpy

theMaterial = "gold_mtr.001"
selectedObjects =  bpy.context.selected_objects
theMaterial = bpy.data.materials.get(theMaterial)

#assign material
for i, val in enumerate(selectedObjects):
    # Assign it to object
    if selectedObjects[i].data.materials:
        # assign to 1st material slot
        selectedObjects[i].data.materials[0] = theMaterial
    else:
        # no slots
        selectedObjects[i].data.materials.append(theMaterial)

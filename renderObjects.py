import bpy

theObjectName = "Cube.00"
imageOutput = "C:/tmp/"
editableObjectsInScene = bpy.context.editable_objects

def selectObjects():
    bpy.ops.object.select_pattern(pattern= theObjectName + "*")
    selectedObjects = bpy.context.selected_objects
    hideAllEditableObjects(selectedObjects)

def renderObject():
    print('Rendering image')
    bpy.ops.render.render(animation=False, write_still=True, use_viewport=False, layer="", scene="")
    
def setOutput(index):
    bpy.context.scene.render.filepath = imageOutput + theObjectName + str(index) + ".png"
    
def hideAllEditableObjects(objects):
    for o in objects:
        o.hide_viewport = True
        o.hide_render = True
    unhideAndRender(objects)

def unhideAndRender(objects):
    for index, o in enumerate(objects):
        setOutput(index)
        o.hide_viewport = False
        o.hide_render = False
        renderObject()
        o.hide_viewport = True
        o.hide_render = True
    unhideAllObjects(objects)
        
def unhideAllObjects(objects):
    for o in objects:
        o.hide_viewport = False
        o.hide_render = False

def initRender():
    print("Render initiated")
    selectObjects()

initRender()

print('done')





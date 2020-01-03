import bpy

#Create few objects
pos = 0
for i in range(6):
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(pos, 0, 0))
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, location=(pos, 3, 0))
    pos = pos + 3
    

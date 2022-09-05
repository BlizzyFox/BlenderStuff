# Sets selected vertices  to Basis position
#
# By BlizzyFox
# 
# Select starting shape key and select problem vertices in Edit mode.
# Run script. 

import bpy

obj = bpy.context.active_object

startShape = obj.active_shape_key_index

shapeKeyListLength = len(obj.data.shape_keys.key_blocks)

#Override incase you want to stop before the end of the shapekey list
endShape = shapeKeyListLength

for i in range(startShape, endShape):
    #Set Shapekey
    obj.active_shape_key_index = i
    print(obj.active_shape_key.name)
    #Blend from shape stuff
    bpy.ops.mesh.blend_from_shape(shape="Basis", blend=1.0, add=False) #Blend from basis

import bpy
from math import radians
from bpy_extras import image_utils

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Clear all elementes (lights, cameras, movies).
lights = bpy.data.lights
for lt in lights:
    bpy.data.lights.remove(lt)
    
movies = bpy.data.movieclips
for mc in movies:
    bpy.data.movieclips.remove(mc)
    
cameras = bpy.data.cameras   
for cm in cameras:
    bpy.data.cameras.remove(cm)
    
images = bpy.data.images   
for im in images:
    bpy.data.images.remove(im)
    
#camera parameters.
focal_length = 15
camera_posx = 0
camera_posy = 0 
camera_posz = 0
camera_rotx = 90
camera_roty = 0 
camera_rotz = 90
camera_resolution_x = 1280 
camera_resolution_y = 1024

#projector parameters.
projector_posx = -14.8724 
projector_posy = 85.9443  
projector_posz = -14.4028 
projector_rotx = 98.4275
projector_roty = 0
projector_rotz = 89.728

#camera setup.
bpy.ops.object.camera_add()
camera = bpy.data.objects['Camera']
camera.data.lens = focal_length
camera.location[0] = camera_posx
camera.location[1] = camera_posy
camera.location[2] = camera_posz
camera.rotation_euler[0] = radians(camera_rotx)
camera.rotation_euler[1] = radians(camera_roty)
camera.rotation_euler[2] = radians(camera_rotz)

#projector setup.
bpy.ops.projector.create()
bpy.ops.projector.switch_to_cycles()
projector = bpy.data.objects['Projector']
projector.proj_settings.projected_texture = 'custom_texture'
projector.location[0] = projector_posx/1000
projector.location[1] = projector_posy/1000
projector.location[2] = projector_posz/1000
projector.rotation_euler[0] = radians(projector_rotx)
projector.rotation_euler[1] = radians(projector_roty)
projector.rotation_euler[2] = radians(projector_rotz)

# -*- coding: utf-8 -*-
# Blender 3.0.1 schematic apartment study, version v001.
# Source: 01-source-drawings/Screenshot from 2026-11-11 20-25-21.png
# WARNING: PIXEL-TRACED GEOMETRY, NOT DIMENSIONALLY VERIFIED.
# Do not use for construction. Run inside Blender 3.0.1, then save .blend.
import bpy
import math
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
SCALE=0.0128  # approximate only, must be replaced by verified dimensions
X0,Y0=460,810
def xy(x,y): return ((x-X0)*SCALE,(Y0-y)*SCALE)
def material(name,rgb):
 m=bpy.data.materials.new(name)
 m.diffuse_color=(*rgb,1)
 return m
oak=material("Light oak / concept",(0.57,0.39,0.24))
white=material("Fixed walls / approximate",(0.83,0.82,0.78))
linen=material("Textile / concept",(0.72,0.67,0.60))
def cube(name,cx,cy,sx,sy,sz,z,mat):
 bpy.ops.mesh.primitive_cube_add(size=1,location=(cx,cy,z+sz/2))
 ob=bpy.context.object
 ob.name=name
 ob.dimensions=(sx,sy,sz)
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 ob.data.materials.append(mat)
 return ob
def rectangle(name,x1,y1,x2,y2,h,mat,z=0):
 a,b=xy(x1,y1),xy(x2,y2)
 return cube(name,(a[0]+b[0])/2,(a[1]+b[1])/2,abs(a[0]-b[0]),abs(a[1]-b[1]),h,z,mat)
def wall(name,x1,y1,x2,y2):
 a,b=Vector(xy(x1,y1)),Vector(xy(x2,y2))
 c=(a+b)/2
 ob=cube(name,c.x,c.y,(b-a).length,0.15,2.65,0,white)
 ob.rotation_euler.z=math.atan2(b.y-a.y,b.x-a.x)
# Room extents are visual placeholders, not certified walls.
for name,coords in [
 ("03 kitchen, labeled 11.9 m2",(558,289,817,573)),
 ("04 young adult room, labeled 12.5 m2",(831,289,1077,618)),
 ("05 adult bedroom, labeled 18.0 m2",(1102,289,1490,575)),
 ("01 hallway, labeled 10.3 m2",(675,622,1159,774)),
 ("02 bathroom, labeled 4.6 m2",(489,598,665,773))]:
 rectangle(name,*coords,0.10,oak,z=-0.10)
for name,coords in [
 ("kitchen west",(555,287,555,572)),
 ("kitchen / bedroom partition",(819,370,819,620)),
 ("young adult north",(830,286,1077,286)),
 ("young adult east",(1084,289,1084,618)),
 ("young adult south left",(819,620,954,620)),
 ("young adult south right",(1016,620,1084,620)),
 ("adult bedroom north",(1103,287,1490,287)),
 ("adult bedroom east",(1492,288,1492,574)),
 ("adult bedroom south",(1160,576,1491,576)),
 ("adult bedroom west",(1092,288,1092,619))]:
 wall(name,*coords)
# Furniture blocks are options; NOT verified against outlet locations.
rectangle("kitchen worktop proposal",558,310,610,549,0.90,oak)
rectangle("kitchen dining table proposal",665,432,755,491,0.75,oak)
rectangle("young adult bed proposal",853,329,950,487,0.48,linen)
rectangle("young adult desk proposal",995,413,1069,515,0.74,oak)
rectangle("young adult wardrobe proposal",838,531,914,589,2.20,oak)
rectangle("adults double bed proposal",1210,355,1362,520,0.48,linen)
rectangle("adults wardrobe proposal",1418,311,1470,525,2.30,oak)
rectangle("hallway wardrobe proposal",1030,686,1120,735,2.30,oak)
bpy.ops.object.light_add(type='AREA',location=(6,9,9))
bpy.context.object.data.energy=1800
bpy.context.object.data.size=9
bpy.ops.object.camera_add(location=(7,-10,15))
cam=bpy.context.object
direction=Vector((6.3,4.2,0))-cam.location
cam.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
cam.data.type='ORTHO'
cam.data.ortho_scale=20
scene=bpy.context.scene
scene.camera=cam
scene.render.engine='BLENDER_EEVEE'
scene.render.resolution_x=1600
scene.render.resolution_y=1000
scene.unit_settings.system='METRIC'
scene.render.filepath='//apartment-overview-v001.png'
bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath('//apartment-schematic-v001.blend'))
print("Saved schematic only; verify geometry and Blender 3.0.1 compatibility.")

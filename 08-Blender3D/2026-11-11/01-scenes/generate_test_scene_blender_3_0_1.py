# Apartment Interior Design — Blender 3.0.1 test scene
# Open in Blender 3.0.1 > Scripting > Open > Run Script.
# Creates a simple living-room blockout and saves apartment-test.blend.
import bpy, math, os
from mathutils import Vector

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
s=bpy.context.scene
s.unit_settings.system='METRIC'
s.render.engine='BLENDER_EEVEE'
s.render.resolution_x=1280
s.render.resolution_y=800
s.render.resolution_percentage=100
s.eevee.use_gtao=True

def material(n,c):
    m=bpy.data.materials.new(n); m.diffuse_color=(*c,1); return m
white=material('Warm white',(0.82,0.79,0.72))
oak=material('Natural oak',(0.55,0.37,0.20))
fabric=material('Greige upholstery',(0.48,0.43,0.36))
dark=material('Graphite',(0.035,0.04,0.045))
glass=material('Window glass',(0.42,0.62,0.72))
def box(n,loc,dim,ma):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o=bpy.context.object; o.name=n; o.dimensions=dim
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(ma); return o
# 5.2 x 4.2 m room; front wall omitted for visibility
box('Floor',(0,0,-.08),(5.2,4.2,.16),oak)
box('Back wall',(0,2.05,1.375),(5.2,.12,2.75),white)
box('Left wall',(-2.54,0,1.375),(.12,4.2,2.75),white)
box('Right wall',(2.54,0,1.375),(.12,4.2,2.75),white)
box('Window frame',(-.75,1.975,1.72),(1.75,.055,1.25),dark)
box('Window glass',(-.75,1.94,1.72),(1.62,.025,1.12),glass)
box('Radiator',(-.75,1.78,.48),(1.35,.18,.48),white)
box('Sofa base',(-1.65,-.35,.34),(1.05,2.25,.42),fabric)
box('Sofa back',(-2.12,-.35,.78),(.22,2.25,.78),fabric)
box('Coffee table',(-.05,-.25,.43),(1.1,.85,.08),oak)
box('Media console',(2.05,.25,.32),(.42,1.9,.48),oak)
box('TV',(2.28,.25,1.35),(.08,1.55,.92),dark)
box('Rug',(.05,-.25,.015),(2.5,2.25,.025),fabric)
bpy.ops.object.camera_add(location=(6.8,-7.8,5.2))
cam=bpy.context.object
cam.rotation_euler=(Vector((0,.15,1))-cam.location).to_track_quat('-Z','Y').to_euler()
cam.data.lens=40; s.camera=cam
bpy.ops.object.light_add(type='AREA', location=(0,-1,2.55))
light=bpy.context.object; light.data.energy=1100; light.data.shape='DISK'; light.data.size=4
light.rotation_euler=(math.radians(15),0,math.radians(20))
s.render.image_settings.file_format='PNG'
s.render.filepath='//apartment-test-render.png'
try: folder=os.path.dirname(os.path.abspath(__file__))
except NameError: folder=bpy.path.abspath('//')
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(folder,'apartment-test.blend'))

# Blender 3.0.1: import GLB v002 and save native .blend
# Place apartment-geometry-v002-2026-11-11.glb in the same folder.
# Usage: blender --background --python import_apartment_v002.py
import bpy
import os
from mathutils import Vector
assert bpy.app.version[:3] == (3, 0, 1), "Run this script in Blender 3.0.1"
base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "apartment-geometry-v002-2026-11-11.glb")
assert os.path.isfile(src), "Missing GLB next to script: " + src
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=src)
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.render.engine = 'BLENDER_EEVEE'
bpy.ops.object.camera_add(location=(6, -10, 14))
cam = bpy.context.object
target = Vector((5, 3, 0))
cam.rotation_euler = (target - cam.location).to_track_quat('-Z','Y').to_euler()
cam.data.type = 'ORTHO'
cam.data.ortho_scale = 16
scene.camera = cam
bpy.ops.object.light_add(type='AREA', location=(4, 3, 9))
bpy.context.object.data.energy = 2500
bpy.context.object.data.size = 8
scene.render.resolution_x = 1600
scene.render.resolution_y = 1100
scene.render.resolution_percentage = 100
scene.render.filepath = os.path.join(base, "apartment-preview-v002-2026-11-11.png")
out = os.path.join(base, "apartment-geometry-v002-2026-11-11.blend")
bpy.ops.wm.save_as_mainfile(filepath=out)
bpy.ops.render.render(write_still=True)
print("Created:", out)
# IMPORTANT: geometry is partially calibrated to drawings and is NOT construction-verified.

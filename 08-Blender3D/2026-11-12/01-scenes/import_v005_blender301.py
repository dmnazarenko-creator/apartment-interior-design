# Blender 3.0.1 — импорт исследовательской v005 (FreeCAD BREP + 5 перегородок)
# Скопируйте рядом файл apartment-shell-partitions-v005-2026-11-12.glb
# Запуск: blender --background --python import_v005_blender301.py
import bpy
import os
from mathutils import Vector
if bpy.app.version[:3] != (3, 0, 1):
    raise RuntimeError("Нужна Blender 3.0.1; текущая версия: %s" % str(bpy.app.version[:3]))
base = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base, "apartment-shell-partitions-v005-2026-11-12.glb")
if not os.path.isfile(src):
    raise FileNotFoundError(src)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=src)
scene = bpy.context.scene
scene.unit_settings.system='METRIC'
scene.render.engine='BLENDER_EEVEE'
bpy.ops.object.camera_add(location=(11,-13,16))
cam=bpy.context.object
target=Vector((-3.8,6.5,1.0))
cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler()
cam.data.type='ORTHO'
cam.data.ortho_scale=18
scene.camera=cam
bpy.ops.object.light_add(type='AREA',location=(-4,6,9))
bpy.context.object.data.energy=2500
bpy.context.object.data.size=9
scene.render.resolution_x=1600
scene.render.resolution_y=1100
scene.render.filepath=os.path.join(base,'apartment-preview-v005-2026-11-12.png')
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(base,'apartment-shell-partitions-v005-2026-11-12.blend'))
print("Файл сохранён; регистрация контуров пока предварительная.")

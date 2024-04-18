import bpy
import random

  


for atom in bpy.data.objects:
    if "_atom" in str(atom):    
        bpy.context.view_layer.objects.active = atom
        atom =bpy.context.object
        seed =random.uniform(1.0, 10.0)
        action = atom.animation_data.action
        for c in action.fcurves: 
            m = c.modifiers.new('NOISE')
            m.strength = .7
            m.phase = seed
   


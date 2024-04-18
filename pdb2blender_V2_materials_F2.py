import bpy
import math


draw_bonds = 0
shade_smooth = 1
make_pretty_flag = 1
change_alpha_flag = 0

def change_alpha():
    pass
    #for mat in bpy.data.materials:
    #    if not mat.use_nodes: continue
    #    if mat.blend_method == "OPAQUE":
    #        mat.blend_method = "HASHED"
    
    #for mat in bpy.data.materials:
    #    if not mat.use_nodes: continue
    #    for n in mat.node_tree.nodes:
    #        if n.type == 'BSDF_PRINCIPLED':
    #            if mat.blend_method == "HASHED":
    #                n.inputs["Alpha"].default_value = 1    
    
    ##this will key frame it as well
    #for mat in bpy.data.materials:
        #if not mat.use_nodes: continue
        #for n in mat.node_tree.nodes:
            #if n.type == 'BSDF_PRINCIPLED':
                #if mat.blend_method == "HASHED":
                    #imp = mat.node_tree.nodes["Principled BSDF"].inputs["Alpha"]
                    #imp.default_value = 0
                    #imp.keyframe_insert("default_value", frame = 1)    

def make_pretty():
    #carbon = bpy.data.materials.new('carbon')
    #carbon.use_nodes = True
    #carbon.diffuse_color = (0.142,0.142,0.142,1)
    
    #bonds = bpy.data.materials.new('bonds')
    #bonds.use_nodes = True
    #bonds.diffuse_color = (1.0,1.0,1.0,1)     
    
    for all_things in bpy.data.objects: 
        if "_atom" in str(all_things):
                     
            
            for poly in all_things.data.polygons:
                poly.use_smooth = True    
        
        if "Cylinder" in str(all_things):
                 
            
            for poly in all_things.data.polygons:
                poly.use_smooth = True      

def bond_between(x1, y1, z1, x2, y2, z2, bond_r):

    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1    
    dist = math.sqrt(dx**2 + dy**2 + dz**2)
  
    bpy.ops.mesh.primitive_cylinder_add(
        radius = bond_r, 
        depth = dist,
        location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)   
    ) 
  
    phi = math.atan2(dy, dx) 
    theta = math.acos(dz/dist) 
  
    bpy.context.object.rotation_euler[1] = theta 
    bpy.context.object.rotation_euler[2] = phi 
  
  

def add_atom(atomLoc_x, atomLoc_y, atomLoc_z, atom_type):
    #carbon atom
    if atom_type =="C" and draw_bonds != 1:
        atom_radius = .9
        atom_prefix = "C_atom"
    else:
        atom_radius = .7
        atom_prefix = "C_atom"
        
    if atom_type =="H": 
        atom_radius = .6
        atom_prefix = "H_atom"     
    
    
    if atom_type =="Ge":
        atom_radius = .95
        atom_prefix = "Ge_atom"
    elif atom_type =="O":
        atom_radius = .85
        atom_prefix = "O_atom"
    elif atom_type =="Si":
        atom_radius = 1.2
        atom_prefix = "Si_atom" 
    elif atom_type =="B":
        atom_radius = .95
        atom_prefix = "B_atom"
    elif atom_type =="N":
        atom_radius = .85
        atom_prefix = "N_atom"
    elif atom_type =="F":
        atom_radius = .75
        atom_prefix = "F_atom" 
    elif atom_type =="P":
        atom_radius = 1.05
        atom_prefix = "P_atom" 
    elif atom_type =="S":
        atom_radius = 1.2
        atom_prefix = "S_atom"
    elif atom_type =="Al":
        atom_radius = 1.5
        atom_prefix = "Au_atom"
    elif atom_type =="Br":
        atom_radius = 1.05
        atom_prefix = "I_atom"            
    
    
  
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=atom_radius, location=(atomLoc_x, atomLoc_y, atomLoc_z), rotation=(0.0, 0.0, 0.0))
    for obj in bpy.context.selected_objects:
        obj.name = str(atom_prefix) 
        if "C" in obj.name:
            mat = bpy.data.materials.get('carbon')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "Ge" in obj.name:
            mat = bpy.data.materials.get('germanium')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "H" in obj.name:
            mat = bpy.data.materials.get('hydrogen')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "O" in obj.name:
            mat = bpy.data.materials.get('oxygen')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "Si" in obj.name:
            mat = bpy.data.materials.get('silicon')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "B" in obj.name:
            mat = bpy.data.materials.get('boron')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "N" in obj.name:
            mat = bpy.data.materials.get('nitrogen')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat 
        elif "F" in obj.name:
            mat = bpy.data.materials.get('flourine')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat 
        elif "P" in obj.name:
            mat = bpy.data.materials.get('phosphorus')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "S" in obj.name:
            mat = bpy.data.materials.get('sulfur')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "I" in obj.name:
            mat = bpy.data.materials.get('iodine')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat
        elif "Au" in obj.name:
            mat = bpy.data.materials.get('gold')
            bpy.ops.object.material_slot_add()
            obj.data.materials[0] = mat               
    

#Create a list to store the xyz values of the atoms. 
AtomCoordinates = []  

#Blender file path
#C:\Users\Tom\Desktop\new tras\blender prototypes\atom models\molecules\norad_habst
#'C:\\Users\\Tom\Desktop\\new tras\\blender prototypes\\modeling\\build lonsdaleite\\lons hex.pdb'
#C:\Users\Tom\Desktop\new tras\old school mech syn\atomistic models
#file = open('C:\\Users\\Tom\Desktop\\new tras\\Movies\\Introduction to MechSyn Project\\tool tip models\\adamantane-thiol-AFM-tip3states.pdb', 'r')
file = open('C:\\Users\\Tom\Desktop\\mechsyn_animation\\lonsdaleite cage sequence\\lons repeat first row.pdb', 'r')


igot = file.readlines()

for line in igot:
    if line.find("ATOM   ") > -1:
                xyz =  line.split()
                atom_number = int(xyz[1])
                atom_type = str(xyz[2])
                atomLoc_x = float(xyz[5])
                AtomCoordinates.append(atomLoc_x)
                atomLoc_y = float(xyz[6])
                AtomCoordinates.append(atomLoc_y)
                atomLoc_z = float(xyz[7])
                AtomCoordinates.append(atomLoc_z)
                
               
                add_atom(atomLoc_x, atomLoc_y, atomLoc_z, atom_type)
                print(atom_number, atom_type, atomLoc_x, atomLoc_y, atomLoc_z)
                #print(AtomCoordinates)
                #print(len(AtomCoordinates))
                print('number of atoms = ', len(AtomCoordinates)/3)
                

if draw_bonds == 1:
    for line in igot:
        
        if line.find("CONECT ") > -1:
                    bonds =  line.split()
                    print(bonds)
                    connected_atoms = (len(bonds)-1) #minus one because the 'CONECT'statements
                    #print(connected_atoms) # could be 2 or 3 or 4
                    #print(bonds[1])
                    
                    #bonds[1] with be the starting atom for the bond. Its coordinates should be
                    x_bondStart = int(bonds[1])*3-3
                    y_bondStart = int(bonds[1])*3-2
                    z_bondStart = int(bonds[1])*3-1
                    
                    #print(AtomCoordinates[x_bondStart], AtomCoordinates[y_bondStart], AtomCoordinates[z_bondStart])
    
                    for bond_end_atom in range(2, len(bonds)):
                        #print('this is ',bond_end_atom)
                        
                        #print('atom number of the bond ending atom ' ,bonds[bond_end_atom])
                        
                        x_bondEnd = int(bonds[bond_end_atom])*3-3
                        y_bondEnd = int(bonds[bond_end_atom])*3-2
                        z_bondEnd = int(bonds[bond_end_atom])*3-1                    
                        
                        print('===========Starting coordinates of the bond===========')
                        print(AtomCoordinates[x_bondStart], AtomCoordinates[y_bondStart], AtomCoordinates[z_bondStart])
                        print('===========Ending coordinates of the bond===========')
                        print(AtomCoordinates[x_bondEnd], AtomCoordinates[y_bondEnd], AtomCoordinates[z_bondEnd])
                        print(" ")
                        
                        x1 = AtomCoordinates[x_bondStart]
                        y1 = AtomCoordinates[y_bondStart]
                        z1 = AtomCoordinates[z_bondStart]
                        x2 = AtomCoordinates[x_bondEnd]
                        y2 = AtomCoordinates[y_bondEnd]
                        z2 = AtomCoordinates[z_bondEnd]
                        bond_r = 0.1
                        print(x1, y1, z1, x2,y2,z2, bond_r)
                        bond_between(x1, y1, z1, x2, y2, z2, bond_r)
                        
else:
    pass
                    
if make_pretty_flag == 1:      
    make_pretty()
    print("making pretty")
else:
    pass

        
if change_alpha_flag ==1:
    change_alpha()
    print("setting material alpha values")
else:
    pass
                
    
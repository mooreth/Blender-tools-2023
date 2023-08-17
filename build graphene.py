import bpy
import math


build_graphene = 1
make_pretty_flag = 1
join_all = 0

def join():
    for ob in bpy.context.scene.objects:
        ob.select_set(True)
        bpy.ops.object.join()
    obj = bpy.context.object
    obj.name = "graphene sheet"
    

def make_pretty():
    
    carbon = bpy.data.materials.new('carbon')
    carbon.use_nodes = True
    carbon.diffuse_color = (0.142,0.142,0.142,1)
    
    bonds = bpy.data.materials.new('bonds')
    bonds.use_nodes = True
    bonds.diffuse_color = (1.0,1.0,1.0,1)     

    for all_things in bpy.data.objects: 
        if "C_atom" in str(all_things):
                     
            all_things.data.materials[0] = carbon 
            for poly in all_things.data.polygons:
                poly.use_smooth = True    
        
        if "Bond" in str(all_things):
                 
            all_things.data.materials[0] = bonds 
            for poly in all_things.data.polygons:
                poly.use_smooth = True          

def bond_between(loc0, loc1, atom1_name, atom2_name):
 
 
        x1 = loc0[0]
        y1 = loc0[1]
        z1 = loc0[2]
        
        x2 = loc1[0]
        y2 = loc1[1]
        z2 = loc1[2]  
        
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1    
        dist = math.sqrt(dx**2 + dy**2 + dz**2)
      
        bpy.ops.mesh.primitive_cylinder_add(
            radius = 0.01, 
            depth = dist,
            location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)   
        ) 
      
        phi = math.atan2(dy, dx) 
        theta = math.acos(dz/dist) 
      
        bpy.context.object.rotation_euler[1] = theta 
        bpy.context.object.rotation_euler[2] = phi 
        
        
        atom1_num = atom1_name.replace('_atom', ' ' )
        atom2_num = atom2_name.replace('_atom', ' ')
        #print(atom1_num,atom2_num)
        bond_name = "Bond "+str(atom1_num)+" and "+str(atom2_num) #this is new
        for obj_bond in bpy.context.selected_objects:
                obj_bond.name = bond_name
                bpy.ops.object.material_slot_add()


def start_bonding():
    bonds = {}
    
    #Sp2 carbon carbon bond length in graphene
    Sp2CC = 0.142  # 0.0462 is 3%
    Sp3CH = 1.09
    
    #Sp3 carbon carbon bond length
    Sp3CC = 1.54  # 0.0462 is 3%
    Sp3CH = 1.09
    
    
    #need to add all the atoms to the dictionary first
    for all_atoms in bpy.data.objects:
            if "atom" in str(all_atoms):
                    if 'C' in all_atoms.name:
                            bonds[all_atoms.name] = { 'valence':3, 'bond1':'0', 'bond2':'0', 'bond3':'0' }       
                            
                    elif 'H' in all_atoms.name:
                            bonds[all_atoms.name] = { 'valence':1, 'bond1':'0'}    
    
    
    
    for obj1 in bpy.data.objects:
            
            if "atom" in str(obj1):
                    if 'C' in obj1.name:
                            atom1 = 'C'
                            atom1_name = obj1.name
                           
                            
                    elif 'H' in obj1.name:
                            atom1 = 'H'
                            atom1_name = obj1.name
                            
                        
                   
                    #key:value pairs where the keys are valence, bond1, bond2.....
    
                    for obj2 in bpy.data.objects:
                            if "atom" in str(obj2) and obj1 != obj2:
                            
                                    #print(obj1, obj2)
                                    loc0 = obj1.matrix_world.translation
                                    loc1 = obj2.matrix_world.translation
                                    length = round((loc0 - loc1).length,4)
                                    #print(length) 
    
                                            
                                    if 'C' in obj2.name:
                                            atom2 = 'C'
                                            atom2_name = obj2.name
                                            
                                    elif 'H' in obj2.name:
                                            atom2 = 'H'
                                            atom2_name = obj2.name
                                    
                                    #print(obj1.name, length, obj2.name)
                                    
                                    
                                    ##CARBON
                                    if length >= 0.141 and length <=0.143 and atom1 == 'C' and atom2 == 'C':
                                            #print('good C-C bond found', obj1.name, length, obj2.name)
                                            num_bonds = bonds[obj1.name]['valence']
                                            
                                            for foo in range(1, num_bonds+1):
                                              ##print(foo)
                                              
                                                    bondnumber = "bond"+str(foo)
                                                    
                                                    if bonds[obj1.name][bondnumber] == '0':
                                                            bonds[obj1.name][bondnumber] = obj2.name
                                                            
                                                            break
                                              
                                             #before it draws the bond obj1 should look for itself listed in obj2's bonding record, if so don't draw the bond again 
    
                                            new_output = list(bonds[obj2.name].values())
                                            
                                            print("'''''''''''''''''''''''")
                                            print( "object 1 is", obj1.name, "object 2 is", obj2.name, new_output, "\n")
                                            if obj1.name in new_output:
                                                    print('bond already drawn')
                                                    pass
                                            else:
                                                    bond_between(loc0, loc1, atom1_name, atom2_name )
                                    
                                    ## HYDROGEN
                                    if length >= 1.08 and length <=1.09 and atom1 == 'H' and atom2 == 'C':
                                            
                                            num_bonds = bonds[obj1.name]['valence']
                                            
                                            for foo in range(1, num_bonds+1):
                                              ##print(foo)
                                              
                                                    bondnumber = "bond"+str(foo)
                                                    
                                                    if bonds[obj1.name][bondnumber] == '0':
                                                            bonds[obj1.name][bondnumber] = obj2.name
                                                            
                                                            break
                                              
                                             #before it draws the bond obj1 should look for itself listed in obj2's bonding record, if so don't draw the bond again 
    
                                            new_output = list(bonds[obj2.name].values())
                                            
                                            print("'''''''''''''''''''''''")
                                            print( "object 1 is", obj1.name, "object 2 is", obj2.name, new_output, "\n")
                                            if obj1.name in new_output:
                                                    print('bond already drawn')
                                                    pass
                                            else:
                                                    bond_between(loc0, loc1, atom1_name, atom2_name )    
    





###Build an arm chair sheet. If you rotate this by 90 degrees in Z it becomes a zig zag
if build_graphene == 1:

    sheet_width = 4 #nm THIS IS WHAT YOU CHANGE TO SET THE SIZE OF THE SHEET
    sheet_length = 4 # THIS IS WHAT YOU CHANGE TO SET THE SIZE OF THE SHEET
    
    horizontal_distance =0.245/2 #nm
    number_horizontal_cells =  sheet_width // horizontal_distance

    cell_length = 0.284 +.142 
    number_verticle_cells =  sheet_length // cell_length
    
    #print(number_horizontal_cells)
    print(number_verticle_cells)
    
    atom_radius = 0.03 #nm
    atom_prefix = "C_atom"
   
    #atomLoc_x = 0
    atomLoc_y = 0
    atomLoc_z = 0

    y_shift = 0

#for each of the y rows
    for y_rows in range(1,int(number_verticle_cells*2+1)):
        #print(y_rows)
        atomLoc_x = 0 #<-----X HAS TO ALTERNATE BETWEEN 0 AND -X SHIFT FACTOR
        for cells in range(1, int(number_horizontal_cells+2)):
           #if it is an odd y row
            #print(cells)
            #if cells == 0:
                #zig_factor = 0
                #x_shift = 0
            
            #if y is odd
            if y_rows % 2 != 0:
                x_shift = 0
                if cells % 2 == 0:
                    zig_factor = 0.071
                else:
                    zig_factor = 0
           #if it is an even y row 
            else:
                #x_shift = -.123
                if cells % 2 == 0:
                    zig_factor = -0.071
                else:
                    zig_factor = 0            
                
            bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=atom_radius, location=(atomLoc_x+x_shift, atomLoc_y+zig_factor+y_shift, atomLoc_z), rotation=(0.0, 0.0, 0.0)) #add the y shift to the y location
            for obj1 in bpy.context.selected_objects:
                obj1.name = str(atom_prefix)
                bpy.ops.object.material_slot_add()
            atomLoc_x = atomLoc_x + horizontal_distance
            
    #y shift = y shift +plus next increment
        if y_rows % 2 != 0:
            y_shift = y_shift- .142   
            print(y_shift)
        else:
            y_shift = y_shift-.284
            print(y_shift)
    
    start_bonding()
    if make_pretty_flag == 1:
        make_pretty()

if join_all == 1:
    join()

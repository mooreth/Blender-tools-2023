import bpy
import random 


rectangular_array = 0

x_shift = 0
y_shift = 0
side_length = 8 #0.8
sqr_3 = 1.73
x_center, y_center = 0,0



columns = 20
rows = 20

for y_rows in range(rows):
    print(y_rows)
    #if y is an odd row start it one shift to the left
    if y_rows % 2 != 0:
        x_shift = -9.8
    for x_columns in range(columns):
        #column is even
        if x_columns % 2 == 0 :
            z_rotation = 29.84
            y_zig = 0
            
            trimer_1_x, trimer_1_y = x_center, x_center +(sqr_3/3)*side_length
            
            trimer_2_x, trimer_2_y = x_center-(x_center-side_length/2) , x_center -(sqr_3/6)*side_length
            
            trimer_3_x, trimer_3_y = x_center-(x_center+side_length/2) , x_center -(sqr_3/6)*side_length        
               
        else:
            z_rotation = 1.57
            y_zig = 4.82
            trimer_1_x, trimer_1_y = x_center, x_center -(sqr_3/3)*side_length
            
            trimer_2_x, trimer_2_y = x_center+(x_center-side_length/2) , x_center +(sqr_3/6)*side_length
            
            trimer_3_x, trimer_3_y = x_center+(x_center+side_length/2) , x_center +(sqr_3/6)*side_length        
      
        if random.uniform(0, 1) <= 0.3:   
            bpy.ops.object.collection_instance_add(collection='c2 tool', align='WORLD', location=(trimer_1_x+x_shift, trimer_1_y + y_zig +y_shift, 0), rotation=(0, 0, z_rotation), scale=(1, 1, 1))
        else:
            bpy.ops.object.collection_instance_add(collection='h don tool', align='WORLD', location=(trimer_1_x+x_shift, trimer_1_y + y_zig +y_shift, 0), rotation=(0, 0, z_rotation), scale=(1, 1, 1))
        
        if random.uniform(0, 1) <= 0.3: 
            bpy.ops.object.collection_instance_add(collection='c2 tool', align='WORLD', location=(trimer_2_x+x_shift, trimer_2_y + y_zig +y_shift, 0), rotation=(0, 0, z_rotation), scale=(1, 1, 1))
        else:
            bpy.ops.object.collection_instance_add(collection='h don tool', align='WORLD', location=(trimer_2_x+x_shift, trimer_2_y + y_zig +y_shift, 0), rotation=(0, 0, z_rotation), scale=(1, 1, 1))
        bpy.ops.object.collection_instance_add(collection='c2 tool', align='WORLD', location=(trimer_3_x+x_shift, trimer_3_y + y_zig+y_shift, 0), rotation=(0, 0, z_rotation), scale=(1, 1, 1))  
        
        x_shift = x_shift + 9.8
    y_shift = y_shift - 16
    x_shift = 0
      

if rectangular_array == 1:
    
    #z will stay constanct
    starting_x = -10
    ending_x = 300
    starting_y = -10
    ending_y = 300
    
    padding = 10
    
    for x_cor in range(starting_x, ending_x, padding):
        for y_cor in range(starting_y, ending_y, padding):
            if random.uniform(0, 1) <= 0.9:
                if random.uniform(0, 1) <= 0.3:
                    bpy.ops.object.collection_instance_add(collection='h don tool', align='WORLD', location=(x_cor, y_cor, 0), rotation=(0, 0, 30), scale=(1, 1, 1))
                else:
                    bpy.ops.object.collection_instance_add(collection='c2 tool', align='WORLD', location=(x_cor, y_cor, 0), rotation=(0, 0, 30), scale=(1, 1, 1))


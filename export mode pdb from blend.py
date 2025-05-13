import bpy
f = open('C:\\Users\\moore\\OneDrive\\Desktop\\Blender Game Engine\\Get Closer\\model_export.pdb', "a") 
tag = "HETATM"
index = 1
for obj in bpy.data.objects:
    if obj.name == "Camera":
        break
    string_obj = str(obj)
    
    
    if "atom" in string_obj:   
        
        if "C_" in string_obj:
            element = "C"            
        else:
            element = "H"
        
        #print(atomType)
    xyz_data = obj.location
    xcor = round(xyz_data[0],2)
    ycor = round(xyz_data[1],2)
    zcor = round(xyz_data[2],2)
    
    record_name_len = 6
    record_name_pad = record_name_len - len(tag)
    
    serial_len = 5
    index_pad = serial_len - len(str(index)) 
    
    atom_name_len = 3
    atom_name_pad = atom_name_len - len(element)
    
    character = 1
    residue_name = 3
    
    chainID_len =   4
    chainID = "A" 
    chainID_pad = chainID_len - len(chainID)
    
    residue_sequence_num_len = 4
    residue_sequence_num = "1"
    residue_seqeunce_num_pad = residue_sequence_num_len- len(residue_sequence_num)
    
    iCode = 4
    
    x_len = 8
    x_len_pad = x_len - len(str(xcor))
    
    y_len = 8
    y_len_pad = y_len - len(str(ycor))        
    
    z_len = 8
    z_len_pad = z_len - len(str(zcor))        
   
    
    ##all text end at the rightside of its column allowance, so there wouldn't be padding on the right side, the left side padding just descreases and the string gets longer.
    pdb_line = record_name_pad *" " + tag +index_pad*" " +str(index) + atom_name_pad*" " + element + character*" " + residue_name* " " + chainID_pad*" " + chainID + residue_seqeunce_num_pad*" " + residue_sequence_num + iCode*" "+ x_len_pad*" "+ str(xcor) + y_len_pad*" "+ str(ycor) + z_len_pad*" "+ str(zcor) +"  1.00  0.00           "+ element       +"\n"
    print(obj.name)
    print(pdb_line, len(pdb_line))
    f.write(pdb_line) 
    index = index + 1
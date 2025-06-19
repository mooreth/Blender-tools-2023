insert_string = "  1.00 10.00           "

with open('C:\\Users\\Tom\\MolecularNodesCache\\insert.pdb', 'r') as file:    
        for lines in file:
                if lines.find("ATOM  ") > -1:
                        line_to_write = lines[:54] + insert_string + lines[54:]
                        print(line_to_write)
                        
                else:
                        line_to_write = lines
                with open('C:\\Users\\Tom\\MolecularNodesCache\\insert MN.pdb', 'a') as output_file:
                                output_file.write(line_to_write)                
                
                

        
        
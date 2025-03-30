def modify_file(input_filename, output_filename):
     input_filename = input("Enter the name of the file to read: ")
     output_filename = input("Enter the name of the file to write the modified content: ")
     try:
        # Open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()
        modified_content = content.upper()
    
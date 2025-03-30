def modify_file(input_filename, output_filename):
     input_filename = input("Enter the name of the file to read: ")
     output_filename = input("Enter the name of the file to write the modified content: ")
     try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            line_number = 1
            for line in infile:
                modified_line = f"{line_number}: {line}"
                outfile.write(modified_line)
                line_number += 1
        print(f"Successfully read '{input_filename}' and wrote the modified content to '{output_filename}'.")
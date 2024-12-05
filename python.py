def process_file():
    # Ask user for input and output filenames
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    
    try:
        # Read from input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify content (example: replacing text)
        modified_content = content.replace('old', 'new')
        
        # Write modified content to output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except IOError:
        print(f"Error reading or writing to files.")

# Call the function to run the program
process_file()

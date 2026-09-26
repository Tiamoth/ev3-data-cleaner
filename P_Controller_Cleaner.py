import re
import os

def clean_ev3_data(input_filename, output_filename):
    """
    Cleans and formats squashed EV3 data logging text files into 
    region-friendly CSV files so Excel can graph them easily.
    """
    print(f"Reading raw data from: {input_filename}...")
    
    try:
        with open(input_filename, 'r') as file:
            raw_data = file.read()
            
        # Insert a newline between the Turn value (ends in .\d) and the next Error value (- or \d)
        cleaned_data = re.sub(r'(,\s*-?\d+\.\d)(-|\d)', r'\1\n\2', raw_data)

        # Localize for regions using a comma as a decimal separator (like South Africa)
        # 1. Swap periods to a temporary placeholder
        cleaned_data = cleaned_data.replace('.', 'DECIMAL_PLACEHOLDER')
        # 2. Swap existing commas (delimiters) to semicolons
        cleaned_data = cleaned_data.replace(',', ';')
        # 3. Swap the temporary placeholder to commas
        cleaned_data = cleaned_data.replace('DECIMAL_PLACEHOLDER', ',')

        # Add the column headers for Excel
        final_csv = "Error;Turn\n" + cleaned_data

        # Save the new file
        with open(output_filename, 'w') as file:
            file.write(final_csv)
            
        print(f"Success! Cleaned data saved to: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'. Make sure it is inside your P_Data_Cleaning folder.")

if __name__ == "__main__":
    # Automatically find the exact folder this script is saved in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Attach the folder path directly to the file names
    input_file = os.path.join(script_dir, "Pdata.txt")
    output_file = os.path.join(script_dir, "Pdata_Cleaned.csv")
    
    clean_ev3_data(input_file, output_file)
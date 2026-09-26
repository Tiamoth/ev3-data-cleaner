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
            
        cleaned_data = re.sub(r'(,\s*-?\d+\.\d)(-|\d)', r'\1\n\2', raw_data)


        cleaned_data = cleaned_data.replace('.', 'DECIMAL_PLACEHOLDER')
    
        cleaned_data = cleaned_data.replace(',', ';')
   
        cleaned_data = cleaned_data.replace('DECIMAL_PLACEHOLDER', ',')

   
        final_csv = "Error;Turn\n" + cleaned_data

        with open(output_filename, 'w') as file:
            file.write(final_csv)
            
        print(f"Success! Cleaned data saved to: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'. Make sure it is inside your P_Data_Cleaning folder.")

if __name__ == "__main__":
   
    script_dir = os.path.dirname(os.path.abspath(__file__))
    

    input_file = os.path.join(script_dir, "Pdata.txt")
    output_file = os.path.join(script_dir, "Pdata_Cleaned.csv")
    
    clean_ev3_data(input_file, output_file)
# EV3 Data Logger Formatting Fix

A Python utility script that cleans and formats raw data streams logged by a LEGO Mindstorms EV3 robot into localized, Excel-ready CSV files for PID Controller analysis.

## The Problem
When logging high-speed sensor data (like PID tracking error and motor turn values) using the standard EV3 graphical blocks, two formatting issues happen:
1. **Squashed Data Lines:** The EV3 outputs a continuous, unbroken string of data (like `-12.48,-31.2-18.72,-31.2`). This makes it impossible for Excel to separate the rows.
2. **Regional Decimal Clashes:** The EV3 outputs decimal numbers using a period (`41.5`). However, Excel installations in regions like South Africa expect a comma for decimals (`41,5`). This causes Data Type errors.

## The Solution (Full Workflow)
This repository contains the Python script to fix the data, as well as the original `.ev3` project file so you can see exactly how the hardware was programmed.

### 1. The EV3 Logic
In the provided `.ev3` file, you will see two key steps:
* **File Cleanup:** A `File Access` block is used to *delete* the old `Pdata` file before the main loop starts. This ensures we don't accidentally append new test data to an old run.
  *(Insert image_cff7e5.png here)*
* **Data Merging:** Inside the loop, the Error and Turn math blocks are wired into a `Text - Merge` block (separated by a comma), which feeds directly into the `File Access` write block.
  *(Insert image_cff83c.png here)*

### 2. Log the Data
Run the robot on the track for a short distance to capture a few corners, then stop the program. Extract the logged `.rtf` file using the EV3 Memory Browser and save it to your PC as a `.txt` file (e.g., `Pdata.txt`).

### 3. Run the Script
Place `clean_p_data.py` into the same folder as your text file and run it. The script uses Regex to automatically fix the squashed numbers, swap the decimals, and produce a clean `.csv` file.

```bash
python clean_p_data.py
```

### 4. Graph in Excel
Open the new `.csv` file in Excel. The data will be perfectly split into "Error" and "Turn" columns, allowing you to instantly generate performance graphs.

## Results
Below is the final line graph generated in Excel using the cleaned CSV data. It clearly visualizes the physical oscillation (hunting) of the P-controller.
*(Insert your Excel Line Graph image here)*

## Example Data
**Raw EV3 Output (`Pdata.txt`):**
```text
-12.48,-31.2-18.72,-31.2-28.08,-31.2-37.44,-31.2
```

**Cleaned Output (`Pdata_Cleaned.csv`):**
```text
Error;Turn
-12,48;-31,2
-18,72;-31,2
-28,08;-31,2
-37,44;-31,2
```

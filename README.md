# Small_Pivots

## Overview

This Python script processes financial time series data to identify specific pivot points in the data. These pivots are marked in the DataFrame with labels 'SPL' (Support Pivot Low) and 'SPH' (Support Pivot High). The script reads the data from a CSV file, processes it to identify these pivots, and then exports the processed data to a new CSV file.

## Requirements

- Python 3.x
- pandas

To install the required package, run:

```bash
pip install pandas
```

## How It Works

### 1. Input Data

The script reads input data from a file named `Sample_input.txt`. This file is expected to be a CSV file with a semicolon (`;`) delimiter. The columns of this file should be:

- `DATE & TIME`: The date and time of the record.
- `OPEN`: The opening price.
- `HIGH`: The highest price.
- `LOW`: The lowest price.
- `CLOSE`: The closing price.
- `VOLUME`: The volume of trades.
- `SPL`: Placeholder for Support Pivot Low (initially set to `None`).
- `SPH`: Placeholder for Support Pivot High (initially set to `None`).

### 2. Data Processing

- **Read the Data**: The script reads the input data into a pandas DataFrame and parses the `DATE & TIME` column as a datetime object.
  
- **Drop VOLUME Column**: The `VOLUME` column is dropped as it is not used in the pivot point calculation.

- **Check Pivot Function**: The `check_pivot` function iterates over the DataFrame rows to identify pivot points:
  
  - If a row's `HIGH` value is lower than the next two rows' `HIGH` values and its `CLOSE` value is lower than the next two rows' `CLOSE` values, the row is marked as 'SPL'.
  
  - Conversely, if a row's `LOW` value is higher than the next two rows' `LOW` values and its `CLOSE` value is higher than the next two rows' `CLOSE` values, the row is marked as 'SPH'.
  
  - The function uses a toggle mechanism to alternate between identifying 'SPL' and 'SPH' points.

### 3. Output Data

The processed DataFrame is printed to the console and also saved to a CSV file named `sample_input.csv`.

## How to Run

1. Place your input data in a file named `Sample_input.txt` with the correct format.
2. Run the script.
3. The output will be saved in a file named `sample_input.csv`.

## Example

If your `Sample_input.txt` looks like this:

```
2023-08-30 09:00;100;110;90;105;5000
2023-08-30 10:00;105;115;95;110;6000
2023-08-30 11:00;110;120;100;115;7000
```

The script will process this data and output a `sample_input.csv` with pivot points marked in the `SPL` and `SPH` columns.

## Notes

- The script assumes that the data is in a specific format and that the columns are properly aligned. Ensure that your data matches the expected format to avoid errors.
- The script does not currently handle edge cases, such as fewer than three rows of data.

---

This README provides an overview of the script's functionality, how it works, and how to run it. Modify the input data and adjust the script as needed for your specific use case.

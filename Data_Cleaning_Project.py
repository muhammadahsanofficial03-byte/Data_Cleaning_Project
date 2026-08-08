import pandas as pd
import logging
import os

# Configure logging to show progress in the terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_ecommerce_data(input_filename, output_filename):
    """
    Loads raw Excel data, cleans it, and exports to a CSV file.
    """
    try:
        logging.info(f"Loading raw dataset from '{input_filename}'...")
        # Load the specific sheet seen in the video
        df = pd.read_excel(input_filename, sheet_name='Dataset for Data Analytics')
        
        initial_row_count = len(df)
        logging.info(f"Successfully loaded {initial_row_count} rows.")

        # --- STEP 1: Handle Missing Values ---
        logging.info("Filling missing values...")
        df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')
        df['TrackingNumber'] = df['TrackingNumber'].fillna('PENDING_TRACKING')
        
        # Drop rows missing crucial identifiers (Order ID, Customer ID, Date)
        df.dropna(subset=['OrderID', 'CustomerID', 'Date'], inplace=True)

        # --- STEP 2: Remove Duplicates ---
        logging.info("Removing duplicate records...")
        df.drop_duplicates(inplace=True)

        # --- STEP 3: Standardize Data Types ---
        logging.info("Converting data types...")
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Ensure numerical columns are treated as numbers (floats)
        numeric_columns = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # --- STEP 4: Format Text Data ---
        logging.info("Standardizing text formatting...")
        categorical_columns = ['Product', 'PaymentMethod', 'OrderStatus', 'ReferralSource']
        for col in categorical_columns:
             if col in df.columns:
                # Convert to Title Case and remove accidental leading/trailing spaces
                df[col] = df[col].astype(str).str.title().str.strip()

        # --- STEP 5: Validate Financial Calculations ---
        logging.info("Checking TotalPrice calculations...")
        expected_total = df['Quantity'] * df['UnitPrice']
        # Flag discrepancies greater than 5 cents to account for minor floating-point math errors
        mismatches = abs(df['TotalPrice'] - expected_total) > 0.05
        if mismatches.any():
            logging.warning(f"Found {mismatches.sum()} rows where TotalPrice != Quantity * UnitPrice.")

        # --- STEP 6: Export Cleaned Data ---
        logging.info(f"Saving cleaned dataset to '{output_filename}'...")
        df.to_csv(output_filename, index=False)
        
        final_row_count = len(df)
        rows_dropped = initial_row_count - final_row_count
        logging.info(f"Done! {rows_dropped} rows removed. Cleaned data contains {final_row_count} rows.")

    except FileNotFoundError:
        logging.error(f"Error: Could not find '{input_filename}'. Please ensure it is in the same folder as this script.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure your raw video file is named exactly this and placed in the same folder
    INPUT_FILE = 'raw_sales_data.xlsx' 
    OUTPUT_FILE = 'cleaned_sales_data.csv'
    
    clean_ecommerce_data(INPUT_FILE, OUTPUT_FILE)
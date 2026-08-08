# E-Commerce Data Cleaning Pipeline

## 📝 Overview
This repository contains a robust Python pipeline designed to clean and standardize raw e-commerce sales data. Built in reference to the **DecodeLabs Data Cleaning Project.mp4** file, this script leverages the `pandas` library to transform a messy Excel spreadsheet into a structured, analysis-ready CSV file. 

The pipeline automates critical data preprocessing steps, including missing value imputation, deduplication, text standardization, and financial validation, ensuring the output is perfectly primed for accurate analytics and dashboarding.

---

## ✨ Features & Cleaning Operations
This script performs the following automated operations on the raw dataset:

*   **Missing Value Handling:** Intelligently imputes missing marketing codes (`CouponCode`) and tracking numbers with default placeholders. Drops rows missing critical identifiers (Order ID, Customer ID, Date) to maintain strict data integrity.
*   **Deduplication:** Scans the dataset to identify and remove identical duplicate records.
*   **Data Type Casting:** Standardizes the `Date` column into uniform datetime objects and ensures all financial columns (`UnitPrice`, `TotalPrice`) are accurately processed as numeric floats.
*   **Text Standardization:** Normalizes categorical text columns (e.g., `Product`, `PaymentMethod`, `OrderStatus`) to Title Case and strips accidental whitespace to prevent grouping errors in future analytics.
*   **Financial Validation:** Cross-checks financial accuracy by verifying that `TotalPrice` equals `Quantity` multiplied by `UnitPrice`. It logs warnings in the terminal if any mathematical discrepancies are detected.

---

## 🛠️ Prerequisites
To run this project, you will need Python 3.8+ installed on your machine. The script relies on the following Python libraries:
*   `pandas` (for data manipulation)
*   `openpyxl` (for reading `.xlsx` files)

You can install the required dependencies using pip:
```bash
pip install pandas openpyxl

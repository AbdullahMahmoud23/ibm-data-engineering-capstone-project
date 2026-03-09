#!/bin/bash

# ==============================================================================
# Script Name: datadump.sh
# Description: Exports the sales_data table to a file named sales_data.sql
# ==============================================================================

# Define the output file
OUTPUT_FILE="sales_data.sql"

# Define database credentials (update these with your actual details)
DB_USER="root"
DB_NAME="sales"

echo "Starting export of sales_data table to $OUTPUT_FILE..."

mysqldump -u "$DB_USER" -p "$DB_NAME" sales_data > "$OUTPUT_FILE"


# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Export successful! Data saved to $OUTPUT_FILE."
else
    echo "Error: Failed to export the table. Please check your credentials and database name."
fi
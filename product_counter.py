import os
import csv
from collections import Counter

# List of the main directories to scan
directories_to_scan = ['fine_train', 'fine_test', 'fine_val']

# A Counter object to hold the grand total for each product
grand_total_counts = Counter()

# Main loop to iterate through all specified directories
for directory in directories_to_scan:
    current_counts = {}
    print(f"\n--- Scanning Directory: '{directory}' ---")
    
    if not os.path.isdir(directory):
        print(f"WARNING: Directory '{directory}' not found. Skipping.")
        continue

    for product_folder in os.listdir(directory):
        path = os.path.join(directory, product_folder)
        
        if os.path.isdir(path):
            num_files = len(os.listdir(path))
            current_counts[product_folder] = num_files
            grand_total_counts[product_folder] += num_files
            
    if current_counts:
        # Print the summary for the current directory
        total_images_in_dir = sum(current_counts.values())
        print(f"Summary for '{directory}': Found {len(current_counts)} product types with {total_images_in_dir} total photos.")
    else:
        print("No product folders found in this directory.")

# --- Overall Report and CSV Export ---
print("\n" + "="*45)
print("     OVERALL DATASET REPORT & CSV EXPORT")
print("="*45)

if not grand_total_counts:
    print("\nNo data was found to export.")
else:
    # Print final summary to the console
    overall_total_images = sum(grand_total_counts.values())
    print(f"\nGrand Summary:")
    print(f"Total Unique Product Types: {len(grand_total_counts)}")
    print(f"Total Photos in Entire Dataset: {overall_total_images}")

    # --- Export to CSV File ---
    csv_file_name = 'product_counts_report.csv'
    print(f"\nExporting final report to '{csv_file_name}'...")

    try:
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            # Define the header
            header = ['Product', 'Total_Count']
            csv_writer = csv.writer(csvfile)
            
            # Write the header row
            csv_writer.writerow(header)
            
            # Write the data rows, sorted alphabetically by product name
            for product, total_count in sorted(grand_total_counts.items()):
                csv_writer.writerow([product, total_count])

        print(f"✅ Successfully exported the report.")

    except IOError:
        print(f"❌ Error: Could not write to the file {csv_file_name}.")
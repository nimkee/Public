#   Here is the GPT generated code -- the for loop is what I am looking for


import csv
from datetime import datetime

# Define the start and end dates for the 10-year period
start_date = datetime(2010, 1, 1)
end_date = datetime(2019, 12, 31)

# Open the CSV file and filter rows within the desired period
with open('weather_data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Read the header row
    header = next(csv_reader)

    # Print the header row or process it as needed
    print("Header:", header)

    # Iterate through the remaining rows
    for row in csv_reader:
        # Assuming the date is in the first column (modify as needed)
        date_str = row[0]
        date = datetime.strptime(date_str, '%Y-%m-%d')  # Parse date string to datetime object

        # Check if the date falls within the desired 10-year period. Use en ELIF block to catch the second date range
        if start_date <= date <= end_date:
            # Print or process the row as needed
            print("Date:", date_str, "Data:", row)

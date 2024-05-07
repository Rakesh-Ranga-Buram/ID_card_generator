import fpdf
import csv
import os

# Create a new PDF document
pdf = fpdf.FPDF(unit='in', format='Letter')
pdf.set_auto_page_break(auto=True, margin=0.5)

# Set the ID template image
id_template = './id.png'

# Open the CSV file and read its header row
with open('Employee_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames

    # Loop through each row in the CSV file
    for row in reader:
        # Set the employee's name, position, and photo path
        name = row['Name']
        position = row['Position']
        photo_path = row['Photo']

        # Add a new page to the PDF document
        pdf.add_page()

        # Add the ID template image to the page
        pdf.image(id_template, 0, 0, 6.5, 4)

        # Add the employee's name and position to the page
        pdf.set_font('Arial', 'B', 24)
        pdf.text(2.5, 3.5, name)

        pdf.set_font('Arial', '', 16)
        pdf.text(2.5, 3.8, position)

        # Add the employee's photo to the page
        pdf.image(photo_path, 4, 0.6, 1.5, 2, type='JPG')

# Save the PDF document to a file
pdf.output('employee_ids.pdf')
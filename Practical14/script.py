import xml.etree.ElementTree as ET
import openpyxl

# Parse the XML document
tree = ET.parse('go_obo.xml')
root = tree.getroot()

# Create an Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write headers
worksheet['A1'] = 'GO id'
worksheet['B1'] = 'Term Name'
worksheet['C1'] = 'Definition String'
worksheet['D1'] = 'Number of Child Nodes'

row = 2  # Start writing data from row 2

# Find all occurrences of 'autophagosome' in the <defstr> element
for term in root.iter('term'):
    term_id = term.find('id').text
    term_name = term.find('name').text
    def_str = term.find('def/defstr').text

    # Check if the def_str contains 'autophagosome'
    if 'autophagosome' in def_str:
        # Write data to the spreadsheet
        worksheet['A' + str(row)] = term_id
        worksheet['B' + str(row)] = term_name
        worksheet['C' + str(row)] = def_str

        # Count the number of child nodes
        child_count = sum(1 for _ in term.findall('.//is_a'))
        worksheet['D' + str(row)] = child_count

        row += 1

# Save the workbook
workbook.save('autophagosome.xlsx')

import xml.etree.ElementTree as ET

serial_number = ""
station_id = ""
operator = ""
uut_result = ""
test_type = ""
uut_part = ""
i = 0

tree = ET.parse('Report[P200005 3-2 final][11 39 23 AM][1 27 2020].xml')
root = tree.getroot()
xmlstr = ET.tostring(root, encoding='utf8', method='xml')

root = ET.fromstring(xmlstr)
# print(root)
# print(type(root))

# print(root[0][0][0][0].text)


for report in root:  # parsing into first <Report> layer under <Reports>
    #print(report.tag, report.attrib)
    for prop in report: # parsing into parent list of <Prop>
        if prop[0].get('Name') == 'SerialNumber':
            serial_number = prop[0][0].text
            print(f"Serial Number: {serial_number}")
        elif prop.get('Name') == 'StationInfo':
            station_id = prop[0][0].text
            print(f"Station ID: {station_id}")
            operator = prop[0][1].text
            print(f"Operator: {operator}")

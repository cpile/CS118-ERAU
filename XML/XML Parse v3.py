import xml.etree.ElementTree as ET
import os


# C:\Users\pilecd\Desktop\XML\Report[P200005 3-2 final][11 39 23 AM][1 27 2020].xml
# tree = ET.parse('Report[P200005 3-2 final][11 39 23 AM][1 27 2020].xml')
# tree = ET.parse('Report[S200001 RMR 2-1 cold][10 33 24 AM][2 10 2020].xml')
# tree = ET.parse('Report[S200001][5 51 04 AM][2 10 2020].xml')
# tree = ET.parse('Report[S200020 4-2 cold][3 36 28 PM][1 29 2020].xml')
# tree = ET.parse('Report[S200020 4-2 pre][12 04 48 PM][1 29 2020].xml')

def get_serial_number(root):
    for reports in root:
        for report in reports:  # parsing into parent list of <Prop>
            if report.get('Name') == 'UUT':
                for prop in report:
                    if prop.get('Name') == 'SerialNumber':
                        return prop[0].text


def get_station_id(root):
    for reports in root:
        for report in reports:
            if report.get('Name') == 'StationInfo':
                for prop in report:
                    if prop.get('Name') == 'StationID':
                        return prop[0].text


def get_operator(root):
    for reports in root:
        for report in reports:
            if report.get('Name') == 'StationInfo':
                for prop in report:
                    if prop.get('Name') == 'LoginName':
                        return prop[0].text


def get_uut_result(root):
    for report in root:
        return report.get('UUTResult')


def get_test_type(root):
    for report in root:
        return report.get('Type')


def get_uut_part(root):
    for reports in root:
        for report in reports:
            if report.get('Type') == 'TEResult':
                for prop in report:
                    if prop.get('Name') == 'TS':
                        for subprop in prop:
                            if subprop.get('Name') == 'SequenceCall':
                                for subsubprop in subprop:
                                    if subsubprop.get('Name') == 'ResultList':
                                        for values in subsubprop:
                                            if values.get('ID') == '[0]':
                                                for results in values:
                                                    if results.get('Type') == 'TEResult':
                                                        for parts in results:
                                                            if parts.get('Name') == 'ReportText':
                                                                x = parts[0].text
                                                                y = x.replace('<b>', '\'')
                                                                y = y.replace('</b>', '')
                                                                y = y.replace('\n', '')
                                                                z = y.split("'")
                                                                return z[2]


def main():
    while True:  # asks user for XML file path then verifies it is an XML file before opening
        xmlfile = input("Enter XML file path: ")
        if os.path.isfile(xmlfile):
            with open(xmlfile, 'r') as fh:
                tree = ET.parse(fh)
                root = tree.getroot()
            break

    serial_number = get_serial_number(root)
    test_type = get_test_type(root)
    uut_result = get_uut_result(root)
    station_id = get_station_id(root)
    operator = get_operator(root)
    uut_part = get_uut_part(root)

    print(f"Test Type: {test_type}")
    print(f"UUT Result: {uut_result}")
    print(f"Serial Number: {serial_number}")
    print(f"Station ID: {station_id}")
    print(f"Operator: {operator}")
    print(uut_part)


if __name__ == '__main__':
    main()

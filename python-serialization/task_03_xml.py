#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data to.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Parameters:
        filename (str): The XML file to read from.

    Returns:
        dict: A dictionary representation of the XML data.
    """

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            text = child.text
            if text is None:
                result[child.tag] = None
            elif text.isdigit():
                result[child.tag] = int(text)
            else:
                try:
                    result[child.tag] = float(text)
                except ValueError:
                    result[child.tag] = text
        return result
    except Exception as e:
        print(f"Error reading XML: {e}")
        return {}


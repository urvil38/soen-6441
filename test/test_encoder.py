import csv
from io import StringIO
import xml.etree.ElementTree as ET
import unittest
from typing import List, Tuple
from src.encoder import generate_xml_response, generate_csv_response


class TestGenerateXMLResponse(unittest.TestCase):

    def test_generate_xml_response(self):

        # Set up test data
        initial_guess = 1.0
        alpha = 0.5
        records = [(2.0, 3.0), (4.0, 5.0), (6.0, 7.0)]

        # Call the function
        xml_str = generate_xml_response(initial_guess, alpha, records)

        # Parse the XML string to an ElementTree object
        root = ET.fromstring(xml_str)

        # Assert the root element is named "result"
        self.assertEqual(root.tag, "result")

        # Assert there is one "input" element
        input_elems = root.findall("./input")
        self.assertEqual(len(input_elems), 1)

        # Assert the "alpha" element is correct
        alpha_elems = root.findall("./input/alpha")
        self.assertEqual(len(alpha_elems), 1)
        self.assertEqual(alpha_elems[0].get(
            "initial_guess"), str(initial_guess))
        self.assertEqual(alpha_elems[0].text, str(alpha))

        # Assert there is one "output" element
        output_elems = root.findall("./output")
        self.assertEqual(len(output_elems), 1)

        # Assert there is one "record" element for each record
        record_elems = root.findall("./output/record")
        self.assertEqual(len(record_elems), len(records))

        # Assert each "record" element has a "radius" and "length" element with the correct values
        for i, record_elem in enumerate(record_elems):
            radius = records[i][0]
            length = records[i][1]
            radius_elem = record_elem.find("./radius")
            length_elem = record_elem.find("./length")
            self.assertEqual(float(radius_elem.text), radius)
            self.assertEqual(float(length_elem.text), length)


class TestGenerateCSVResponse(unittest.TestCase):

    def test_generate_csv_response(self):

        # Set up test data
        alpha = 0.5
        records = [(2.0, 3.0), (4.0, 5.0), (6.0, 7.0)]

        # Call the function
        csv_str = generate_csv_response(alpha, records)

        # Parse the CSV string into a list of lists
        rows = [row for row in csv.reader(StringIO(csv_str))]

        # Assert the CSV header is correct
        self.assertEqual(rows[0], ['alpha', 'radius', 'length'])

        # Assert there is one row for each record, plus the header row
        self.assertEqual(len(rows), len(records) + 1)

        # Assert each row has the correct values
        for i, row in enumerate(rows[1:]):
            radius = records[i][0]
            length = records[i][1]
            self.assertEqual(float(row[0]), alpha)
            self.assertEqual(float(row[1]), radius)
            self.assertEqual(float(row[2]), length)

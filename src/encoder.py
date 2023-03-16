import xml.dom.minidom
import csv
from io import StringIO
from typing import Tuple, List


def generate_xml_response(
        initial_guess: float,
        alpha: float,
        records: List[Tuple[float, float]]) -> str:
    """
    Generates an XML response from the provided initial_guess, alpha, and records

    Args:
        initial_guess (float): The initial guess value
        alpha (float): The alpha value
        records (List[Tuple[float,float]]): A list of tuples representing the radius 
        and length of each record

    Returns:
        str: An XML string containing the provided data, formatted using 
        a Document Object Model (DOM)
    """
    # Get a DOMImplementation object
    impl = xml.dom.minidom.getDOMImplementation()

    # Create a DocumentType object
    dtd = impl.createDocumentType("result", None, "cheers.dtd")

    # Create a Document object
    doc = impl.createDocument(None, 'result', dtd)

    # Create an Element object for the root element
    root = doc.documentElement

    # Create the input element
    input_elem = doc.createElement('input')
    root.appendChild(input_elem)

    # Create the alpha element
    alpha_elem = doc.createElement('alpha')
    alpha_elem.setAttribute('initial_guess', str(initial_guess))
    alpha_elem.appendChild(doc.createTextNode(str(alpha)))
    input_elem.appendChild(alpha_elem)

    # Create the output element
    output_elem = doc.createElement('output')
    root.appendChild(output_elem)

    # Create a record element for each record
    for record in records:
        record_elem = doc.createElement('record')
        output_elem.appendChild(record_elem)

        radius_elem = doc.createElement('radius')
        radius_elem.appendChild(doc.createTextNode(str(record[0])))
        record_elem.appendChild(radius_elem)

        length_elem = doc.createElement('length')
        length_elem.appendChild(doc.createTextNode(str(record[1])))
        record_elem.appendChild(length_elem)

    # Pretty print the XML document
    xml_str = doc.toprettyxml(indent='  ', encoding='UTF-8').decode('UTF-8')

    return xml_str


def generate_csv_response(alpha: float, records: List[Tuple[float, float]]) -> str:
    """
    Generates a CSV response string with alpha, radius, and length columns.

    Args:
        alpha: A float representing the alpha value.
        records: A list of tuples containing the radius and length values.

    Returns:
        A string representing the CSV data.
    """
    output = StringIO()

    # create a csv writer object with the StringIO as output
    writer = csv.writer(output)

    # write the CSV header
    writer.writerow(['alpha', 'radius', 'length'])

    # write the data rows
    for row in records:
        writer.writerow([alpha, row[0], row[1]])

    # return the CSV data as a string
    return output.getvalue()

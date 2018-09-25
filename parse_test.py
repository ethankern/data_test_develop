import unittest
from parse import return_text, get_data
import xml.etree.ElementTree as ET

tree = ET.parse("BoojCodeTest.xml")
root = tree.getroot()

class ParsingTestCase(unittest.TestCase):

          def setUp(self):
                    pass

          def tearDown(self):
                    pass

          def test_return_text(self):

                    textreturn = return_text(root)          # Searches tree for some child with
                                                            # tag "DateListed" and returns its text.

                    self.assertEqual(type(textreturn), str) # Return value should be a string.

          def test_types(self):

                    row = get_data(root, 200)               # Gets data for a row in the CSV file.

                    self.assertEqual(type(row), list)       # Each row it returns should be a list.

          def test_empty(self):

                    emptyfield = get_data(root.find('.//Rooms'), 200)  # Stores data from element that
                                                                       # should return 'None' into our
                                                                       # field/row.
                    for item in emptyfield:

                              self.assertEqual(item, 'None')


if __name__ == "__main__":
          unittest.main()

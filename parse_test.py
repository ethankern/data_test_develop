import unittest
from parse import return_text, get_data
import xml.etree.ElementTree as ET

tree = ET.parse("BoojCodeTest.xml")
root = tree.getroot()

class ParsingTestCase(unittest.TestCase):

          def setUp(self):
                    pass


          def test_(self):

                    textreturn = return_text(root) # Searches tree for some child with
                                                   # tag "DateListed" and returns its text.
                                                    
                    self.assertEqual(type(textreturn), str) # Return value should be a string.


if __name__ == "__main__":
          unittest.main()

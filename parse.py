import csv
import requests
import xml.etree.ElementTree as ET

# Get xml data using requests.
URL = "http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml"
response = requests.get(URL)

# Open xml file and write requests content to it.
with open('BoojCodeTest.xml', 'wb') as file:
          file.write(response.content)
          
# Open a csv file and create csv writer object.
Test_data = open('TestData.csv', 'w')
csvwriter = csv.writer(Test_data)

# Create ElementTree object to find and parse xml data.
tree = ET.parse("BoojCodeTest.xml")
root = tree.getroot()


          # Function takes a listing (ET.Element object) and returns string
          # containing what we want to sort the listings by.
          # Need this as the key for sorting by date or by anything else.
def return_text(listing):
                                        # Can change DateListed to whatever child tag
                                        # we want to sort by.
          return listing.find('.//DateListed').text

          # Function takes a listing argument and returns a row
          # (a list) of items to be written to a csv.
def get_data(listing):
          
          row = []            # Row to be populated by each listing and written to csv.

          for field in header:          # Iterate the data search for every desired field.
                    
                    ETfield = listing.find('.//' + str(field))        # Element object in the tree
                                                                      # containing our field's data.
                    
                    try:                # Add the element's text to the row, up to 200 chars.
                              
                              row.append(ETfield.text[:200])
                              
                    except (TypeError, AttributeError):     # If the element has no data, we need
                                                            # to search its children.
                                                            # We raise errors for trying to index or
                                                            # call a method from a NoneType object.
                              try:
                                        fieldlist = []      # Create a secondary list for this field.
                                        for child in ETfield.getchildren():     # Put each child's data
                                                  fieldlist.append(child.text)  # into this list.
                                        row.append(fieldlist)
                                        
                              except:
                                        row.append('None')
                                        
          return row
                                                  

# Write csv header row.
header = ['MlsId','MlsName','DateListed','StreetAddress','Price','Bedrooms','Bathrooms','Appliances','Rooms','Description']
csvwriter.writerow(header)


# Main function:
                                        # Iterate search over each Listing element in the tree,
                                        # and sort by the tag's text (a string) defined in return_text().
for listing in sorted(root.findall('Listing'), key=return_text):
                                                  # Only want descriptions containing the word 'and',
                                                  # and only listings posted in 2016.
          if ' and ' in listing.find('.//Description').text and '2016' in listing.find('.//DateListed').text:
          
                                                  # Search each desired tag for child elements 
                                                  # and add their text to the row.
                    row = get_data(listing)
          
                    csvwriter.writerow(row)



Test_data.close()

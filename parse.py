# parse.py
# Parses a target XML document and writes 
# its data to an organized CSV file.
#
# Ethan Kern
# 24Sept2018

import csv
import re
import requests
import xml.etree.ElementTree as ET

# URL of target XML file.
URL = "http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml"

# Our desired fields that we want to find data for.
# (These strings must match the XML tags exactly.)
# This will be written as the first row in the CSV file.
header = ['MlsId','MlsName','DateListed','StreetAddress','Price','Bedrooms','Bathrooms','Appliances','Rooms','Description']

# Our desired cutoff for string data.
charlimit = 200



          # Function takes a listing (ET.Element object) and returns string
          # containing what we want to sort the listings by.
          # Need this as the key for sorting by date or by anything else.
def return_text(listing):
                                        # Can change DateListed to whatever child tag
                                        # we want to sort by.
          return listing.find('.//DateListed').text

          # Function takes a listing argument and returns a row
          # (a list) of items to be written to a csv.
def get_data(listing, charlimit):
          
          row = []            # Row to be populated by each listing and written to csv.

          for field in header:          # Iterate the data search for every desired field.
                    
                    ETfield = listing.find('.//' + str(field))        # Element object in the tree
                                                                      # containing our field's data.
                    
                    try:                
                              if not re.search(r'\w', ETfield.text):  # If the element's text doesn't
                                        raise AttributeError          # have any alphanumeric chars.
                                        
                              row.append(ETfield.text[:charlimit])    # Add the element's text to the
                                                                      # row, up to a desired cutoff.
                              
                    except (TypeError, AttributeError):     # If the element has no data, we need
                                                            # to search its children.
                                                            # We raise errors for trying to index or
                                                            # call a method from a NoneType object.
                              try:
                                        fieldlist = []      # Create a secondary list for this field.
                                        for child in ETfield.getchildren():     # Put each child's data
                                                  fieldlist.append(child.text)  # into this list.
                                        
                                        if not fieldlist:   # Checking the child elements for
                                                            # empty data.
                                                  raise AttributeError
                                        
                                        row.append(fieldlist)
                                        
                              except AttributeError:        # If the element has no children,
                                                            # find its "siblings" whose tags
                                                            # are similar.
                                        try:
                                                  fieldlist = []
                                                                      # Use Xpath to get list of siblings.
                                                  for child in listing.find('.//' + str(field) + '/..').getchildren():
                                                            
                                                                                          # If a sibling uses our
                                                                                          # desired field's name.
                                                            if str(field) in child.tag and str(field) != child.tag:
                                                                      
                                                                      fieldlist.append(child.tag + ': ' + str(child.text))
                                                  row.append(fieldlist)
                                        except:
                                                  row.append('None')
                                        
          return row


################
# Main function:
################

# Get xml data using requests.
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

# Write csv header row.
csvwriter.writerow(header)

                                        # Iterate search over each Listing element in the tree,
                                        # and sort by the tag's text (a string) defined in return_text().
for listing in sorted(root.findall('Listing'), key=return_text):
                                                  # Only want descriptions containing the word 'and',
                                                  # and only listings posted in 2016.
          if ' and ' in listing.find('.//Description').text and '2016' in listing.find('.//DateListed').text:
          
                                                  # Search each desired tag for child elements 
                                                  # and add their text to the row.
                    row = get_data(listing, charlimit)
          
                    csvwriter.writerow(row)



Test_data.close()

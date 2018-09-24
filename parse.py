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


# Function takes a listing (ET.element object) and returns string
# containing what we want to sort the listings by.
# Need this as the key for sorting by date or by anything else.
def return_text(listing):
                                        # Can change DateListed to whatever child tag
                                        # we want to sort by.
          return listing.find('.//DateListed').text


# Write csv header row.
header = ['MlsId','MlsName','DateListed','StreetAddress','Price','Bedrooms','Bathrooms','Appliances','Rooms','Description']
csvwriter.writerow(header)


                                        # Iterate search over each Listing element in the tree,
                                        # and sort by the tag's text (a string) defined in return_text().
for listing in sorted(root.findall('Listing'), key=return_text):
                                                  # Only want descriptions containing the word 'and',
                                                  # and only listings posted in 2016.
          if ' and ' in listing.find('.//Description').text and '2016' in listing.find('.//DateListed').text:
                    
                    row = []                  # A row to be populated for each listing.
          
                                                  # Search each desired tag for child elements 
                                                  # and add their text to the row.
                    MlsId = listing.find('.//MlsId').text
                    row.append(MlsId)
                    MlsName = listing.find('.//MlsName').text
                    row.append(MlsName)
                    DateListed = listing.find('.//DateListed').text
                    row.append(DateListed)
                    StreetAddress = listing.find('.//StreetAddress').text
                    row.append(StreetAddress)
                    Price = listing.find('.//Price').text
                    row.append(Price)
                    Bedrooms = listing.find('.//Bedrooms').text
                    row.append(Bedrooms)
                    Bathrooms = listing.find('.//Bathrooms').text
                    row.append(Bathrooms)
                                                  # Elements with additional children
                    Appliances = []               # have each child listed.
                    for appliance in listing.findall('.//Appliance'):
                              Appliances.append(appliance.text)
                    row.append(Appliances)
          
                    Rooms = []
                    for room in listing.findall('.//Room'):
                              Rooms.append(room.text)
                    row.append(Rooms)
          
                    Description = listing.find('.//Description').text[0:200]
                    row.append(Description)
          
                    csvwriter.writerow(row)



Test_data.close()

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


# Write csv header row.
header = ['MlsId','MlsName','DateListed','StreetAddress','Price','Bedrooms','Bathrooms','Appliances','Description']
csvwriter.writerow(header)

for node in root.findall('Listing'):    # Iterates searches over a list of each Listing.
          
          listing = []                  # A row to be populated.
          
                                        # Search each desired tag to find child nodes 
                                        # and add their text to the row.
          MlsId = node.find('.//MlsId').text
          listing.append(MlsId)
          MlsName = node.find('.//MlsName').text
          listing.append(MlsName)
          DateListed = node.find('.//DateListed').text
          listing.append(DateListed)
          StreetAddress = node.find('.//StreetAddress').text
          listing.append(StreetAddress)
          Price = node.find('.//Price').text
          listing.append(Price)
          Bedrooms = node.find('.//Bedrooms').text
          listing.append(Bedrooms)
          Bathrooms = node.find('.//Bathrooms').text
          listing.append(Bathrooms)
          Appliances = node.find('.//Appliances').text
          listing.append(Appliances)
          #Rooms = node.find('.//Rooms').text     # This text method fails if there is no Rooms tag in a listing.
          #listing.append(Rooms)
          Description = node.find('.//Description').text[0:200]
          listing.append(Description)
          
          csvwriter.writerow(listing)



Test_data.close()

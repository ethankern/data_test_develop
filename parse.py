import csv
import requests

# Grab xml data using requests.
URL = "http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml"
response = requests.get(URL)

# Open xml file and write requests content to it.
with open('BoojCodeTest.xml', 'wb) as file:
          file.write(response.content)

# Open a csv file and create csv writer object.
Test_data = open('TestData.csv', 'w')
csvwriter = csv.writer(Test_data)
          

          
Test_data(close)

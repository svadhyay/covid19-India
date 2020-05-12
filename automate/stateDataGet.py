from selenium import webdriver
from bs4 import BeautifulSoup
#import pandas as pd
import csv
#import vimpdb; vimpdb.set_trace()

# set driver as chrome
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# get data from website
driver.get("https://www.mohfw.gov.in")
content = driver.page_source
# parse html into soup
soup = BeautifulSoup(content,features="html.parser")
#stateDataSection = soup.findAll(id="state-data")

if True:
    #print("******* table header *********** ")
    tableHeader = soup.find('thead')
    headers = [header.text for header in tableHeader.findAll('th')]

if True:
    #print("******* table body *********** ")
    tableBody = soup.find('tbody')
    #print(tableBody)
    rows = []
    for row in tableBody.findAll('tr'):
        #rows.append([val.text.encode('utf8') for val in row.findAll('td')])
        rows.append([val.text for val in row.findAll('td')])
    #print("******* table rows *********** ")
    #print(rows)

    if True:
        with open('mohfwdata.csv','w',newline='') as f:
            writer = csv.writer(f)
            #writer = csv.writer(f,dialect='unix')
            writer.writerow(headers)
            writer.writerows(row for row in rows if row)

        # removing carriage return  TODO
        if False:
            with open('mohfwdata.csv', "rb") as inf:
                with open('mohfwdata1.csv', "w") as fixed:
                    for line in inf:
                        fixed.write(line)

    if False:
        print(" ************ print the csv *********** ")
        with open('mohfwdata.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        #print(" ************ print the existing csv *********** ")
        #with open('mohfw/2020_05_08_0800.csv', newline='') as f:
        #    reader = csv.reader(f)
        #    for row in reader:
        #        print(row)








# close the chrome driver tab
driver.quit()

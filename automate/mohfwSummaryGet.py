from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# set driver as chrome
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# get data from website
driver.get("https://www.mohfw.gov.in")
content = driver.page_source
# parse html into soup
soup = BeautifulSoup(content,features="html.parser")
print("############# type of soup is = ", type(soup))

if True:
    print("******* stats count div *********** ")
    siteStatsData = soup.find('div', class_='site-stats-count')
    #print(siteStatsData)
    print("############# type of siteStatsData is = ", type(siteStatsData))
    timeStamp = siteStatsData.find('div', class_='status-update')
    timeStamp = timeStamp.find('span')
    timeStamp = timeStamp.text
    print("timestamp text is --->",timeStamp,"<---")
    print("############# type of timeStamp is = ", type(timeStamp))
    hhmmStr = timeStamp[22:26]
    print("hhmm = ", hhmmStr)
#    as on : 14 May 2020, 08:00 IST (GMT+5:30)

#<div class="site-stats-count">
#                <ul>
#                <li class="bg-blue">
#                <img src="assets/images/icon-infected.png" alt="Active Status">
#                <strong>49219</strong>
#                <span>Active Cases</span>
#                </li>
#                <li class="bg-green">
#                <img src="assets/images/icon-inactive.png" alt="Inactive Status">
#                <strong>26234</strong>
#                <span class="mob-hide">Cured / Discharged </span>
#                <span class="mob-show">Cured/ </span>
#                <span class="mob-show">Discharged </span>
#                </li>								
#                <li class="bg-red">
#                <img src="assets/images/icon-death.png" alt="Death Status">
#                <strong>2549</strong>
#                <span>Deaths  </span>
#
#                </li>
#                <li class="bg-orange">
#                <img src="assets/images/icon-active.png" alt="Inactive Status">
#                <strong>1</strong>
#                <span>Migrated</span>
#                </li>
#                <li class="icon-dashboard">
#                <a class="trigger-advisories" href="#site-advisories"><img src="assets/images/icon-advisories.png" alt="Advisories"></a>
#                <a class="trigger-state" href="#state-data"><img src="assets/images/icon-state.png" alt="State Data"></a>
#                <a class="trigger-graph" href="http://www.mohfw.gov.in/index.php" target="_blank"><img src="assets/images/graph.png" alt="Graphics"></a>
#                </li>
#                </ul>
#                <div class="status-update">
#                <h2>COVID-19 INDIA <span>as on : 14 May 2020, 08:00 IST (GMT+5:30)</span></h2>
#                </div>
#</div>


# close the chrome driver tab
driver.quit()
